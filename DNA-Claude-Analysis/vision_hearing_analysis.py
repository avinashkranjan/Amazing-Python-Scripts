#!/usr/bin/env python3
"""
Vision and Hearing SNP Analysis Script
Analyzes vision and hearing-related genetic markers from 23andMe data
"""

import os
from collections import defaultdict
from datetime import datetime

# Paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
GENOME_FILE = f"{BASE_PATH}/data/genome_data.txt"
REPORTS_PATH = f"{BASE_PATH}/reports"

# =============================================================================
# SNP DATABASE - Vision and Hearing
# =============================================================================

VISION_SNPS = {
    "myopia": {
        "name": "Myopia (Nearsightedness)",
        "name_ru": "Миопия (близорукость)",
        "snps": {
            "rs524952": {
                "gene": "GJD2",
                "description": "Myopia susceptibility",
                "description_ru": "Предрасположенность к миопии",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("high", "Increased myopia risk (homozygous)", "Повышенный риск миопии (гомозигота)"),
                    "AG": ("moderate", "Moderate myopia risk", "Умеренный риск миопии"),
                    "AC": ("moderate", "Moderate myopia risk", "Умеренный риск миопии"),
                    "GG": ("normal", "Normal myopia risk", "Нормальный риск"),
                    "CC": ("normal", "Normal myopia risk", "Нормальный риск"),
                }
            },
            "rs634990": {
                "gene": "RASGRF1",
                "description": "Myopia development",
                "description_ru": "Развитие миопии",
                "risk_allele": "C",
                "interpretation": {
                    "CC": ("high", "Increased myopia risk", "Повышенный риск миопии"),
                    "CT": ("moderate", "Moderate myopia risk", "Умеренный риск миопии"),
                    "TT": ("normal", "Normal myopia risk", "Нормальный риск"),
                }
            },
            "rs17412774": {
                "gene": "ZNF644",
                "description": "High myopia susceptibility",
                "description_ru": "Предрасположенность к высокой миопии",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("high", "High risk of severe myopia", "Высокий риск тяжелой миопии"),
                    "AG": ("moderate", "Moderate risk of high myopia", "Умеренный риск высокой миопии"),
                    "GG": ("normal", "Normal risk", "Нормальный риск"),
                }
            },
        }
    },
    "amd": {
        "name": "Age-related Macular Degeneration (AMD)",
        "name_ru": "Возрастная макулярная дегенерация (ВМД)",
        "snps": {
            "rs1061170": {
                "gene": "CFH (Y402H)",
                "description": "Major AMD risk factor - Complement Factor H",
                "description_ru": "Основной фактор риска ВМД - фактор комплемента H",
                "risk_allele": "C",
                "interpretation": {
                    "CC": ("high", "7x increased AMD risk (homozygous risk)", "7-кратный риск ВМД (гомозигота риска)"),
                    "TC": ("moderate", "2.5x increased AMD risk (heterozygous)", "2.5-кратный риск ВМД (гетерозигота)"),
                    "CT": ("moderate", "2.5x increased AMD risk (heterozygous)", "2.5-кратный риск ВМД (гетерозигота)"),
                    "TT": ("normal", "Normal AMD risk", "Нормальный риск ВМД"),
                }
            },
            "rs10490924": {
                "gene": "ARMS2 (A69S)",
                "description": "AMD susceptibility - ARMS2 gene",
                "description_ru": "Предрасположенность к ВМД - ген ARMS2",
                "risk_allele": "T",
                "interpretation": {
                    "TT": ("high", "Significantly increased AMD risk", "Значительно повышенный риск ВМД"),
                    "GT": ("moderate", "Moderate AMD risk increase", "Умеренно повышенный риск ВМД"),
                    "GG": ("normal", "Normal AMD risk", "Нормальный риск ВМД"),
                }
            },
        }
    },
    "glaucoma": {
        "name": "Glaucoma",
        "name_ru": "Глаукома",
        "snps": {
            "rs10483727": {
                "gene": "SIX6",
                "description": "Primary open-angle glaucoma risk",
                "description_ru": "Риск первичной открытоугольной глаукомы",
                "risk_allele": "C",
                "interpretation": {
                    "CC": ("high", "Increased glaucoma risk", "Повышенный риск глаукомы"),
                    "CT": ("moderate", "Moderate glaucoma risk", "Умеренный риск глаукомы"),
                    "TC": ("moderate", "Moderate glaucoma risk", "Умеренный риск глаукомы"),
                    "TT": ("normal", "Normal glaucoma risk", "Нормальный риск глаукомы"),
                }
            },
            "rs4656461": {
                "gene": "TMCO1",
                "description": "Intraocular pressure regulation",
                "description_ru": "Регуляция внутриглазного давления",
                "risk_allele": "G",
                "interpretation": {
                    "GG": ("high", "Increased glaucoma risk", "Повышенный риск глаукомы"),
                    "AG": ("moderate", "Moderate glaucoma risk", "Умеренный риск глаукомы"),
                    "GA": ("moderate", "Moderate glaucoma risk", "Умеренный риск глаукомы"),
                    "AA": ("normal", "Normal glaucoma risk", "Нормальный риск глаукомы"),
                }
            },
        }
    },
    "cataracts": {
        "name": "Cataracts",
        "name_ru": "Катаракта",
        "snps": {
            "rs2165241": {
                "gene": "EPHA2",
                "description": "Age-related cataract susceptibility",
                "description_ru": "Предрасположенность к возрастной катаракте",
                "risk_allele": "T",
                "interpretation": {
                    "TT": ("high", "Increased cataract risk", "Повышенный риск катаракты"),
                    "CT": ("moderate", "Moderate cataract risk", "Умеренный риск катаракты"),
                    "TC": ("moderate", "Moderate cataract risk", "Умеренный риск катаракты"),
                    "CC": ("normal", "Normal cataract risk", "Нормальный риск катаракты"),
                }
            },
            "rs1048661": {
                "gene": "LOXL1",
                "description": "Exfoliation syndrome and secondary glaucoma",
                "description_ru": "Эксфолиативный синдром и вторичная глаукома",
                "risk_allele": "G",
                "interpretation": {
                    "GG": ("high", "Increased risk of exfoliation syndrome", "Повышенный риск эксфолиативного синдрома"),
                    "GT": ("moderate", "Moderate risk", "Умеренный риск"),
                    "TG": ("moderate", "Moderate risk", "Умеренный риск"),
                    "TT": ("normal", "Lower risk", "Пониженный риск"),
                }
            },
        }
    },
}

HEARING_SNPS = {
    "age_related_hearing_loss": {
        "name": "Age-Related Hearing Loss (Presbycusis)",
        "name_ru": "Возрастная потеря слуха (пресбиакузис)",
        "snps": {
            "rs7598759": {
                "gene": "GRM7",
                "description": "Glutamate receptor - hearing sensitivity",
                "description_ru": "Глутаматный рецептор - чувствительность слуха",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("high", "Increased risk of age-related hearing loss", "Повышенный риск возрастной потери слуха"),
                    "AG": ("moderate", "Moderate risk", "Умеренный риск"),
                    "GA": ("moderate", "Moderate risk", "Умеренный риск"),
                    "GG": ("normal", "Normal risk", "Нормальный риск"),
                }
            },
            "rs11928865": {
                "gene": "GRHL2",
                "description": "Cochlear hair cell function",
                "description_ru": "Функция волосковых клеток улитки",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("high", "Increased hearing loss risk", "Повышенный риск потери слуха"),
                    "AG": ("moderate", "Moderate risk", "Умеренный риск"),
                    "GA": ("moderate", "Moderate risk", "Умеренный риск"),
                    "GG": ("normal", "Normal risk", "Нормальный риск"),
                }
            },
        }
    },
    "hereditary_deafness": {
        "name": "Hereditary Deafness",
        "name_ru": "Наследственная глухота",
        "snps": {
            "rs80338939": {
                "gene": "GJB2 (35delG)",
                "description": "Most common cause of hereditary deafness",
                "description_ru": "Наиболее частая причина наследственной глухоты",
                "risk_allele": "delG",
                "interpretation": {
                    "--": ("high", "Homozygous 35delG - congenital deafness", "Гомозигота 35delG - врожденная глухота"),
                    "D": ("high", "Carrier of 35delG mutation - hearing loss risk", "Носитель мутации 35delG - риск потери слуха"),
                    "DI": ("moderate", "Heterozygous carrier of 35delG", "Гетерозиготный носитель 35delG"),
                    "II": ("normal", "Not a carrier of 35delG", "Не носитель 35delG"),
                    "GG": ("normal", "Not a carrier of 35delG", "Не носитель 35delG"),
                    "CC": ("normal", "Not a carrier of 35delG", "Не носитель 35delG"),
                    "CG": ("normal", "Not a carrier of 35delG", "Не носитель 35delG"),
                }
            },
        }
    },
    "noise_induced_hearing_loss": {
        "name": "Noise-Induced Hearing Loss (NIHL)",
        "name_ru": "Шумовая потеря слуха",
        "snps": {
            "rs7598759": {
                "gene": "GRM7",
                "description": "Susceptibility to noise damage",
                "description_ru": "Восприимчивость к шумовым повреждениям",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("high", "Increased NIHL susceptibility", "Повышенная восприимчивость к NIHL"),
                    "AG": ("moderate", "Moderate NIHL susceptibility", "Умеренная восприимчивость"),
                    "GA": ("moderate", "Moderate NIHL susceptibility", "Умеренная восприимчивость"),
                    "GG": ("normal", "Normal susceptibility", "Нормальная восприимчивость"),
                }
            },
            "rs4880": {
                "gene": "SOD2 (Ala16Val)",
                "description": "Oxidative stress protection in cochlea",
                "description_ru": "Защита от окислительного стресса в улитке",
                "risk_allele": "T",
                "interpretation": {
                    "TT": ("high", "Reduced antioxidant protection - NIHL risk", "Сниженная антиоксидантная защита - риск NIHL"),
                    "CT": ("moderate", "Moderate antioxidant protection", "Умеренная антиоксидантная защита"),
                    "TC": ("moderate", "Moderate antioxidant protection", "Умеренная антиоксидантная защита"),
                    "AT": ("moderate", "Moderate antioxidant protection", "Умеренная антиоксидантная защита"),
                    "TA": ("moderate", "Moderate antioxidant protection", "Умеренная антиоксидантная защита"),
                    "CC": ("normal", "Good antioxidant protection", "Хорошая антиоксидантная защита"),
                    "AA": ("normal", "Good antioxidant protection (Ala/Ala)", "Хорошая антиоксидантная защита (Ala/Ala)"),
                }
            },
        }
    },
    "otosclerosis": {
        "name": "Otosclerosis",
        "name_ru": "Отосклероз",
        "snps": {
            "rs39399": {
                "gene": "TGFB1",
                "description": "Abnormal bone remodeling in middle ear",
                "description_ru": "Аномальное ремоделирование кости среднего уха",
                "risk_allele": "C",
                "interpretation": {
                    "CC": ("high", "Increased otosclerosis risk", "Повышенный риск отосклероза"),
                    "CT": ("moderate", "Moderate otosclerosis risk", "Умеренный риск отосклероза"),
                    "TC": ("moderate", "Moderate otosclerosis risk", "Умеренный риск отосклероза"),
                    "TT": ("normal", "Normal risk", "Нормальный риск"),
                }
            },
        }
    },
    "menieres_disease": {
        "name": "Meniere's Disease",
        "name_ru": "Болезнь Меньера",
        "snps": {
            "rs4947296": {
                "gene": "NFKB1",
                "description": "Inflammatory response in inner ear",
                "description_ru": "Воспалительная реакция во внутреннем ухе",
                "risk_allele": "T",
                "interpretation": {
                    "TT": ("high", "Increased Meniere's disease risk", "Повышенный риск болезни Меньера"),
                    "CT": ("moderate", "Moderate risk", "Умеренный риск"),
                    "TC": ("moderate", "Moderate risk", "Умеренный риск"),
                    "CC": ("normal", "Normal risk", "Нормальный риск"),
                }
            },
        }
    },
}


def load_genome():
    """Load genome data from 23andMe file"""
    genome = {}
    with open(GENOME_FILE, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 4:
                rsid = parts[0]
                genotype = parts[3]
                genome[rsid] = genotype
    return genome


def analyze_vision(genome):
    """Analyze vision-related SNPs"""
    results = {
        "category": "Vision",
        "category_ru": "Зрение",
        "subcategories": {},
        "summary": {
            "high_risk": [],
            "moderate_risk": [],
            "normal": [],
            "not_found": []
        }
    }

    for subcat_key, subcat_data in VISION_SNPS.items():
        subcat_results = {
            "name": subcat_data["name"],
            "name_ru": subcat_data["name_ru"],
            "snps": {}
        }

        for rsid, snp_info in subcat_data["snps"].items():
            genotype = genome.get(rsid)

            if genotype and genotype != "--":
                # Normalize genotype (sort alleles for matching)
                sorted_genotype = "".join(sorted(genotype))
                original_genotype = genotype

                # Try to find interpretation
                interpretation = None
                for gt_key, interp in snp_info["interpretation"].items():
                    if gt_key == genotype or gt_key == sorted_genotype:
                        interpretation = interp
                        break

                if interpretation:
                    risk_level, desc_en, desc_ru = interpretation
                    snp_result = {
                        "gene": snp_info["gene"],
                        "genotype": original_genotype,
                        "risk_level": risk_level,
                        "description": snp_info["description"],
                        "description_ru": snp_info["description_ru"],
                        "interpretation": desc_en,
                        "interpretation_ru": desc_ru,
                    }
                    subcat_results["snps"][rsid] = snp_result

                    if risk_level == "high":
                        results["summary"]["high_risk"].append((rsid, snp_info["gene"], desc_en))
                    elif risk_level == "moderate":
                        results["summary"]["moderate_risk"].append((rsid, snp_info["gene"], desc_en))
                    else:
                        results["summary"]["normal"].append((rsid, snp_info["gene"]))
                else:
                    # Genotype found but no interpretation available
                    snp_result = {
                        "gene": snp_info["gene"],
                        "genotype": original_genotype,
                        "risk_level": "unknown",
                        "description": snp_info["description"],
                        "interpretation": f"Genotype {original_genotype} - no interpretation available",
                    }
                    subcat_results["snps"][rsid] = snp_result
            else:
                results["summary"]["not_found"].append((rsid, snp_info["gene"]))

        results["subcategories"][subcat_key] = subcat_results

    return results


def analyze_hearing(genome):
    """Analyze hearing-related SNPs"""
    results = {
        "category": "Hearing",
        "category_ru": "Слух",
        "subcategories": {},
        "summary": {
            "high_risk": [],
            "moderate_risk": [],
            "normal": [],
            "not_found": []
        }
    }

    for subcat_key, subcat_data in HEARING_SNPS.items():
        subcat_results = {
            "name": subcat_data["name"],
            "name_ru": subcat_data["name_ru"],
            "snps": {}
        }

        for rsid, snp_info in subcat_data["snps"].items():
            genotype = genome.get(rsid)

            if genotype and genotype != "--":
                # Normalize genotype
                sorted_genotype = "".join(sorted(genotype))
                original_genotype = genotype

                # Try to find interpretation
                interpretation = None
                for gt_key, interp in snp_info["interpretation"].items():
                    if gt_key == genotype or gt_key == sorted_genotype:
                        interpretation = interp
                        break

                if interpretation:
                    risk_level, desc_en, desc_ru = interpretation
                    snp_result = {
                        "gene": snp_info["gene"],
                        "genotype": original_genotype,
                        "risk_level": risk_level,
                        "description": snp_info["description"],
                        "description_ru": snp_info["description_ru"],
                        "interpretation": desc_en,
                        "interpretation_ru": desc_ru,
                    }
                    subcat_results["snps"][rsid] = snp_result

                    if risk_level == "high":
                        results["summary"]["high_risk"].append((rsid, snp_info["gene"], desc_en))
                    elif risk_level == "moderate":
                        results["summary"]["moderate_risk"].append((rsid, snp_info["gene"], desc_en))
                    else:
                        results["summary"]["normal"].append((rsid, snp_info["gene"]))
                else:
                    snp_result = {
                        "gene": snp_info["gene"],
                        "genotype": original_genotype,
                        "risk_level": "unknown",
                        "description": snp_info["description"],
                        "interpretation": f"Genotype {original_genotype} - no interpretation available",
                    }
                    subcat_results["snps"][rsid] = snp_result
            else:
                results["summary"]["not_found"].append((rsid, snp_info["gene"]))

        results["subcategories"][subcat_key] = subcat_results

    return results


def calculate_amd_risk(vision_results):
    """Calculate combined AMD risk from CFH and ARMS2 variants"""
    amd_data = vision_results["subcategories"].get("amd", {})
    snps = amd_data.get("snps", {})

    cfh_result = snps.get("rs1061170", {})
    arms2_result = snps.get("rs10490924", {})

    cfh_genotype = cfh_result.get("genotype", "")
    arms2_genotype = arms2_result.get("genotype", "")

    # Calculate risk multiplier
    cfh_risk = 1.0
    if cfh_genotype == "CC":
        cfh_risk = 7.0
    elif cfh_genotype in ["TC", "CT"]:
        cfh_risk = 2.5

    arms2_risk = 1.0
    if arms2_genotype == "TT":
        arms2_risk = 8.0
    elif arms2_genotype in ["GT", "TG"]:
        arms2_risk = 2.5

    combined_risk = cfh_risk * arms2_risk

    risk_assessment = {
        "cfh_genotype": cfh_genotype if cfh_genotype else "Not found",
        "cfh_risk_multiplier": cfh_risk,
        "arms2_genotype": arms2_genotype if arms2_genotype else "Not found",
        "arms2_risk_multiplier": arms2_risk,
        "combined_risk_multiplier": combined_risk,
        "risk_category": "Unknown"
    }

    if combined_risk >= 10:
        risk_assessment["risk_category"] = "Very High"
        risk_assessment["risk_category_ru"] = "Очень высокий"
        risk_assessment["recommendation"] = "Regular ophthalmologic screening strongly recommended"
        risk_assessment["recommendation_ru"] = "Настоятельно рекомендуется регулярный осмотр офтальмолога"
    elif combined_risk >= 5:
        risk_assessment["risk_category"] = "High"
        risk_assessment["risk_category_ru"] = "Высокий"
        risk_assessment["recommendation"] = "Regular eye exams recommended, consider AREDS supplements"
        risk_assessment["recommendation_ru"] = "Рекомендуются регулярные осмотры глаз, рассмотреть добавки AREDS"
    elif combined_risk >= 2:
        risk_assessment["risk_category"] = "Moderate"
        risk_assessment["risk_category_ru"] = "Умеренный"
        risk_assessment["recommendation"] = "Annual eye exams, healthy lifestyle"
        risk_assessment["recommendation_ru"] = "Ежегодные осмотры глаз, здоровый образ жизни"
    else:
        risk_assessment["risk_category"] = "Normal"
        risk_assessment["risk_category_ru"] = "Нормальный"
        risk_assessment["recommendation"] = "Standard eye care"
        risk_assessment["recommendation_ru"] = "Стандартный уход за глазами"

    return risk_assessment


def generate_report(vision_results, hearing_results, amd_risk):
    """Generate markdown report"""
    report = []

    # Header
    report.append("# Vision and Hearing Genetic Analysis Report")
    report.append(f"# Генетический анализ зрения и слуха\n")
    report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append("---\n")

    # Executive Summary
    report.append("## Executive Summary / Краткое резюме\n")

    # Vision summary
    vision_high = len(vision_results["summary"]["high_risk"])
    vision_moderate = len(vision_results["summary"]["moderate_risk"])
    vision_normal = len(vision_results["summary"]["normal"])

    report.append(f"### Vision / Зрение")
    report.append(f"- **High risk markers / Маркеры высокого риска:** {vision_high}")
    report.append(f"- **Moderate risk markers / Маркеры умеренного риска:** {vision_moderate}")
    report.append(f"- **Normal markers / Нормальные маркеры:** {vision_normal}\n")

    # Hearing summary
    hearing_high = len(hearing_results["summary"]["high_risk"])
    hearing_moderate = len(hearing_results["summary"]["moderate_risk"])
    hearing_normal = len(hearing_results["summary"]["normal"])

    report.append(f"### Hearing / Слух")
    report.append(f"- **High risk markers / Маркеры высокого риска:** {hearing_high}")
    report.append(f"- **Moderate risk markers / Маркеры умеренного риска:** {hearing_moderate}")
    report.append(f"- **Normal markers / Нормальные маркеры:** {hearing_normal}\n")

    report.append("---\n")

    # ==========================================================================
    # VISION SECTION
    # ==========================================================================
    report.append("# VISION ANALYSIS / АНАЛИЗ ЗРЕНИЯ\n")

    # AMD Risk Assessment
    report.append("## AMD Risk Assessment / Оценка риска ВМД\n")
    report.append(f"**CFH rs1061170:** {amd_risk['cfh_genotype']} (Risk: {amd_risk['cfh_risk_multiplier']}x)")
    report.append(f"**ARMS2 rs10490924:** {amd_risk['arms2_genotype']} (Risk: {amd_risk['arms2_risk_multiplier']}x)")
    report.append(f"**Combined Risk Multiplier / Комбинированный множитель риска:** {amd_risk['combined_risk_multiplier']}x")
    report.append(f"**Risk Category / Категория риска:** {amd_risk['risk_category']} / {amd_risk.get('risk_category_ru', '')}")
    report.append(f"**Recommendation / Рекомендация:** {amd_risk['recommendation']}")
    report.append(f"*{amd_risk.get('recommendation_ru', '')}*\n")

    # Detailed vision results by subcategory
    for subcat_key, subcat_data in vision_results["subcategories"].items():
        report.append(f"## {subcat_data['name']}")
        report.append(f"### {subcat_data['name_ru']}\n")

        if not subcat_data["snps"]:
            report.append("*No data available / Данные недоступны*\n")
            continue

        report.append("| SNP | Gene | Genotype | Risk | Interpretation |")
        report.append("|-----|------|----------|------|----------------|")

        for rsid, snp_data in subcat_data["snps"].items():
            risk_emoji = ""
            if snp_data["risk_level"] == "high":
                risk_emoji = "HIGH"
            elif snp_data["risk_level"] == "moderate":
                risk_emoji = "MODERATE"
            elif snp_data["risk_level"] == "normal":
                risk_emoji = "Normal"
            else:
                risk_emoji = "?"

            interpretation = snp_data.get("interpretation", "N/A")
            interpretation_ru = snp_data.get("interpretation_ru", "")

            report.append(f"| {rsid} | {snp_data['gene']} | {snp_data['genotype']} | {risk_emoji} | {interpretation} |")

        report.append("")

    report.append("---\n")

    # ==========================================================================
    # HEARING SECTION
    # ==========================================================================
    report.append("# HEARING ANALYSIS / АНАЛИЗ СЛУХА\n")

    # Detailed hearing results by subcategory
    for subcat_key, subcat_data in hearing_results["subcategories"].items():
        report.append(f"## {subcat_data['name']}")
        report.append(f"### {subcat_data['name_ru']}\n")

        if not subcat_data["snps"]:
            report.append("*No data available / Данные недоступны*\n")
            continue

        report.append("| SNP | Gene | Genotype | Risk | Interpretation |")
        report.append("|-----|------|----------|------|----------------|")

        for rsid, snp_data in subcat_data["snps"].items():
            risk_emoji = ""
            if snp_data["risk_level"] == "high":
                risk_emoji = "HIGH"
            elif snp_data["risk_level"] == "moderate":
                risk_emoji = "MODERATE"
            elif snp_data["risk_level"] == "normal":
                risk_emoji = "Normal"
            else:
                risk_emoji = "?"

            interpretation = snp_data.get("interpretation", "N/A")

            report.append(f"| {rsid} | {snp_data['gene']} | {snp_data['genotype']} | {risk_emoji} | {interpretation} |")

        report.append("")

    report.append("---\n")

    # ==========================================================================
    # RECOMMENDATIONS
    # ==========================================================================
    report.append("# Recommendations / Рекомендации\n")

    report.append("## Vision Recommendations / Рекомендации по зрению\n")

    if vision_high > 0:
        report.append("### High Risk Findings / Находки высокого риска:\n")
        for rsid, gene, desc in vision_results["summary"]["high_risk"]:
            report.append(f"- **{gene} ({rsid}):** {desc}")
        report.append("")

    report.append("### General Vision Care / Общий уход за зрением:")
    report.append("- Regular comprehensive eye exams / Регулярные комплексные осмотры глаз")
    report.append("- Protect eyes from UV radiation / Защита глаз от УФ-излучения")
    report.append("- Maintain healthy diet rich in antioxidants / Здоровое питание, богатое антиоксидантами")
    report.append("- Avoid smoking / Избегать курения")
    report.append("- Monitor blood pressure and cholesterol / Контроль артериального давления и холестерина\n")

    report.append("## Hearing Recommendations / Рекомендации по слуху\n")

    if hearing_high > 0:
        report.append("### High Risk Findings / Находки высокого риска:\n")
        for rsid, gene, desc in hearing_results["summary"]["high_risk"]:
            report.append(f"- **{gene} ({rsid}):** {desc}")
        report.append("")

    report.append("### General Hearing Care / Общий уход за слухом:")
    report.append("- Use hearing protection in loud environments / Использовать защиту слуха в шумной среде")
    report.append("- Limit exposure to loud music / Ограничить воздействие громкой музыки")
    report.append("- Regular hearing tests after age 50 / Регулярные тесты слуха после 50 лет")
    report.append("- Avoid ototoxic medications when possible / По возможности избегать ототоксичных препаратов")
    report.append("- Maintain cardiovascular health / Поддерживать здоровье сердечно-сосудистой системы\n")

    report.append("---\n")

    # Disclaimer
    report.append("## Disclaimer / Отказ от ответственности\n")
    report.append("*This report is for educational and informational purposes only. It should not be used for medical diagnosis or treatment decisions. Consult with healthcare professionals for personalized medical advice.*\n")
    report.append("*Этот отчет предназначен только для образовательных и информационных целей. Он не должен использоваться для медицинской диагностики или принятия решений о лечении. Проконсультируйтесь с медицинскими специалистами для получения персонализированных медицинских рекомендаций.*\n")

    return "\n".join(report)


def main():
    """Main function"""
    print("=" * 60)
    print("Vision and Hearing Genetic Analysis")
    print("=" * 60)

    # Load genome data
    print("\nLoading genome data...")
    genome = load_genome()
    print(f"Loaded {len(genome)} SNPs")

    # Analyze vision
    print("\nAnalyzing vision-related SNPs...")
    vision_results = analyze_vision(genome)

    # Analyze hearing
    print("Analyzing hearing-related SNPs...")
    hearing_results = analyze_hearing(genome)

    # Calculate AMD risk
    print("Calculating AMD risk...")
    amd_risk = calculate_amd_risk(vision_results)

    # Generate report
    print("\nGenerating report...")
    report = generate_report(vision_results, hearing_results, amd_risk)

    # Create output directory if needed
    output_dir = f"{REPORTS_PATH}/vision_hearing"
    os.makedirs(output_dir, exist_ok=True)

    # Save report
    output_file = f"{output_dir}/report.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nReport saved to: {output_file}")

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print("\n--- VISION ---")
    print(f"High risk: {len(vision_results['summary']['high_risk'])}")
    print(f"Moderate risk: {len(vision_results['summary']['moderate_risk'])}")
    print(f"Normal: {len(vision_results['summary']['normal'])}")
    print(f"Not found: {len(vision_results['summary']['not_found'])}")

    print(f"\nAMD Combined Risk: {amd_risk['combined_risk_multiplier']}x ({amd_risk['risk_category']})")

    print("\n--- HEARING ---")
    print(f"High risk: {len(hearing_results['summary']['high_risk'])}")
    print(f"Moderate risk: {len(hearing_results['summary']['moderate_risk'])}")
    print(f"Normal: {len(hearing_results['summary']['normal'])}")
    print(f"Not found: {len(hearing_results['summary']['not_found'])}")

    if vision_results['summary']['high_risk']:
        print("\n!!! HIGH RISK VISION MARKERS !!!")
        for rsid, gene, desc in vision_results['summary']['high_risk']:
            print(f"  - {gene} ({rsid}): {desc}")

    if hearing_results['summary']['high_risk']:
        print("\n!!! HIGH RISK HEARING MARKERS !!!")
        for rsid, gene, desc in hearing_results['summary']['high_risk']:
            print(f"  - {gene} ({rsid}): {desc}")


if __name__ == "__main__":
    main()
