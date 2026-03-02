#!/usr/bin/env python3
"""
Cognitive SNP Analysis Script
Analyzes cognitive-related genetic markers from 23andMe data
"""

import os
from collections import defaultdict
from datetime import datetime

# Paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
GENOME_FILE = f"{BASE_PATH}/data/genome_data.txt"
REPORTS_PATH = f"{BASE_PATH}/reports"

# =============================================================================
# SNP DATABASE - Organized by cognitive category
# =============================================================================

COGNITIVE_SNPS = {
    "memory": {
        "name": "Память",
        "snps": {
            "rs17070145": {
                "gene": "KIBRA (WWC1)",
                "description": "Эпизодическая память, консолидация воспоминаний",
                "risk_allele": "C",
                "interpretation": {
                    "TT": ("excellent", "Лучшая эпизодическая память - гомозигота по благоприятному аллелю"),
                    "CT": ("good", "Хорошая эпизодическая память - гетерозигота"),
                    "CC": ("normal", "Обычная эпизодическая память"),
                }
            },
            "rs4680": {
                "gene": "COMT Val158Met",
                "description": "Рабочая память, когнитивная гибкость, устойчивость к стрессу",
                "risk_allele": "-",
                "interpretation": {
                    "AA": ("info", "Met/Met ('Worrier') - лучше рабочая память в покое, выше тревожность под стрессом"),
                    "AG": ("info", "Val/Met - сбалансированный тип, адаптивная когнитивная гибкость"),
                    "GA": ("info", "Val/Met - сбалансированный тип, адаптивная когнитивная гибкость"),
                    "GG": ("info", "Val/Val ('Warrior') - лучше когниция под стрессом, хуже в покое"),
                }
            },
            "rs6265": {
                "gene": "BDNF Val66Met",
                "description": "Нейропластичность, обучение, память",
                "risk_allele": "A",
                "interpretation": {
                    "GG": ("normal", "Val/Val - нормальная секреция BDNF, хорошая нейропластичность"),
                    "CC": ("normal", "Val/Val - нормальная секреция BDNF, хорошая нейропластичность"),
                    "AG": ("moderate", "Val/Met - немного сниженная секреция BDNF"),
                    "CT": ("moderate", "Val/Met - немного сниженная секреция BDNF"),
                    "AA": ("reduced", "Met/Met - сниженная нейропластичность, но может быть компенсировано упражнениями"),
                    "TT": ("reduced", "Met/Met - сниженная нейропластичность, но может быть компенсировано упражнениями"),
                }
            },
        }
    },

    "cognitive_aging": {
        "name": "Когнитивное старение",
        "snps": {
            "rs429358": {
                "gene": "APOE (e4 маркер)",
                "description": "Болезнь Альцгеймера, когнитивное старение",
                "risk_allele": "C",
                "interpretation": {
                    "CC": ("high", "Вероятно e4/e4 - значительно повышен риск когнитивного снижения"),
                    "CT": ("moderate", "Вероятно носитель e4 - умеренно повышен риск"),
                    "TC": ("moderate", "Вероятно носитель e4 - умеренно повышен риск"),
                    "TT": ("normal", "Нет аллеля e4 - обычный риск когнитивного старения"),
                }
            },
            "rs7412": {
                "gene": "APOE (e2 маркер)",
                "description": "Защитный аллель против Альцгеймера",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("info", "Используется вместе с rs429358 для определения APOE генотипа"),
                    "CT": ("protective", "Возможно носитель e2 - защитный эффект"),
                    "TC": ("protective", "Возможно носитель e2 - защитный эффект"),
                    "TT": ("info", "Используется вместе с rs429358 для определения APOE генотипа"),
                }
            },
            "rs9536314": {
                "gene": "KLOTHO",
                "description": "Ген долголетия, защита мозга от старения",
                "risk_allele": "-",
                "interpretation": {
                    "GT": ("excellent", "Гетерозигота KL-VS - оптимальный вариант, лучшее когнитивное старение"),
                    "TG": ("excellent", "Гетерозигота KL-VS - оптимальный вариант, лучшее когнитивное старение"),
                    "GG": ("normal", "Дикий тип - обычное когнитивное старение"),
                    "TT": ("reduced", "Гомозигота KL-VS - возможно сниженная функция (редко)"),
                }
            },
            "rs2802292": {
                "gene": "FOXO3",
                "description": "Ген долголетия, защита нейронов, клеточный стресс",
                "risk_allele": "T",
                "interpretation": {
                    "GG": ("excellent", "Ассоциирован с долголетием и лучшим когнитивным здоровьем"),
                    "GT": ("good", "Гетерозигота - умеренно защитный эффект"),
                    "TG": ("good", "Гетерозигота - умеренно защитный эффект"),
                    "TT": ("normal", "Обычный вариант"),
                }
            },
        }
    },

    "attention": {
        "name": "Внимание и дофамин",
        "snps": {
            "rs1800955": {
                "gene": "DRD4 -521 C/T",
                "description": "Дофаминовый рецептор D4, внимание, СДВГ",
                "risk_allele": "T",
                "interpretation": {
                    "TT": ("info", "Сниженная экспрессия DRD4 - может влиять на внимание"),
                    "CT": ("info", "Гетерозигота - средний уровень экспрессии DRD4"),
                    "TC": ("info", "Гетерозигота - средний уровень экспрессии DRD4"),
                    "CC": ("normal", "Нормальная экспрессия рецептора D4"),
                }
            },
            "rs1800497": {
                "gene": "DRD2/ANKK1 Taq1A",
                "description": "D2 дофаминовые рецепторы, внимание, обучение с подкреплением",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("moderate", "A1/A1 - меньше D2 рецепторов, может влиять на обучение и мотивацию"),
                    "AG": ("low", "A1/A2 - умеренно снижены D2 рецепторы"),
                    "GA": ("low", "A1/A2 - умеренно снижены D2 рецепторы"),
                    "GG": ("normal", "A2/A2 - нормальное количество D2 рецепторов"),
                }
            },
            "rs27072": {
                "gene": "DAT1 (SLC6A3)",
                "description": "Транспортер дофамина, скорость обработки информации",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("info", "Может влиять на дофаминергическую передачу"),
                    "AG": ("info", "Гетерозигота"),
                    "GA": ("info", "Гетерозигота"),
                    "GG": ("normal", "Обычный транспорт дофамина"),
                }
            },
        }
    },

    "verbal": {
        "name": "Вербальные способности",
        "snps": {
            "rs7794745": {
                "gene": "CNTNAP2",
                "description": "Развитие речи, языковые способности",
                "risk_allele": "T",
                "interpretation": {
                    "TT": ("moderate", "Ассоциирован со сниженными языковыми способностями"),
                    "AT": ("low", "Гетерозигота - небольшое влияние"),
                    "TA": ("low", "Гетерозигота - небольшое влияние"),
                    "AA": ("normal", "Нормальные языковые способности"),
                }
            },
            "rs17236239": {
                "gene": "CNTNAP2",
                "description": "Контактин-ассоциированный белок, нейроразвитие",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("moderate", "Может влиять на языковое развитие"),
                    "AG": ("low", "Гетерозигота"),
                    "GA": ("low", "Гетерозигота"),
                    "GG": ("normal", "Нормальный вариант"),
                }
            },
            "rs759178": {
                "gene": "FOXP2",
                "description": "Ген речи и языка, артикуляция, грамматика",
                "risk_allele": "-",
                "interpretation": {
                    "AA": ("info", "Вариант гена речи FOXP2"),
                    "AG": ("info", "Гетерозигота FOXP2"),
                    "GA": ("info", "Гетерозигота FOXP2"),
                    "GG": ("info", "Вариант гена речи FOXP2"),
                }
            },
        }
    },

    "neuroprotection": {
        "name": "Нейропротекция",
        "snps": {
            "rs1800629": {
                "gene": "TNF-a -308",
                "description": "Нейровоспаление, воспалительный ответ в мозге",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("high", "Высокая продукция TNF-a - повышенное нейровоспаление"),
                    "AG": ("moderate", "Умеренно повышенная продукция TNF-a"),
                    "GA": ("moderate", "Умеренно повышенная продукция TNF-a"),
                    "GG": ("normal", "Нормальный уровень TNF-a"),
                }
            },
            "rs1800795": {
                "gene": "IL-6 -174",
                "description": "Интерлейкин-6, нейровоспаление, когнитивное старение",
                "risk_allele": "C",
                "interpretation": {
                    "CC": ("moderate", "Повышенная продукция IL-6 - больше воспаления"),
                    "CG": ("low", "Умеренно повышенный уровень IL-6"),
                    "GC": ("low", "Умеренно повышенный уровень IL-6"),
                    "GG": ("normal", "Нормальный уровень IL-6 - меньше нейровоспаления"),
                }
            },
            "rs1800896": {
                "gene": "IL-10 -1082",
                "description": "Противовоспалительный цитокин, защита мозга",
                "risk_allele": "A",
                "interpretation": {
                    "GG": ("protective", "Высокая продукция IL-10 - хорошая противовоспалительная защита"),
                    "AG": ("normal", "Средняя продукция IL-10"),
                    "GA": ("normal", "Средняя продукция IL-10"),
                    "CT": ("normal", "Средняя продукция IL-10"),
                    "TC": ("normal", "Средняя продукция IL-10"),
                    "AA": ("reduced", "Низкая продукция IL-10 - сниженная противовоспалительная защита"),
                    "TT": ("reduced", "Низкая продукция IL-10 - сниженная противовоспалительная защита"),
                    "CC": ("protective", "Высокая продукция IL-10 - хорошая противовоспалительная защита"),
                }
            },
        }
    },

    "caffeine_cognition": {
        "name": "Кофеин и когниция",
        "snps": {
            "rs762551": {
                "gene": "CYP1A2",
                "description": "Метаболизм кофеина, когнитивные эффекты кофе",
                "risk_allele": "C",
                "interpretation": {
                    "AA": ("excellent", "Быстрый метаболизатор - кофеин улучшает когницию, низкий риск побочек"),
                    "AC": ("good", "Средний метаболизатор - умеренная польза от кофеина"),
                    "CA": ("good", "Средний метаболизатор - умеренная польза от кофеина"),
                    "CC": ("reduced", "Медленный метаболизатор - кофеин может вызывать тревожность, бессонницу"),
                }
            },
            "rs5751876": {
                "gene": "ADORA2A",
                "description": "Аденозиновый рецептор, тревожность от кофеина",
                "risk_allele": "C",
                "interpretation": {
                    "TT": ("excellent", "Меньше тревожности от кофе, лучше когнитивный эффект"),
                    "CT": ("good", "Умеренная чувствительность к тревожности от кофеина"),
                    "TC": ("good", "Умеренная чувствительность к тревожности от кофеина"),
                    "CC": ("sensitive", "Высокая тревожность от кофеина - рекомендуется ограничить"),
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
        'risk_level': None,
        'interpretation': None
    }

    if snp_id in genome_data:
        result['found'] = True
        raw_genotype = genome_data[snp_id]['genotype']
        result['genotype'] = raw_genotype
        result['chromosome'] = genome_data[snp_id]['chromosome']
        result['position'] = genome_data[snp_id]['position']

        # Try to find interpretation
        normalized = normalize_genotype(raw_genotype)
        interpretations = snp_info.get('interpretation', {})

        # Try both original and normalized genotype
        for gt in [raw_genotype, normalized]:
            if gt in interpretations:
                result['risk_level'], result['interpretation'] = interpretations[gt]
                break

        # If still not found, try reverse
        if result['interpretation'] is None and len(raw_genotype) == 2:
            reversed_gt = raw_genotype[::-1]
            if reversed_gt in interpretations:
                result['risk_level'], result['interpretation'] = interpretations[reversed_gt]

    return result


def determine_apoe_genotype(genome):
    """Determine APOE genotype from rs429358 and rs7412"""
    rs429358 = genome.get('rs429358', {}).get('genotype', '')
    rs7412 = genome.get('rs7412', {}).get('genotype', '')

    # APOE determination table
    # rs429358 (C=e4), rs7412 (T=e2)
    apoe_table = {
        ('TT', 'CC'): ('e2/e2', 'protective', 'Защитный генотип - пониженный риск когнитивного снижения'),
        ('TT', 'CT'): ('e2/e3', 'protective', 'Немного пониженный риск'),
        ('CT', 'CC'): ('e2/e4', 'moderate', 'Смешанный - один защитный, один рисковый аллель'),
        ('TT', 'TT'): ('e3/e3', 'normal', 'Наиболее распространенный генотип - обычный риск'),
        ('CT', 'CT'): ('e3/e4', 'high', 'Повышенный риск когнитивного снижения (~3x)'),
        ('CC', 'TT'): ('e4/e4', 'very_high', 'Значительно повышенный риск (~12x)'),
        ('CT', 'TT'): ('e3/e4', 'high', 'Повышенный риск когнитивного снижения (~3x)'),
        ('CC', 'CT'): ('e4/e4 или e3/e4', 'high', 'Повышенный риск'),
    }

    # Normalize genotypes
    n429 = normalize_genotype(rs429358)
    n7412 = normalize_genotype(rs7412)

    for (g1, g2), (apoe, risk, desc) in apoe_table.items():
        if normalize_genotype(g1) == n429 and normalize_genotype(g2) == n7412:
            return {
                'rs429358': rs429358,
                'rs7412': rs7412,
                'apoe_genotype': apoe,
                'risk_level': risk,
                'interpretation': desc
            }

    return {
        'rs429358': rs429358,
        'rs7412': rs7412,
        'apoe_genotype': 'Не определен',
        'risk_level': 'unknown',
        'interpretation': f'Комбинация {rs429358}/{rs7412} не в таблице'
    }


def determine_comt_profile(genome):
    """Determine COMT cognitive profile from rs4680"""
    rs4680 = genome.get('rs4680', {}).get('genotype', '')

    profiles = {
        'AA': ('Worrier (Met/Met)', 'cognitive',
               'Лучше рабочая память и исполнительные функции в спокойном состоянии. '
               'Может испытывать снижение когниции под стрессом. Рекомендуется: '
               'медитация, управление стрессом, избегать избытка кофеина.'),
        'AG': ('Intermediate (Val/Met)', 'balanced',
               'Сбалансированный профиль. Адаптивная когнитивная гибкость - '
               'хорошо работает и в покое, и под умеренным стрессом.'),
        'GA': ('Intermediate (Val/Met)', 'balanced',
               'Сбалансированный профиль. Адаптивная когнитивная гибкость - '
               'хорошо работает и в покое, и под умеренным стрессом.'),
        'GG': ('Warrior (Val/Val)', 'stress_resilient',
               'Лучше когнитивные функции под стрессом и давлением. '
               'Может хуже работать в рутинных спокойных условиях. '
               'Рекомендуется: умеренный стресс для оптимальной работы, дедлайны.')
    }

    if rs4680 in profiles:
        name, profile_type, desc = profiles[rs4680]
        return {
            'genotype': rs4680,
            'profile_name': name,
            'profile_type': profile_type,
            'description': desc
        }

    return {
        'genotype': rs4680,
        'profile_name': 'Не определен',
        'profile_type': 'unknown',
        'description': 'Генотип не распознан'
    }


def determine_caffeine_response(genome):
    """Determine cognitive response to caffeine"""
    rs762551 = genome.get('rs762551', {}).get('genotype', '')
    rs5751876 = genome.get('rs5751876', {}).get('genotype', '')

    # Metabolism speed
    metabolism = 'unknown'
    if rs762551 == 'AA':
        metabolism = 'fast'
    elif rs762551 in ['AC', 'CA']:
        metabolism = 'intermediate'
    elif rs762551 == 'CC':
        metabolism = 'slow'

    # Anxiety sensitivity
    anxiety = 'unknown'
    if rs5751876 == 'TT':
        anxiety = 'low'
    elif rs5751876 in ['CT', 'TC']:
        anxiety = 'moderate'
    elif rs5751876 == 'CC':
        anxiety = 'high'

    # Combined recommendation
    recommendations = {
        ('fast', 'low'): ('excellent', 'Отличный респондер на кофеин. 2-4 чашки кофе улучшат когницию без побочек.'),
        ('fast', 'moderate'): ('good', 'Хороший респондер. 2-3 чашки кофе, избегать после обеда.'),
        ('fast', 'high'): ('moderate', 'Быстрый метаболизм, но высокая тревожность. Ограничить до 1-2 чашек утром.'),
        ('intermediate', 'low'): ('good', 'Умеренный респондер. 1-2 чашки кофе, не позже 14:00.'),
        ('intermediate', 'moderate'): ('moderate', 'Средняя чувствительность. 1-2 чашки утром.'),
        ('intermediate', 'high'): ('limited', 'Средний метаболизм + высокая тревожность. Рассмотреть зеленый чай.'),
        ('slow', 'low'): ('moderate', 'Медленный метаболизм. 1 чашка утром, избегать после полудня.'),
        ('slow', 'moderate'): ('limited', 'Медленный метаболизм + тревожность. Максимум 1 чашка утром.'),
        ('slow', 'high'): ('avoid', 'Медленный метаболизм + высокая тревожность. Рекомендуется избегать кофеин.'),
    }

    key = (metabolism, anxiety)
    if key in recommendations:
        response, rec = recommendations[key]
    else:
        response, rec = ('unknown', 'Недостаточно данных для рекомендации')

    return {
        'cyp1a2_genotype': rs762551,
        'adora2a_genotype': rs5751876,
        'metabolism': metabolism,
        'anxiety_sensitivity': anxiety,
        'response_type': response,
        'recommendation': rec
    }


def generate_cognitive_report(all_results, genome):
    """Generate comprehensive cognitive report"""
    report = []
    report.append("# Когнитивный генетический профиль")
    report.append(f"\nДата анализа: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("\n---\n")

    report.append("## Важные предупреждения\n")
    report.append("1. **Это НЕ медицинский диагноз** - только информационный анализ")
    report.append("2. **Генетика - не приговор** - среда и образ жизни важнее")
    report.append("3. **Когнитивные способности многофакторны** - один ген не определяет интеллект")
    report.append("4. **Для медицинских решений** - консультация специалиста обязательна\n")

    report.append("---\n")

    # Statistics
    total_found = 0
    total_snps = 0
    for cat, results in all_results.items():
        total_snps += len(results)
        total_found += sum(1 for r in results if r['found'])

    report.append(f"## Статистика анализа\n")
    report.append(f"- Проанализировано SNP: {total_snps}")
    report.append(f"- Найдено в геноме: {total_found}")
    report.append(f"- Не найдено: {total_snps - total_found}\n")

    report.append("---\n")

    # COMT Profile
    report.append("## Когнитивный профиль COMT\n")
    comt = determine_comt_profile(genome)
    report.append(f"- **Генотип rs4680:** {comt['genotype']}")
    report.append(f"- **Профиль:** {comt['profile_name']}")
    report.append(f"- **Описание:** {comt['description']}\n")

    # APOE for cognitive aging
    report.append("## APOE генотип (когнитивное старение)\n")
    apoe = determine_apoe_genotype(genome)
    report.append(f"- rs429358: {apoe['rs429358']}")
    report.append(f"- rs7412: {apoe['rs7412']}")
    report.append(f"- **APOE генотип:** {apoe['apoe_genotype']}")
    report.append(f"- **Уровень риска:** {apoe['risk_level']}")
    report.append(f"- {apoe['interpretation']}\n")

    # Caffeine response
    report.append("## Ответ на кофеин\n")
    caffeine = determine_caffeine_response(genome)
    report.append(f"- **CYP1A2 (rs762551):** {caffeine['cyp1a2_genotype']} - метаболизм: {caffeine['metabolism']}")
    report.append(f"- **ADORA2A (rs5751876):** {caffeine['adora2a_genotype']} - тревожность: {caffeine['anxiety_sensitivity']}")
    report.append(f"- **Тип ответа:** {caffeine['response_type']}")
    report.append(f"- **Рекомендация:** {caffeine['recommendation']}\n")

    report.append("---\n")

    # Detailed results by category
    for category, results in all_results.items():
        cat_info = COGNITIVE_SNPS[category]
        report.append(f"## {cat_info['name']}\n")

        # Table
        report.append("| SNP | Ген | Генотип | Статус | Интерпретация |")
        report.append("|-----|-----|---------|--------|---------------|")

        for r in results:
            if r['found']:
                status = r['risk_level'] or 'н/д'
                interp = r['interpretation'] or 'Нет данных'
                report.append(f"| {r['snp_id']} | {r['gene']} | **{r['genotype']}** | {status} | {interp} |")
            else:
                report.append(f"| {r['snp_id']} | {r['gene']} | - | - | Не найден в геноме |")

        report.append("")

    report.append("---\n")

    # Key findings summary
    report.append("## Ключевые находки\n")

    # Collect notable findings
    excellent = []
    protective = []
    moderate_concerns = []
    high_concerns = []

    for category, results in all_results.items():
        for r in results:
            if r['risk_level'] == 'excellent':
                excellent.append((category, r))
            elif r['risk_level'] == 'protective':
                protective.append((category, r))
            elif r['risk_level'] in ['moderate', 'reduced']:
                moderate_concerns.append((category, r))
            elif r['risk_level'] in ['high', 'very_high']:
                high_concerns.append((category, r))

    if excellent:
        report.append("### Сильные стороны\n")
        for cat, r in excellent:
            report.append(f"- **{r['gene']}** ({r['genotype']}): {r['interpretation']}")
        report.append("")

    if protective:
        report.append("### Защитные факторы\n")
        for cat, r in protective:
            report.append(f"- **{r['gene']}** ({r['genotype']}): {r['interpretation']}")
        report.append("")

    if high_concerns:
        report.append("### Требуют внимания\n")
        for cat, r in high_concerns:
            report.append(f"- **{r['gene']}** ({r['genotype']}): {r['interpretation']}")
        report.append("")

    if moderate_concerns:
        report.append("### Умеренные особенности\n")
        for cat, r in moderate_concerns:
            report.append(f"- **{r['gene']}** ({r['genotype']}): {r['interpretation']}")
        report.append("")

    report.append("---\n")

    # Recommendations
    report.append("## Рекомендации по оптимизации когнитивных функций\n")

    report.append("### На основе вашего профиля:\n")

    # COMT-based recommendations
    if comt['profile_type'] == 'cognitive':
        report.append("**COMT (Worrier):**")
        report.append("- Практикуйте медитацию и дыхательные техники")
        report.append("- Ограничьте кофеин в стрессовые периоды")
        report.append("- Магний и L-теанин могут помочь\n")
    elif comt['profile_type'] == 'stress_resilient':
        report.append("**COMT (Warrior):**")
        report.append("- Используйте умеренный стресс для мотивации")
        report.append("- Дедлайны и соревновательность улучшат продуктивность")
        report.append("- Избегайте слишком спокойной рутины\n")

    # BDNF-based recommendations
    bdnf_result = None
    for r in all_results.get('memory', []):
        if r['snp_id'] == 'rs6265':
            bdnf_result = r
            break

    if bdnf_result and bdnf_result['risk_level'] in ['moderate', 'reduced']:
        report.append("**BDNF (сниженная нейропластичность):**")
        report.append("- Регулярные аэробные упражнения КРИТИЧЕСКИ важны")
        report.append("- Изучение нового (языки, музыка) стимулирует BDNF")
        report.append("- Omega-3 и куркумин поддерживают нейропластичность\n")

    # Inflammation-based recommendations
    inflammation_concern = False
    for r in all_results.get('neuroprotection', []):
        if r['risk_level'] in ['high', 'moderate']:
            inflammation_concern = True
            break

    if inflammation_concern:
        report.append("**Нейровоспаление:**")
        report.append("- Противовоспалительная диета (средиземноморская)")
        report.append("- Omega-3 жирные кислоты")
        report.append("- Достаточный сон (7-9 часов)")
        report.append("- Контроль хронического стресса\n")

    report.append("### Общие рекомендации:\n")
    report.append("- Регулярные физические упражнения (150+ мин/неделю)")
    report.append("- Качественный сон 7-9 часов")
    report.append("- Постоянное обучение и интеллектуальные вызовы")
    report.append("- Социальная активность")
    report.append("- Управление стрессом")
    report.append("- Средиземноморская или MIND диета\n")

    return '\n'.join(report)


def main():
    print("=" * 60)
    print("КОГНИТИВНЫЙ ГЕНЕТИЧЕСКИЙ АНАЛИЗ")
    print("=" * 60)

    print("\n[1/3] Загрузка генома...")
    genome = load_genome()
    print(f"      Загружено {len(genome)} SNP")

    print("\n[2/3] Анализ когнитивных маркеров...")
    all_results = {}

    for category, cat_info in COGNITIVE_SNPS.items():
        print(f"      -> {cat_info['name']}...")
        results = []
        for snp_id, snp_info in cat_info['snps'].items():
            result = analyze_snp(snp_id, snp_info, genome)
            results.append(result)
        all_results[category] = results

        # Count found
        found = sum(1 for r in results if r['found'])
        print(f"         Найдено: {found}/{len(results)}")

    print("\n[3/3] Генерация отчета...")
    report = generate_cognitive_report(all_results, genome)

    # Ensure directory exists
    report_dir = f"{REPORTS_PATH}/cognitive"
    os.makedirs(report_dir, exist_ok=True)

    report_path = f"{report_dir}/report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"      -> {report_path}")

    print("\n" + "=" * 60)
    print("АНАЛИЗ ЗАВЕРШЕН")
    print("=" * 60)

    # Print key findings to console
    print("\nКЛЮЧЕВЫЕ НАХОДКИ:\n")

    # COMT profile
    comt = determine_comt_profile(genome)
    print(f"COMT профиль: {comt['profile_name']}")
    print(f"   {comt['description'][:80]}...\n")

    # APOE
    apoe = determine_apoe_genotype(genome)
    print(f"APOE генотип: {apoe['apoe_genotype']}")
    print(f"   {apoe['interpretation']}\n")

    # Caffeine
    caffeine = determine_caffeine_response(genome)
    print(f"Кофеин: {caffeine['response_type']}")
    print(f"   {caffeine['recommendation']}\n")

    # Notable findings
    for category, results in all_results.items():
        notable = [r for r in results if r['risk_level'] in ['excellent', 'high', 'very_high', 'protective']]
        if notable:
            print(f"{COGNITIVE_SNPS[category]['name']}:")
            for r in notable:
                print(f"   * {r['gene']} ({r['genotype']}): {r['interpretation']}")
            print()


if __name__ == "__main__":
    main()
