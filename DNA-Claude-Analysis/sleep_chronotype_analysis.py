#!/usr/bin/env python3
"""
Sleep and Chronotype Analysis Script
Analyzes sleep-related genetic markers from 23andMe data
"""

import os
from collections import defaultdict
from datetime import datetime

# Paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
GENOME_FILE = f"{BASE_PATH}/data/genome_data.txt"
REPORTS_PATH = f"{BASE_PATH}/reports"

# =============================================================================
# SNP DATABASE - Organized by sleep category
# =============================================================================

SLEEP_SNPS = {
    "chronotype": {
        "name": "Chronotype (Morning/Evening Preference)",
        "description": "Genetic factors influencing circadian rhythm and sleep-wake timing",
        "snps": {
            "rs1801260": {
                "gene": "CLOCK",
                "description": "Master circadian clock gene - morning/evening preference",
                "risk_allele": "C",
                "interpretation": {
                    "TT": ("morning", "Morning person (lark) - natural early riser"),
                    "TC": ("intermediate", "Intermediate chronotype - flexible schedule"),
                    "CT": ("intermediate", "Intermediate chronotype - flexible schedule"),
                    "CC": ("evening", "Evening person (owl) - natural night owl"),
                }
            },
            "rs2304672": {
                "gene": "PER2",
                "description": "Period circadian protein 2 - circadian rhythm regulation",
                "risk_allele": "G",
                "interpretation": {
                    "CC": ("normal", "Typical circadian rhythm"),
                    "CG": ("delayed", "Slightly delayed circadian phase"),
                    "GC": ("delayed", "Slightly delayed circadian phase"),
                    "GG": ("delayed", "Delayed sleep phase tendency - later sleep times"),
                }
            },
            "rs228697": {
                "gene": "PER3",
                "description": "Period circadian protein 3 - sleep timing and duration",
                "risk_allele": "G",
                "interpretation": {
                    "CC": ("morning", "Morning preference, shorter sleep need"),
                    "CG": ("intermediate", "Intermediate chronotype"),
                    "GC": ("intermediate", "Intermediate chronotype"),
                    "GG": ("evening", "Evening preference, may need more sleep"),
                }
            },
        }
    },

    "sleep_depth": {
        "name": "Sleep Depth and Quality",
        "description": "Genetic factors affecting sleep depth and sensitivity to disturbances",
        "snps": {
            "rs73598374": {
                "gene": "ADA",
                "description": "Adenosine deaminase - adenosine metabolism affects sleep depth",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("deep", "Deep sleeper - less sensitive to disturbances"),
                    "CT": ("average", "Average sleep depth"),
                    "TC": ("average", "Average sleep depth"),
                    "TT": ("light", "Light sleeper - more sensitive to disturbances"),
                }
            },
            "rs5751876": {
                "gene": "ADORA2A",
                "description": "Adenosine A2A receptor - sleep pressure and caffeine sensitivity",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("deep", "Normal adenosine signaling - good sleep quality"),
                    "CT": ("average", "Moderate caffeine sensitivity"),
                    "TC": ("average", "Moderate caffeine sensitivity"),
                    "TT": ("light", "High caffeine sensitivity - disturbed sleep from caffeine"),
                }
            },
        }
    },

    "sleep_duration": {
        "name": "Sleep Duration",
        "description": "Genetic factors influencing natural sleep length",
        "snps": {
            "rs1823125": {
                "gene": "PAX8",
                "description": "Paired box 8 - associated with sleep duration",
                "risk_allele": "G",
                "interpretation": {
                    "AA": ("long", "Tendency for longer sleep duration (>8h)"),
                    "AG": ("average", "Average sleep duration needs (~7-8h)"),
                    "GA": ("average", "Average sleep duration needs (~7-8h)"),
                    "GG": ("short", "Short sleeper tendency (<7h may be sufficient)"),
                }
            },
            "rs11046205": {
                "gene": "ABCC9",
                "description": "ATP-binding cassette C9 - sleep duration regulation",
                "risk_allele": "A",
                "interpretation": {
                    "GG": ("short", "Short sleep duration tendency"),
                    "AG": ("average", "Average sleep duration"),
                    "GA": ("average", "Average sleep duration"),
                    "AA": ("long", "Longer sleep duration needed (~30 min more)"),
                }
            },
        }
    },

    "melatonin": {
        "name": "Melatonin Regulation",
        "description": "Genetic factors affecting melatonin production and sensitivity",
        "snps": {
            "rs10830963": {
                "gene": "MTNR1B",
                "description": "Melatonin receptor 1B - melatonin signaling",
                "risk_allele": "G",
                "interpretation": {
                    "CC": ("normal", "Normal melatonin receptor function"),
                    "CG": ("reduced", "Slightly reduced melatonin sensitivity"),
                    "GC": ("reduced", "Slightly reduced melatonin sensitivity"),
                    "GG": ("reduced", "Reduced melatonin receptor function - may benefit from melatonin"),
                }
            },
            "rs4753426": {
                "gene": "MTNR1B",
                "description": "Melatonin receptor 1B variant - chronotype influence",
                "risk_allele": "C",
                "interpretation": {
                    "TT": ("normal", "Normal melatonin timing"),
                    "CT": ("delayed", "Slightly delayed melatonin onset"),
                    "TC": ("delayed", "Slightly delayed melatonin onset"),
                    "CC": ("delayed", "Delayed melatonin onset - later natural sleep time"),
                }
            },
        }
    },

    "restless_legs": {
        "name": "Restless Legs Syndrome Risk",
        "description": "Genetic factors associated with RLS and periodic limb movements",
        "snps": {
            "rs2300478": {
                "gene": "MEIS1",
                "description": "Meis homeobox 1 - strongest genetic factor for RLS",
                "risk_allele": "G",
                "interpretation": {
                    "AA": ("low", "Low risk for restless legs syndrome"),
                    "AG": ("moderate", "Moderate risk for RLS (~1.5x)"),
                    "GA": ("moderate", "Moderate risk for RLS (~1.5x)"),
                    "GG": ("high", "Elevated risk for restless legs syndrome (~2x)"),
                }
            },
            "rs3923809": {
                "gene": "BTBD9",
                "description": "BTB domain containing 9 - associated with RLS and PLM",
                "risk_allele": "A",
                "interpretation": {
                    "GG": ("low", "Lower risk for RLS and periodic limb movements"),
                    "AG": ("moderate", "Moderate risk for RLS"),
                    "GA": ("moderate", "Moderate risk for RLS"),
                    "AA": ("high", "Elevated risk for RLS and periodic limb movements"),
                }
            },
        }
    },

    "insomnia_risk": {
        "name": "Insomnia Risk",
        "description": "Genetic factors associated with insomnia susceptibility",
        "snps": {
            "rs113851554": {
                "gene": "MEIS1",
                "description": "MEIS1 insomnia variant - sleep onset difficulty",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("low", "Lower genetic risk for insomnia"),
                    "CT": ("moderate", "Moderate insomnia susceptibility"),
                    "TC": ("moderate", "Moderate insomnia susceptibility"),
                    "TT": ("high", "Higher genetic susceptibility to insomnia"),
                }
            },
        }
    },

    "caffeine_and_sleep": {
        "name": "Caffeine Metabolism and Sleep",
        "description": "Genetic factors affecting caffeine metabolism and its impact on sleep",
        "snps": {
            "rs762551": {
                "gene": "CYP1A2",
                "description": "Cytochrome P450 1A2 - primary caffeine metabolizer",
                "risk_allele": "C",
                "interpretation": {
                    "AA": ("fast", "Fast caffeine metabolizer - caffeine clears quickly"),
                    "AC": ("intermediate", "Intermediate caffeine metabolism"),
                    "CA": ("intermediate", "Intermediate caffeine metabolism"),
                    "CC": ("slow", "Slow caffeine metabolizer - caffeine affects sleep longer"),
                }
            },
            "rs5751876": {
                "gene": "ADORA2A",
                "description": "Adenosine A2A receptor - caffeine binding site",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("low_sensitivity", "Lower caffeine sensitivity - less sleep disruption"),
                    "CT": ("moderate_sensitivity", "Moderate caffeine sensitivity"),
                    "TC": ("moderate_sensitivity", "Moderate caffeine sensitivity"),
                    "TT": ("high_sensitivity", "High caffeine sensitivity - caffeine disrupts sleep"),
                }
            },
        }
    },
}


def load_genome():
    """Load genome data into a dictionary"""
    genome = {}
    with open(GENOME_FILE, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 4:
                rsid, chrom, pos, genotype = parts[0], parts[1], parts[2], parts[3]
                genome[rsid] = {
                    'chromosome': chrom,
                    'position': pos,
                    'genotype': genotype
                }
    return genome


def normalize_genotype(genotype):
    """Normalize genotype for comparison (sort alleles)"""
    if len(genotype) == 2:
        return ''.join(sorted(genotype))
    return genotype


def analyze_snp(snp_id, snp_info, genome_data):
    """Analyze a single SNP"""
    result = {
        'snp_id': snp_id,
        'gene': snp_info['gene'],
        'description': snp_info['description'],
        'risk_allele': snp_info['risk_allele'],
        'found': False,
        'genotype': None,
        'status': None,
        'interpretation': None
    }

    if snp_id in genome_data:
        result['found'] = True
        raw_genotype = genome_data[snp_id]['genotype']
        result['genotype'] = raw_genotype
        result['chromosome'] = genome_data[snp_id]['chromosome']
        result['position'] = genome_data[snp_id]['position']

        # Try to find interpretation
        interpretations = snp_info.get('interpretation', {})

        # Try original genotype
        if raw_genotype in interpretations:
            result['status'], result['interpretation'] = interpretations[raw_genotype]
        else:
            # Try normalized genotype
            normalized = normalize_genotype(raw_genotype)
            for gt, (status, interp) in interpretations.items():
                if normalize_genotype(gt) == normalized:
                    result['status'], result['interpretation'] = status, interp
                    break

        # If still not found, try reverse
        if result['interpretation'] is None and len(raw_genotype) == 2:
            reversed_gt = raw_genotype[::-1]
            if reversed_gt in interpretations:
                result['status'], result['interpretation'] = interpretations[reversed_gt]

    return result


def analyze_sleep(genome):
    """Analyze all sleep-related SNPs"""
    all_results = {}

    for category, cat_info in SLEEP_SNPS.items():
        results = []
        for snp_id, snp_info in cat_info['snps'].items():
            result = analyze_snp(snp_id, snp_info, genome)
            results.append(result)
        all_results[category] = results

    return all_results


def determine_chronotype(results):
    """Determine overall chronotype from multiple SNPs"""
    chronotype_results = results.get('chronotype', [])
    melatonin_results = results.get('melatonin', [])

    morning_score = 0
    evening_score = 0
    total_snps = 0

    # Score chronotype SNPs
    for r in chronotype_results:
        if r['found'] and r['status']:
            total_snps += 1
            if r['status'] == 'morning':
                morning_score += 2
            elif r['status'] == 'evening':
                evening_score += 2
            elif r['status'] == 'delayed':
                evening_score += 1
            elif r['status'] == 'intermediate':
                morning_score += 0.5
                evening_score += 0.5

    # Score melatonin SNPs
    for r in melatonin_results:
        if r['found'] and r['status']:
            total_snps += 1
            if r['status'] == 'delayed':
                evening_score += 1
            elif r['status'] == 'normal':
                morning_score += 0.5

    # Determine overall type
    if total_snps == 0:
        return {
            'type': 'unknown',
            'morning_score': 0,
            'evening_score': 0,
            'confidence': 'low',
            'description': 'Insufficient data to determine chronotype'
        }

    diff = morning_score - evening_score
    total_score = morning_score + evening_score

    if diff > 1.5:
        chrono_type = 'morning'
        description = 'Strong morning chronotype (lark) - naturally wake early, most alert in morning'
    elif diff > 0.5:
        chrono_type = 'moderate_morning'
        description = 'Moderate morning preference - function well with early schedule'
    elif diff < -1.5:
        chrono_type = 'evening'
        description = 'Strong evening chronotype (owl) - naturally stay up late, peak alertness evening'
    elif diff < -0.5:
        chrono_type = 'moderate_evening'
        description = 'Moderate evening preference - may struggle with early mornings'
    else:
        chrono_type = 'intermediate'
        description = 'Intermediate chronotype - adaptable to various schedules'

    confidence = 'high' if total_snps >= 4 else 'moderate' if total_snps >= 2 else 'low'

    return {
        'type': chrono_type,
        'morning_score': morning_score,
        'evening_score': evening_score,
        'confidence': confidence,
        'description': description
    }


def determine_sleep_quality(results):
    """Assess overall sleep quality predisposition"""
    depth_results = results.get('sleep_depth', [])
    rls_results = results.get('restless_legs', [])
    insomnia_results = results.get('insomnia_risk', [])

    quality_score = 5  # Start neutral (scale 1-10)
    factors = []

    # Sleep depth
    for r in depth_results:
        if r['found'] and r['status']:
            if r['status'] == 'deep':
                quality_score += 1
                factors.append(f"+ Deep sleep tendency ({r['gene']})")
            elif r['status'] == 'light':
                quality_score -= 1
                factors.append(f"- Light sleeper tendency ({r['gene']})")

    # RLS risk
    for r in rls_results:
        if r['found'] and r['status']:
            if r['status'] == 'high':
                quality_score -= 1.5
                factors.append(f"- Elevated RLS risk ({r['gene']})")
            elif r['status'] == 'low':
                quality_score += 0.5
                factors.append(f"+ Low RLS risk ({r['gene']})")

    # Insomnia risk
    for r in insomnia_results:
        if r['found'] and r['status']:
            if r['status'] == 'high':
                quality_score -= 1.5
                factors.append(f"- Higher insomnia susceptibility ({r['gene']})")
            elif r['status'] == 'low':
                quality_score += 0.5
                factors.append(f"+ Lower insomnia risk ({r['gene']})")

    # Clamp score
    quality_score = max(1, min(10, quality_score))

    if quality_score >= 7:
        assessment = 'Good genetic predisposition for sleep quality'
    elif quality_score >= 5:
        assessment = 'Average genetic sleep quality predisposition'
    else:
        assessment = 'May be genetically prone to sleep difficulties'

    return {
        'score': round(quality_score, 1),
        'assessment': assessment,
        'factors': factors
    }


def determine_caffeine_impact(results):
    """Assess caffeine's impact on sleep"""
    caffeine_results = results.get('caffeine_and_sleep', [])

    metabolism = 'unknown'
    sensitivity = 'unknown'
    cutoff_recommendation = 'Unknown - insufficient data'

    for r in caffeine_results:
        if not r['found']:
            continue

        if r['snp_id'] == 'rs762551':
            if r['status'] == 'fast':
                metabolism = 'fast'
            elif r['status'] == 'slow':
                metabolism = 'slow'
            else:
                metabolism = 'intermediate'

        if r['snp_id'] == 'rs5751876' and 'sensitivity' in r['status']:
            if 'high' in r['status']:
                sensitivity = 'high'
            elif 'low' in r['status']:
                sensitivity = 'low'
            else:
                sensitivity = 'moderate'

    # Determine cutoff recommendation
    if metabolism == 'slow' or sensitivity == 'high':
        cutoff_recommendation = 'Avoid caffeine after 12:00 PM (noon) - prolonged effects likely'
    elif metabolism == 'slow' and sensitivity == 'high':
        cutoff_recommendation = 'Avoid caffeine after 10:00 AM - very sensitive to caffeine effects'
    elif metabolism == 'fast' and sensitivity == 'low':
        cutoff_recommendation = 'Caffeine cutoff by 4:00 PM should be sufficient'
    elif metabolism == 'fast':
        cutoff_recommendation = 'Caffeine cutoff by 2:00-3:00 PM recommended'
    elif metabolism == 'intermediate':
        cutoff_recommendation = 'Caffeine cutoff by 2:00 PM recommended'

    return {
        'metabolism': metabolism,
        'sensitivity': sensitivity,
        'recommendation': cutoff_recommendation
    }


def get_sleep_recommendations(chronotype, sleep_quality, caffeine, results):
    """Generate personalized sleep recommendations based on genetic profile"""
    recommendations = []

    # Chronotype-based recommendations
    if chronotype['type'] in ['evening', 'moderate_evening']:
        recommendations.append({
            'category': 'Schedule',
            'title': 'Evening Chronotype Optimization',
            'details': [
                'If possible, shift work/school schedule later (start 9-10 AM)',
                'Use bright light exposure in morning to shift rhythm earlier',
                'Avoid bright screens 2+ hours before desired bedtime',
                'Consider melatonin 0.5-3mg 5-6 hours before desired sleep time',
                'Weekend sleep schedule should not differ by more than 1 hour'
            ]
        })
    elif chronotype['type'] in ['morning', 'moderate_morning']:
        recommendations.append({
            'category': 'Schedule',
            'title': 'Morning Chronotype Optimization',
            'details': [
                'Leverage natural early wake time for important tasks',
                'Schedule demanding work/exercise for morning hours',
                'Protect evening wind-down time - avoid stimulating activities',
                'Aim for consistent bedtime around 9:30-10:30 PM',
                'Avoid late-night social obligations when possible'
            ]
        })
    else:
        recommendations.append({
            'category': 'Schedule',
            'title': 'Flexible Chronotype',
            'details': [
                'Maintain consistent sleep/wake times (within 30 min daily)',
                'Can adapt to various schedules with proper sleep hygiene',
                'Use light exposure to fine-tune your rhythm as needed'
            ]
        })

    # Caffeine recommendations
    recommendations.append({
        'category': 'Caffeine',
        'title': 'Caffeine Management',
        'details': [
            caffeine['recommendation'],
            f"Caffeine metabolism: {caffeine['metabolism']}",
            f"Caffeine sensitivity: {caffeine['sensitivity']}",
            'Consider switching to decaf or tea in the afternoon',
            'If sleep issues persist, try eliminating caffeine for 2 weeks'
        ]
    })

    # Sleep quality recommendations
    duration_results = results.get('sleep_duration', [])
    duration_need = 'average'
    for r in duration_results:
        if r['found'] and r['status']:
            duration_need = r['status']
            break

    if duration_need == 'long':
        recommendations.append({
            'category': 'Duration',
            'title': 'Sleep Duration Needs',
            'details': [
                'Your genetics suggest you may need 8-9 hours of sleep',
                'Prioritize sleep - it is not optional for your genotype',
                'Track energy levels at different sleep durations',
                'Consider naps if nighttime sleep is insufficient'
            ]
        })
    elif duration_need == 'short':
        recommendations.append({
            'category': 'Duration',
            'title': 'Sleep Duration Needs',
            'details': [
                'You may function well on 6-7 hours of sleep',
                'However, still aim for 7+ hours for optimal health',
                'Monitor for signs of sleep debt (irritability, focus issues)',
                'Quality matters more than quantity for your type'
            ]
        })

    # RLS recommendations
    rls_results = results.get('restless_legs', [])
    rls_risk = 'low'
    for r in rls_results:
        if r['found'] and r['status'] in ['moderate', 'high']:
            rls_risk = r['status']
            break

    if rls_risk in ['moderate', 'high']:
        recommendations.append({
            'category': 'RLS Management',
            'title': 'Restless Legs Prevention',
            'details': [
                'Ensure adequate iron levels (ferritin > 75 ng/mL)',
                'Avoid alcohol and caffeine, especially evening',
                'Regular moderate exercise (but not close to bedtime)',
                'Leg stretches and massage before bed',
                'Consider magnesium supplementation',
                'Consult doctor if symptoms interfere with sleep'
            ]
        })

    # Light sleeper recommendations
    depth_results = results.get('sleep_depth', [])
    is_light_sleeper = any(r['status'] == 'light' for r in depth_results if r['found'])

    if is_light_sleeper:
        recommendations.append({
            'category': 'Environment',
            'title': 'Light Sleeper Optimization',
            'details': [
                'Use white noise machine or app',
                'Invest in quality earplugs designed for sleep',
                'Ensure complete darkness (blackout curtains)',
                'Cool bedroom temperature (65-68F / 18-20C)',
                'Consider separate blankets if sharing bed',
                'Address any partner snoring or movement'
            ]
        })

    # Melatonin recommendations
    melatonin_results = results.get('melatonin', [])
    reduced_melatonin = any(r['status'] in ['reduced', 'delayed'] for r in melatonin_results if r['found'])

    if reduced_melatonin:
        recommendations.append({
            'category': 'Melatonin',
            'title': 'Melatonin Optimization',
            'details': [
                'May benefit from low-dose melatonin (0.5-1mg)',
                'Take melatonin 1-2 hours before desired sleep time',
                'Ensure complete darkness in bedroom',
                'Reduce blue light exposure 2-3 hours before bed',
                'Consider red/amber lighting in evening',
                'Morning sunlight exposure helps regulate natural production'
            ]
        })

    return recommendations


def generate_report(results):
    """Generate comprehensive sleep analysis report"""
    report = []

    # Header
    report.append("# Sleep and Chronotype Analysis Report")
    report.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("\n---\n")

    # Disclaimer
    report.append("## Important Notes\n")
    report.append("- This analysis is for informational purposes only")
    report.append("- Genetics is one factor among many affecting sleep")
    report.append("- Environment, lifestyle, and health conditions also play major roles")
    report.append("- Consult a sleep specialist for persistent sleep issues\n")
    report.append("---\n")

    # Calculate overall assessments
    chronotype = determine_chronotype(results)
    sleep_quality = determine_sleep_quality(results)
    caffeine = determine_caffeine_impact(results)

    # Summary Section
    report.append("## Summary\n")

    report.append("### Your Chronotype\n")
    chrono_icon = {
        'morning': 'Early Bird (Lark)',
        'moderate_morning': 'Morning-Leaning',
        'intermediate': 'Intermediate',
        'moderate_evening': 'Evening-Leaning',
        'evening': 'Night Owl'
    }
    report.append(f"**Type:** {chrono_icon.get(chronotype['type'], chronotype['type'])}")
    report.append(f"\n**Confidence:** {chronotype['confidence'].capitalize()}")
    report.append(f"\n**Description:** {chronotype['description']}\n")

    report.append("### Sleep Quality Predisposition\n")
    report.append(f"**Score:** {sleep_quality['score']}/10")
    report.append(f"\n**Assessment:** {sleep_quality['assessment']}\n")
    if sleep_quality['factors']:
        report.append("**Contributing factors:**")
        for factor in sleep_quality['factors']:
            report.append(f"\n- {factor}")
        report.append("\n")

    report.append("### Caffeine Impact\n")
    report.append(f"**Metabolism:** {caffeine['metabolism'].capitalize()}")
    report.append(f"\n**Sensitivity:** {caffeine['sensitivity'].capitalize()}")
    report.append(f"\n**Recommendation:** {caffeine['recommendation']}\n")

    report.append("---\n")

    # Detailed Results by Category
    report.append("## Detailed Genetic Analysis\n")

    for category, cat_info in SLEEP_SNPS.items():
        cat_results = results.get(category, [])
        found_count = sum(1 for r in cat_results if r['found'])

        report.append(f"### {cat_info['name']}\n")
        report.append(f"*{cat_info['description']}*\n")
        report.append(f"Markers found: {found_count}/{len(cat_results)}\n")

        report.append("| SNP | Gene | Your Genotype | Status | Interpretation |")
        report.append("|-----|------|---------------|--------|----------------|")

        for r in cat_results:
            if r['found']:
                status = r['status'] or 'N/A'
                interp = r['interpretation'] or 'No interpretation available'
                report.append(f"| {r['snp_id']} | {r['gene']} | **{r['genotype']}** | {status} | {interp} |")
            else:
                report.append(f"| {r['snp_id']} | {r['gene']} | - | - | Not found in data |")

        report.append("")

    report.append("---\n")

    # Recommendations
    report.append("## Personalized Recommendations\n")
    recommendations = get_sleep_recommendations(chronotype, sleep_quality, caffeine, results)

    for rec in recommendations:
        report.append(f"### {rec['title']}\n")
        report.append(f"*Category: {rec['category']}*\n")
        for detail in rec['details']:
            report.append(f"- {detail}")
        report.append("")

    report.append("---\n")

    # Optimal Sleep Schedule
    report.append("## Suggested Sleep Schedule\n")

    if chronotype['type'] in ['morning', 'moderate_morning']:
        report.append("Based on your morning chronotype:\n")
        report.append("| Activity | Suggested Time |")
        report.append("|----------|----------------|")
        report.append("| Wake up | 5:30 - 6:30 AM |")
        report.append("| Morning light exposure | 6:00 - 7:00 AM |")
        report.append("| Peak alertness | 8:00 AM - 12:00 PM |")
        report.append("| Caffeine cutoff | 12:00 - 2:00 PM |")
        report.append("| Exercise | Before 6:00 PM |")
        report.append("| Dinner | 6:00 - 7:00 PM |")
        report.append("| Screen cutoff | 8:30 PM |")
        report.append("| Bedtime | 9:30 - 10:30 PM |")
    elif chronotype['type'] in ['evening', 'moderate_evening']:
        report.append("Based on your evening chronotype:\n")
        report.append("| Activity | Suggested Time |")
        report.append("|----------|----------------|")
        report.append("| Wake up | 7:30 - 8:30 AM |")
        report.append("| Morning light exposure | 8:00 - 9:00 AM |")
        report.append("| Peak alertness | 4:00 - 10:00 PM |")
        report.append("| Caffeine cutoff | 12:00 - 1:00 PM |")
        report.append("| Exercise | 4:00 - 7:00 PM |")
        report.append("| Dinner | 7:00 - 8:00 PM |")
        report.append("| Screen cutoff | 10:00 PM |")
        report.append("| Bedtime | 11:00 PM - 12:00 AM |")
    else:
        report.append("Based on your intermediate chronotype:\n")
        report.append("| Activity | Suggested Time |")
        report.append("|----------|----------------|")
        report.append("| Wake up | 6:30 - 7:30 AM |")
        report.append("| Morning light exposure | 7:00 - 8:00 AM |")
        report.append("| Peak alertness | 10:00 AM - 2:00 PM |")
        report.append("| Caffeine cutoff | 2:00 PM |")
        report.append("| Exercise | Before 7:00 PM |")
        report.append("| Dinner | 6:30 - 7:30 PM |")
        report.append("| Screen cutoff | 9:30 PM |")
        report.append("| Bedtime | 10:30 - 11:30 PM |")

    report.append("\n")
    report.append("---\n")

    # Sleep Hygiene Checklist
    report.append("## Universal Sleep Hygiene Checklist\n")
    report.append("Regardless of genetics, these practices improve sleep:\n")
    report.append("- [ ] Consistent sleep/wake times (even weekends)")
    report.append("- [ ] Cool bedroom (65-68F / 18-20C)")
    report.append("- [ ] Complete darkness (blackout curtains)")
    report.append("- [ ] No screens 1 hour before bed")
    report.append("- [ ] No large meals 3 hours before bed")
    report.append("- [ ] No alcohol 4 hours before bed")
    report.append("- [ ] Regular exercise (but not close to bedtime)")
    report.append("- [ ] Stress management practice (meditation, journaling)")
    report.append("- [ ] Comfortable mattress and pillows")
    report.append("- [ ] Reserve bed for sleep and intimacy only\n")

    return '\n'.join(report)


def main():
    """Main function to run the analysis"""
    print("Sleep and Chronotype Analysis")
    print("=" * 40)

    # Load genome data
    print(f"\nLoading genome data from: {GENOME_FILE}")
    genome = load_genome()
    print(f"Loaded {len(genome)} SNPs")

    # Analyze sleep SNPs
    print("\nAnalyzing sleep-related SNPs...")
    results = analyze_sleep(genome)

    # Count found SNPs
    total_snps = 0
    found_snps = 0
    for category, cat_results in results.items():
        for r in cat_results:
            total_snps += 1
            if r['found']:
                found_snps += 1

    print(f"Found {found_snps}/{total_snps} sleep-related SNPs in your data")

    # Determine chronotype
    chronotype = determine_chronotype(results)
    print(f"\nChronotype: {chronotype['type']} ({chronotype['confidence']} confidence)")
    print(f"Description: {chronotype['description']}")

    # Generate report
    print("\nGenerating report...")
    report = generate_report(results)

    # Save report
    output_dir = f"{REPORTS_PATH}/sleep_chronotype"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/report.md"

    with open(output_file, 'w') as f:
        f.write(report)

    print(f"\nReport saved to: {output_file}")
    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()
