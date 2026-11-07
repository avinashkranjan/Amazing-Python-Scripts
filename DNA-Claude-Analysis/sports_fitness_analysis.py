#!/usr/bin/env python3
"""
Sports and Fitness Genetic Analysis Script
Analyzes athletic performance markers from 23andMe data
"""

import os
from collections import defaultdict
from datetime import datetime

# Paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
GENOME_FILE = f"{BASE_PATH}/data/genome_data.txt"
REPORTS_PATH = f"{BASE_PATH}/reports"

# =============================================================================
# SNP DATABASE - Sports and Fitness Markers
# =============================================================================

SPORTS_SNPS = {
    "muscle_fiber_type": {
        "name": "Тип мышечных волокон",
        "description": "Определяет соотношение быстрых и медленных мышечных волокон",
        "snps": {
            "rs1815739": {
                "gene": "ACTN3",
                "description": "Альфа-актинин-3 - ключевой белок быстрых мышечных волокон",
                "interpretation": {
                    "CC": ("power", "RR - Полноценный ACTN3. Быстрые мышечные волокна (тип II). Предрасположенность к спринту и силовым видам"),
                    "CT": ("mixed", "RX - Смешанный тип. Один функциональный аллель. Универсальные способности"),
                    "TT": ("endurance", "XX - Дефицит ACTN3. Медленные волокна (тип I). Предрасположенность к выносливости"),
                }
            },
        }
    },

    "endurance": {
        "name": "Выносливость",
        "description": "Маркеры аэробной выносливости и метаболизма жиров",
        "snps": {
            "rs4253778": {
                "gene": "PPARA",
                "description": "Регулятор метаболизма жирных кислот и энергетического обмена",
                "interpretation": {
                    "GG": ("high", "G/G - Высокая экспрессия PPARA. Эффективное окисление жиров. Хорошая выносливость"),
                    "GC": ("moderate", "G/C - Средняя активность. Умеренная способность к выносливости"),
                    "CC": ("low", "C/C - Сниженная активность PPARA. Менее эффективное использование жиров"),
                }
            },
            "rs8192678": {
                "gene": "PPARGC1A (PGC-1α)",
                "description": "Мастер-регулятор митохондриального биогенеза",
                "interpretation": {
                    "CC": ("high", "Gly/Gly - Высокая активность PGC-1α. Отличный митохондриальный биогенез"),
                    "CT": ("moderate", "Gly/Ser - Умеренная активность. Хороший потенциал выносливости"),
                    "TT": ("low", "Ser/Ser - Сниженная активность. Меньший адаптивный ответ к тренировкам выносливости"),
                }
            },
            "rs2010963": {
                "gene": "VEGFA",
                "description": "Фактор роста эндотелия сосудов - ангиогенез и кровоснабжение мышц",
                "interpretation": {
                    "GG": ("high", "G/G - Высокая экспрессия VEGF. Отличный ангиогенез и капилляризация мышц"),
                    "GC": ("moderate", "G/C - Умеренная экспрессия. Хорошее кровоснабжение"),
                    "CC": ("low", "C/C - Сниженная экспрессия VEGF. Меньший ангиогенный ответ на тренировки"),
                }
            },
        }
    },

    "strength": {
        "name": "Сила и мышечная масса",
        "description": "Маркеры силовых способностей и гипертрофии",
        "snps": {
            "rs1800795": {
                "gene": "IL-6",
                "description": "Интерлейкин-6 - регулятор воспаления и мышечной адаптации",
                "interpretation": {
                    "GG": ("high", "G/G - Низкая продукция IL-6. Лучшее восстановление. Хороший силовой потенциал"),
                    "GC": ("moderate", "G/C - Умеренная продукция. Сбалансированный ответ"),
                    "CG": ("moderate", "C/G - Умеренная продукция. Сбалансированный ответ"),
                    "CC": ("low", "C/C - Высокая продукция IL-6. Больше воспаления. Медленнее восстановление"),
                }
            },
            "rs35767": {
                "gene": "IGF1",
                "description": "Инсулиноподобный фактор роста 1 - ключевой анаболический гормон",
                "interpretation": {
                    "CC": ("high", "C/C - Высокий уровень IGF-1. Хороший потенциал для набора мышечной массы"),
                    "CT": ("moderate", "C/T - Средний уровень IGF-1. Умеренный анаболический потенциал"),
                    "TT": ("low", "T/T - Сниженный IGF-1. Труднее набирать мышечную массу"),
                }
            },
        }
    },

    "lactate_clearance": {
        "name": "Метаболизм лактата",
        "description": "Способность утилизировать молочную кислоту",
        "snps": {
            "rs1049434": {
                "gene": "MCT1 (SLC16A1)",
                "description": "Транспортёр монокарбоксилатов - вывод лактата из мышц",
                "interpretation": {
                    "AA": ("high", "A/A - Высокая активность MCT1. Быстрый клиренс лактата. Отлично для интервальных тренировок"),
                    "AT": ("moderate", "A/T - Средняя активность. Умеренный клиренс лактата"),
                    "TT": ("low", "T/T - Сниженная активность MCT1. Медленнее выводится лактат. Дольше восстановление между подходами"),
                }
            },
        }
    },

    "recovery": {
        "name": "Восстановление",
        "description": "Маркеры регенерации и противовоспалительного ответа",
        "snps": {
            "rs1800629": {
                "gene": "TNF-α",
                "description": "Фактор некроза опухоли альфа - воспаление и катаболизм",
                "interpretation": {
                    "GG": ("fast", "G/G - Низкая продукция TNF-α. Быстрое восстановление. Меньше воспаления после тренировок"),
                    "GA": ("moderate", "G/A - Умеренная продукция. Среднее восстановление"),
                    "AG": ("moderate", "A/G - Умеренная продукция. Среднее восстановление"),
                    "AA": ("slow", "A/A - Высокая продукция TNF-α. Медленное восстановление. Больше мышечной боли"),
                }
            },
            "rs4880": {
                "gene": "SOD2 (MnSOD)",
                "description": "Супероксиддисмутаза 2 - антиоксидантная защита митохондрий",
                "interpretation": {
                    "TT": ("high", "Val/Val - Высокая активность SOD2. Отличная защита от оксидативного стресса"),
                    "CT": ("moderate", "Val/Ala - Средняя активность. Хорошая антиоксидантная защита"),
                    "TC": ("moderate", "Val/Ala - Средняя активность. Хорошая антиоксидантная защита"),
                    "CC": ("low", "Ala/Ala - Сниженная митохондриальная активность SOD2. Больше оксидативного стресса"),
                    "AA": ("high", "Val/Val - Высокая активность SOD2. Отличная защита от оксидативного стресса"),
                    "AG": ("moderate", "Val/Ala - Средняя активность. Хорошая антиоксидантная защита"),
                    "GG": ("low", "Ala/Ala - Сниженная активность SOD2. Больше оксидативного стресса"),
                }
            },
        }
    },

    "injury_risk": {
        "name": "Риск травм",
        "description": "Маркеры прочности соединительной ткани",
        "snps": {
            "rs12722": {
                "gene": "COL5A1",
                "description": "Коллаген V типа - структура сухожилий",
                "interpretation": {
                    "CC": ("low_risk", "C/C - Прочные сухожилия. Низкий риск тендинопатий"),
                    "CT": ("moderate_risk", "C/T - Средняя прочность сухожилий"),
                    "TT": ("high_risk", "T/T - Повышенная эластичность коллагена. Выше риск травм сухожилий (ахиллово, надколенника)"),
                }
            },
            "rs1800012": {
                "gene": "COL1A1",
                "description": "Коллаген I типа - структура связок и костей",
                "interpretation": {
                    "GG": ("low_risk", "G/G - Плотный коллаген. Низкий риск разрывов связок"),
                    "GT": ("moderate_risk", "G/T - Средняя прочность связок. Умеренный риск"),
                    "TG": ("moderate_risk", "T/G - Средняя прочность связок. Умеренный риск"),
                    "TT": ("high_risk", "T/T - Сниженная плотность коллагена. Повышен риск травм ПКС и других связок"),
                    "CC": ("low_risk", "C/C - Плотный коллаген. Низкий риск разрывов связок"),
                    "CT": ("moderate_risk", "C/T - Средняя прочность связок. Умеренный риск"),
                    "AA": ("high_risk", "A/A - Сниженная плотность коллагена. Повышен риск травм связок"),
                }
            },
            "rs2228570": {
                "gene": "VDR (FokI)",
                "description": "Рецептор витамина D - здоровье костей",
                "interpretation": {
                    "CC": ("low_risk", "F/F (C/C) - Активный рецептор VDR. Хорошее усвоение кальция. Крепкие кости"),
                    "CT": ("moderate_risk", "F/f (C/T) - Средняя активность VDR"),
                    "TC": ("moderate_risk", "F/f (T/C) - Средняя активность VDR"),
                    "TT": ("high_risk", "f/f (T/T) - Сниженная активность VDR. Риск низкой плотности костей. Важен витамин D"),
                }
            },
        }
    },

    "vo2max_potential": {
        "name": "Потенциал VO2max",
        "description": "Комплексная оценка аэробной мощности (на основе PPARGC1A, PPARA, VEGFA)",
        "snps": {}  # Calculated from endurance markers
    },

    "motor_learning": {
        "name": "Моторное обучение",
        "description": "Способность к освоению новых двигательных навыков",
        "snps": {
            "rs6265": {
                "gene": "BDNF",
                "description": "Нейротрофический фактор мозга - нейропластичность и моторная память",
                "interpretation": {
                    "CC": ("high", "Val/Val - Высокая секреция BDNF. Быстрое освоение техники. Отличная моторная память"),
                    "CT": ("moderate", "Val/Met - Умеренная секреция. Хорошее моторное обучение"),
                    "TC": ("moderate", "Val/Met - Умеренная секреция. Хорошее моторное обучение"),
                    "TT": ("low", "Met/Met - Сниженная секреция BDNF. Медленнее освоение новых навыков. Нужно больше повторений"),
                    "GG": ("high", "Val/Val - Высокая секреция BDNF. Быстрое освоение техники"),
                    "AG": ("moderate", "Val/Met - Умеренная секреция BDNF"),
                    "GA": ("moderate", "Val/Met - Умеренная секреция BDNF"),
                    "AA": ("low", "Met/Met - Сниженная секреция BDNF. Требуется больше практики"),
                }
            },
        }
    },

    "stress_response": {
        "name": "Стрессоустойчивость",
        "description": "Психологическая устойчивость к соревновательному стрессу",
        "snps": {
            "rs4680": {
                "gene": "COMT",
                "description": "Катехол-О-метилтрансфераза - метаболизм дофамина",
                "interpretation": {
                    "GG": ("warrior", "Val/Val - 'Воин'. Быстрый метаболизм дофамина. Устойчив к стрессу. Лучше в соревнованиях под давлением"),
                    "AG": ("mixed", "Val/Met - Смешанный тип. Баланс между стрессоустойчивостью и когнитивной точностью"),
                    "GA": ("mixed", "Val/Met - Смешанный тип. Баланс между стрессоустойчивостью и когнитивной точностью"),
                    "AA": ("worrier", "Met/Met - 'Тревожный'. Медленный метаболизм. Выше тревожность под давлением, но лучше точность и планирование"),
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
        'found': False,
        'genotype': None,
        'phenotype': None,
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

        # Try original, normalized, and reversed genotype
        for gt in [raw_genotype, normalize_genotype(raw_genotype), raw_genotype[::-1] if len(raw_genotype) == 2 else raw_genotype]:
            if gt in interpretations:
                result['phenotype'], result['interpretation'] = interpretations[gt]
                break

    return result


def analyze_sports(genome):
    """Analyze all sports-related SNPs"""
    all_results = {}

    for category, cat_info in SPORTS_SNPS.items():
        if not cat_info['snps']:  # Skip calculated categories
            continue

        results = []
        for snp_id, snp_info in cat_info['snps'].items():
            result = analyze_snp(snp_id, snp_info, genome)
            results.append(result)
        all_results[category] = results

    return all_results


def calculate_vo2max_potential(results):
    """Calculate VO2max potential based on endurance markers"""
    endurance_results = results.get('endurance', [])

    score = 0
    max_score = 0
    markers_found = 0

    scoring = {
        'high': 3,
        'moderate': 2,
        'low': 1
    }

    for r in endurance_results:
        if r['found'] and r['phenotype']:
            markers_found += 1
            max_score += 3
            score += scoring.get(r['phenotype'], 0)

    if markers_found == 0:
        return None

    percentage = (score / max_score) * 100

    if percentage >= 80:
        level = "Отличный"
        description = "Высокий генетический потенциал для развития VO2max. Хорошо откликаетесь на аэробные тренировки."
    elif percentage >= 60:
        level = "Хороший"
        description = "Хороший потенциал VO2max. При правильных тренировках можно достичь высоких показателей."
    elif percentage >= 40:
        level = "Средний"
        description = "Средний потенциал. Прогресс возможен, но может потребоваться больше времени."
    else:
        level = "Ниже среднего"
        description = "Генетически менее предрасположены к высоким аэробным показателям. Рекомендуется фокус на силовые виды."

    return {
        'score': score,
        'max_score': max_score,
        'percentage': percentage,
        'level': level,
        'description': description,
        'markers_found': markers_found
    }


def determine_athlete_profile(results):
    """Determine overall athlete profile (endurance/power/mixed)"""
    profile = {
        'power_score': 0,
        'endurance_score': 0,
        'max_power': 0,
        'max_endurance': 0
    }

    # ACTN3 - most important marker
    muscle_fiber = results.get('muscle_fiber_type', [])
    for r in muscle_fiber:
        if r['snp_id'] == 'rs1815739' and r['found']:
            profile['max_power'] += 3
            profile['max_endurance'] += 3
            if r['phenotype'] == 'power':
                profile['power_score'] += 3
            elif r['phenotype'] == 'endurance':
                profile['endurance_score'] += 3
            elif r['phenotype'] == 'mixed':
                profile['power_score'] += 1.5
                profile['endurance_score'] += 1.5

    # Endurance markers
    endurance_results = results.get('endurance', [])
    for r in endurance_results:
        if r['found'] and r['phenotype']:
            profile['max_endurance'] += 2
            if r['phenotype'] == 'high':
                profile['endurance_score'] += 2
            elif r['phenotype'] == 'moderate':
                profile['endurance_score'] += 1

    # Strength markers
    strength_results = results.get('strength', [])
    for r in strength_results:
        if r['found'] and r['phenotype']:
            profile['max_power'] += 2
            if r['phenotype'] == 'high':
                profile['power_score'] += 2
            elif r['phenotype'] == 'moderate':
                profile['power_score'] += 1

    # Lactate clearance - benefits both but more for power/interval
    lactate = results.get('lactate_clearance', [])
    for r in lactate:
        if r['found'] and r['phenotype']:
            profile['max_power'] += 1
            profile['max_endurance'] += 1
            if r['phenotype'] == 'high':
                profile['power_score'] += 1
                profile['endurance_score'] += 0.5
            elif r['phenotype'] == 'moderate':
                profile['power_score'] += 0.5
                profile['endurance_score'] += 0.25

    # Calculate percentages
    if profile['max_power'] > 0:
        profile['power_percentage'] = (profile['power_score'] / profile['max_power']) * 100
    else:
        profile['power_percentage'] = 50

    if profile['max_endurance'] > 0:
        profile['endurance_percentage'] = (profile['endurance_score'] / profile['max_endurance']) * 100
    else:
        profile['endurance_percentage'] = 50

    # Determine type
    power_pct = profile['power_percentage']
    endurance_pct = profile['endurance_percentage']

    diff = abs(power_pct - endurance_pct)

    if diff < 15:
        profile['type'] = 'mixed'
        profile['type_name'] = 'Универсальный атлет'
        profile['type_description'] = 'Сбалансированный профиль. Хорошо подходят как силовые, так и циклические виды спорта.'
    elif power_pct > endurance_pct:
        if diff > 30:
            profile['type'] = 'power'
            profile['type_name'] = 'Силовой/Спринтерский'
            profile['type_description'] = 'Выраженная предрасположенность к силовым и скоростно-силовым видам спорта.'
        else:
            profile['type'] = 'power_mixed'
            profile['type_name'] = 'Силовой с элементами универсальности'
            profile['type_description'] = 'Преобладание силовых качеств с хорошей базой для других направлений.'
    else:
        if diff > 30:
            profile['type'] = 'endurance'
            profile['type_name'] = 'Выносливый'
            profile['type_description'] = 'Выраженная предрасположенность к циклическим видам на выносливость.'
        else:
            profile['type'] = 'endurance_mixed'
            profile['type_name'] = 'Выносливый с элементами универсальности'
            profile['type_description'] = 'Преобладание выносливости с хорошей базой для силовых нагрузок.'

    return profile


def get_training_recommendations(profile, results):
    """Generate personalized training recommendations"""
    recommendations = []

    # Based on athlete type
    if profile['type'] in ['power', 'power_mixed']:
        recommendations.append({
            'category': 'Основной фокус',
            'items': [
                'Силовые тренировки 3-4 раза в неделю',
                'Спринтерская работа и плиометрика',
                'Взрывная сила и мощность',
                'Короткие интенсивные интервалы (10-30 сек)',
            ]
        })
        recommendations.append({
            'category': 'Рекомендуемые виды спорта',
            'items': [
                'Тяжёлая атлетика, пауэрлифтинг',
                'Спринт (100-400м), прыжки',
                'Единоборства, борьба',
                'Командные игры (футбол, баскетбол)',
                'Кроссфит',
            ]
        })
    elif profile['type'] in ['endurance', 'endurance_mixed']:
        recommendations.append({
            'category': 'Основной фокус',
            'items': [
                'Длительные аэробные тренировки',
                'Развитие базовой выносливости (зона 2)',
                'Темповые тренировки на лактатном пороге',
                'Длинные интервалы (3-8 мин)',
            ]
        })
        recommendations.append({
            'category': 'Рекомендуемые виды спорта',
            'items': [
                'Бег на длинные дистанции (5км - марафон)',
                'Триатлон, велоспорт',
                'Плавание на длинные дистанции',
                'Лыжные гонки, биатлон',
                'Гребля',
            ]
        })
    else:  # mixed
        recommendations.append({
            'category': 'Основной фокус',
            'items': [
                'Сочетание силовых и аэробных тренировок',
                'Периодизация: блоки силы чередуются с выносливостью',
                'Средние интервалы (1-3 мин)',
                'Функциональный тренинг',
            ]
        })
        recommendations.append({
            'category': 'Рекомендуемые виды спорта',
            'items': [
                'Кроссфит и функциональный фитнес',
                'Средние дистанции (800м - 5км)',
                'Игровые виды спорта',
                'Плавание',
                'Смешанные единоборства (ММА)',
            ]
        })

    # Recovery recommendations
    recovery = results.get('recovery', [])
    slow_recovery = False
    for r in recovery:
        if r['found'] and r['phenotype'] in ['slow', 'low']:
            slow_recovery = True
            break

    if slow_recovery:
        recommendations.append({
            'category': 'Восстановление (важно!)',
            'items': [
                'Увеличьте время между тяжёлыми тренировками (48-72ч)',
                'Приоритет сну (8+ часов)',
                'Противовоспалительное питание (омега-3, куркума)',
                'Регулярные массажи и миофасциальный релиз',
                'Контрастный душ и сауна',
            ]
        })
    else:
        recommendations.append({
            'category': 'Восстановление',
            'items': [
                'Стандартное время восстановления (24-48ч)',
                'Можно тренироваться чаще при хорошем самочувствии',
                'Следите за признаками перетренированности',
            ]
        })

    # Injury prevention
    injury = results.get('injury_risk', [])
    high_injury_risk = False
    for r in injury:
        if r['found'] and r['phenotype'] == 'high_risk':
            high_injury_risk = True
            break

    if high_injury_risk:
        recommendations.append({
            'category': 'Профилактика травм (приоритет!)',
            'items': [
                'Обязательная разминка 15-20 минут',
                'Эксцентрические упражнения для сухожилий',
                'Укрепление коллагена (витамин C + желатин/коллаген)',
                'Достаточный витамин D (проверьте уровень)',
                'Избегайте резкого увеличения нагрузок',
                'Работа над проприоцепцией и балансом',
            ]
        })

    # Stress response
    stress = results.get('stress_response', [])
    for r in stress:
        if r['snp_id'] == 'rs4680' and r['found']:
            if r['phenotype'] == 'worrier':
                recommendations.append({
                    'category': 'Психологическая подготовка',
                    'items': [
                        'Практикуйте техники релаксации перед соревнованиями',
                        'Используйте визуализацию успеха',
                        'Развивайте рутины и ритуалы для снижения тревоги',
                        'Ваше преимущество - точность и стратегическое мышление',
                    ]
                })
            elif r['phenotype'] == 'warrior':
                recommendations.append({
                    'category': 'Психологическая подготовка',
                    'items': [
                        'Ваше преимущество - устойчивость под давлением',
                        'Используйте адреналин соревнований',
                        'Можете полагаться на интуицию в стрессовых ситуациях',
                    ]
                })

    # Motor learning
    motor = results.get('motor_learning', [])
    for r in motor:
        if r['found'] and r['phenotype'] == 'low':
            recommendations.append({
                'category': 'Освоение техники',
                'items': [
                    'Больше времени на отработку техники',
                    'Разбивайте сложные движения на части',
                    'Используйте видео для анализа',
                    'Регулярная практика важнее интенсивности',
                ]
            })

    return recommendations


def generate_report(results, genome):
    """Generate comprehensive sports fitness report"""
    report = []

    # Header
    report.append("# Спортивно-генетический анализ")
    report.append(f"\nДата анализа: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("\n---\n")

    # Disclaimer
    report.append("## Важное предупреждение\n")
    report.append("- Генетика определяет потенциал, но не гарантирует результат")
    report.append("- Тренировки, питание и восстановление важнее генов")
    report.append("- Любой человек может улучшить свои показатели")
    report.append("- Используйте эту информацию для оптимизации, а не ограничения\n")

    report.append("---\n")

    # Athlete profile
    profile = determine_athlete_profile(results)
    report.append("## Профиль атлета\n")
    report.append(f"### {profile['type_name']}\n")
    report.append(f"{profile['type_description']}\n")
    report.append(f"- Силовой потенциал: **{profile['power_percentage']:.0f}%**")
    report.append(f"- Потенциал выносливости: **{profile['endurance_percentage']:.0f}%**\n")

    # VO2max potential
    vo2max = calculate_vo2max_potential(results)
    if vo2max:
        report.append("### Потенциал VO2max\n")
        report.append(f"- Уровень: **{vo2max['level']}** ({vo2max['percentage']:.0f}%)")
        report.append(f"- {vo2max['description']}\n")

    report.append("---\n")

    # Detailed results by category
    report.append("## Детальный анализ по категориям\n")

    for category, cat_info in SPORTS_SNPS.items():
        if not cat_info['snps']:
            continue

        cat_results = results.get(category, [])
        if not cat_results:
            continue

        report.append(f"### {cat_info['name']}\n")
        report.append(f"*{cat_info['description']}*\n")

        report.append("| SNP | Ген | Генотип | Результат |")
        report.append("|-----|-----|---------|-----------|")

        for r in cat_results:
            if r['found']:
                interp = r['interpretation'] or 'Нет данных'
                report.append(f"| {r['snp_id']} | {r['gene']} | **{r['genotype']}** | {interp} |")
            else:
                report.append(f"| {r['snp_id']} | {r['gene']} | - | Не найден в геноме |")

        report.append("")

    report.append("---\n")

    # Training recommendations
    recommendations = get_training_recommendations(profile, results)
    report.append("## Рекомендации по тренировкам\n")

    for rec in recommendations:
        report.append(f"### {rec['category']}\n")
        for item in rec['items']:
            report.append(f"- {item}")
        report.append("")

    report.append("---\n")

    # Statistics
    report.append("## Статистика анализа\n")

    total_snps = 0
    found_snps = 0
    for cat, cat_results in results.items():
        total_snps += len(cat_results)
        found_snps += sum(1 for r in cat_results if r['found'])

    report.append(f"- Проанализировано SNP: {total_snps}")
    report.append(f"- Найдено в геноме: {found_snps}")
    report.append(f"- Не найдено: {total_snps - found_snps}\n")

    # Key findings summary
    report.append("## Ключевые находки\n")

    # ACTN3
    muscle = results.get('muscle_fiber_type', [])
    for r in muscle:
        if r['snp_id'] == 'rs1815739' and r['found']:
            report.append(f"**ACTN3 (rs1815739):** {r['genotype']} - {r['interpretation']}\n")

    # COMT
    stress = results.get('stress_response', [])
    for r in stress:
        if r['snp_id'] == 'rs4680' and r['found']:
            report.append(f"**COMT (rs4680):** {r['genotype']} - {r['interpretation']}\n")

    # Injury risks
    injury = results.get('injury_risk', [])
    injury_issues = [r for r in injury if r['found'] and r['phenotype'] == 'high_risk']
    if injury_issues:
        report.append("**Повышенный риск травм:**")
        for r in injury_issues:
            report.append(f"- {r['gene']}: {r['interpretation']}")
        report.append("")

    return '\n'.join(report)


def main():
    print("=" * 60)
    print("СПОРТИВНО-ГЕНЕТИЧЕСКИЙ АНАЛИЗ")
    print("=" * 60)

    print("\n[1/4] Загрузка генома...")
    genome = load_genome()
    print(f"      Загружено {len(genome)} SNP")

    print("\n[2/4] Анализ спортивных маркеров...")
    results = analyze_sports(genome)

    for category, cat_results in results.items():
        found = sum(1 for r in cat_results if r['found'])
        print(f"      -> {SPORTS_SNPS[category]['name']}: {found}/{len(cat_results)}")

    print("\n[3/4] Определение профиля атлета...")
    profile = determine_athlete_profile(results)
    print(f"      Тип: {profile['type_name']}")
    print(f"      Силовой потенциал: {profile['power_percentage']:.0f}%")
    print(f"      Потенциал выносливости: {profile['endurance_percentage']:.0f}%")

    print("\n[4/4] Генерация отчёта...")
    report = generate_report(results, genome)

    # Ensure directory exists
    output_dir = f"{REPORTS_PATH}/sports_fitness"
    os.makedirs(output_dir, exist_ok=True)

    report_path = f"{output_dir}/report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"      -> {report_path}")

    print("\n" + "=" * 60)
    print("АНАЛИЗ ЗАВЕРШЁН")
    print("=" * 60)

    # Print key findings to console
    print("\nКЛЮЧЕВЫЕ НАХОДКИ:\n")

    # ACTN3
    muscle = results.get('muscle_fiber_type', [])
    for r in muscle:
        if r['snp_id'] == 'rs1815739' and r['found']:
            print(f"  ACTN3: {r['genotype']} - {r['interpretation']}")

    # COMT
    stress = results.get('stress_response', [])
    for r in stress:
        if r['snp_id'] == 'rs4680' and r['found']:
            print(f"  COMT: {r['genotype']} - {r['interpretation']}")

    print(f"\n  Профиль: {profile['type_name']}")
    print(f"  {profile['type_description']}")


if __name__ == "__main__":
    main()
