#!/usr/bin/env python3
"""
Psychology and Behavior Analysis Script
Analyzes psychological and behavioral genetic markers from 23andMe data
"""

import os
from collections import defaultdict
from datetime import datetime

# Paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
GENOME_FILE = f"{BASE_PATH}/data/genome_data.txt"
REPORTS_PATH = f"{BASE_PATH}/reports"

# =============================================================================
# DISCLAIMER
# =============================================================================

DISCLAIMER = """
**ВАЖНЫЙ ДИСКЛЕЙМЕР**

Гены - это предрасположенность, а НЕ судьба.

1. Генетические варианты влияют на склонности, но НЕ определяют поведение
2. Окружающая среда, воспитание и личный выбор играют огромную роль
3. Нейропластичность позволяет мозгу меняться на протяжении всей жизни
4. Один SNP редко определяет сложную черту - это всегда взаимодействие множества генов
5. Эффект большинства вариантов очень мал (обычно <1% влияния)
6. Этот анализ носит ТОЛЬКО информационный характер
7. Для психологической помощи обращайтесь к квалифицированному специалисту

Помните: вы НЕ раб своих генов. Осознание предрасположенностей может помочь
выработать более эффективные стратегии адаптации и развития.
"""

# =============================================================================
# SNP DATABASE - Psychology and Behavior
# =============================================================================

PSYCHOLOGY_SNPS = {
    "serotonin": {
        "name": "Серотониновая система",
        "description": "Регулирует настроение, тревожность, сон и импульсивность",
        "snps": {
            "rs25531": {
                "gene": "SLC6A4 (5-HTTLPR)",
                "description": "Транспортер серотонина - чувствительность к стрессу",
                "interpretation": {
                    "AA": ("high_sensitivity", "L/L - Высокая экспрессия транспортера, более устойчив к стрессу"),
                    "AG": ("moderate_sensitivity", "L/S - Умеренная чувствительность к стрессу"),
                    "GG": ("low_sensitivity", "S/S - Сниженная экспрессия, повышенная чувствительность к стрессу и негативным событиям"),
                },
                "impact": "Влияет на эмоциональную реактивность и восприимчивость к среде"
            },
            "rs6295": {
                "gene": "HTR1A",
                "description": "Рецептор серотонина 1A - тревожность и депрессия",
                "interpretation": {
                    "CC": ("higher_risk", "Повышенный риск тревожности и депрессии"),
                    "CG": ("moderate", "Умеренный риск"),
                    "GG": ("lower_risk", "Пониженный риск тревожности"),
                },
                "impact": "Влияет на базовый уровень тревожности"
            },
        }
    },

    "dopamine": {
        "name": "Дофаминовая система",
        "description": "Регулирует мотивацию, вознаграждение, внимание и исполнительные функции",
        "snps": {
            "rs4680": {
                "gene": "COMT Val158Met",
                "description": "Катехол-О-метилтрансфераза - разрушение дофамина в префронтальной коре",
                "interpretation": {
                    "GG": ("warrior", "Val/Val - 'Воин' (Warrior): быстрое разрушение дофамина, устойчив к стрессу, но ниже базовый дофамин, импульсивнее"),
                    "AG": ("balanced", "Val/Met - Сбалансированный тип: средняя скорость, адаптивность к разным ситуациям"),
                    "AA": ("worrier", "Met/Met - 'Мыслитель' (Worrier): медленное разрушение, выше дофамин, лучше когнитивно, но выше тревожность"),
                },
                "impact": "Ключевой маркер когнитивного стиля и стрессоустойчивости"
            },
            "rs1800497": {
                "gene": "DRD2/ANKK1 Taq1A",
                "description": "Плотность D2 рецепторов дофамина",
                "interpretation": {
                    "AA": ("low_d2", "A1/A1 - Меньше D2 рецепторов: поиск новизны, риск зависимостей"),
                    "AG": ("moderate_d2", "A1/A2 - Умеренно снижены D2 рецепторы"),
                    "GG": ("normal_d2", "A2/A2 - Нормальное количество D2 рецепторов"),
                },
                "impact": "Влияет на чувствительность к вознаграждению"
            },
            "rs1800955": {
                "gene": "DRD4 -521C/T",
                "description": "Рецептор дофамина D4 - новизна и СДВГ",
                "interpretation": {
                    "TT": ("high_novelty", "Повышенный поиск новизны и стимуляции"),
                    "CT": ("moderate_novelty", "Умеренный поиск новизны"),
                    "CC": ("normal_novelty", "Стандартный уровень поиска новизны"),
                },
                "impact": "Влияет на потребность в стимуляции и новых впечатлениях"
            },
        }
    },

    "neuroplasticity": {
        "name": "Нейропластичность",
        "description": "Способность мозга к изменениям, обучению и восстановлению",
        "snps": {
            "rs6265": {
                "gene": "BDNF Val66Met",
                "description": "Нейротрофический фактор мозга - обучение и память",
                "interpretation": {
                    "CC": ("val_val", "Val/Val - Нормальная секреция BDNF, хорошая нейропластичность"),
                    "GG": ("val_val", "Val/Val - Нормальная секреция BDNF, хорошая нейропластичность"),
                    "CT": ("val_met", "Val/Met - Немного сниженная секреция, умеренное влияние на память"),
                    "AG": ("val_met", "Val/Met - Немного сниженная секреция, умеренное влияние на память"),
                    "TT": ("met_met", "Met/Met - Сниженная секреция BDNF, хуже эпизодическая память, выше риск депрессии при стрессе"),
                    "AA": ("met_met", "Met/Met - Сниженная секреция BDNF, хуже эпизодическая память, выше риск депрессии при стрессе"),
                },
                "impact": "Ключевой фактор обучения, памяти и восстановления после стресса"
            },
        }
    },

    "oxytocin": {
        "name": "Окситоциновая система",
        "description": "Регулирует социальное поведение, доверие и эмпатию",
        "snps": {
            "rs53576": {
                "gene": "OXTR",
                "description": "Рецептор окситоцина - социальность и эмпатия",
                "interpretation": {
                    "GG": ("high_empathy", "Высокая эмпатия: лучше распознают эмоции, более социальны, чувствительнее к социальной поддержке"),
                    "AG": ("moderate_empathy", "Умеренная эмпатия: средний уровень социальной чувствительности"),
                    "AA": ("lower_empathy", "Пониженная эмпатия: менее чувствительны к социальным сигналам, но более независимы"),
                },
                "impact": "Влияет на качество социальных связей и эмоциональный интеллект"
            },
            "rs2254298": {
                "gene": "OXTR",
                "description": "Рецептор окситоцина - привязанность",
                "interpretation": {
                    "AA": ("secure", "Более безопасный стиль привязанности"),
                    "AG": ("mixed", "Смешанный стиль"),
                    "GG": ("anxious", "Может быть склонность к тревожной привязанности"),
                },
                "impact": "Влияет на паттерны привязанности в отношениях"
            },
        }
    },

    "addiction_risk": {
        "name": "Риск зависимостей",
        "description": "Генетические факторы предрасположенности к аддиктивному поведению",
        "snps": {
            "rs1799971": {
                "gene": "OPRM1 A118G",
                "description": "Мю-опиоидный рецептор - реакция на опиоиды и алкоголь",
                "interpretation": {
                    "AA": ("normal", "Стандартная чувствительность к опиоидам и алкоголю"),
                    "AG": ("altered", "Изменённая реакция: возможно нужна бОльшая доза обезболивающих, иная реакция на алкоголь"),
                    "GG": ("high_risk", "Повышенный риск алкогольной зависимости, сниженная чувствительность к опиоидам"),
                },
                "impact": "Влияет на эндорфиновую систему вознаграждения"
            },
            "rs16969968": {
                "gene": "CHRNA5",
                "description": "Никотиновый рецептор - риск никотиновой зависимости",
                "interpretation": {
                    "AA": ("high_risk", "Повышенный риск никотиновой зависимости и тяжёлого курения"),
                    "AG": ("moderate_risk", "Умеренно повышенный риск"),
                    "GG": ("normal_risk", "Стандартный риск никотиновой зависимости"),
                },
                "impact": "Влияет на чувствительность к никотину"
            },
            "rs1800497": {
                "gene": "DRD2/ANKK1",
                "description": "D2 рецепторы - общий риск зависимостей",
                "interpretation": {
                    "AA": ("high_risk", "Повышенный риск различных зависимостей (алкоголь, азартные игры)"),
                    "AG": ("moderate_risk", "Умеренно повышенный риск"),
                    "GG": ("normal_risk", "Стандартный риск"),
                },
                "impact": "Ключевой маркер аддиктивной уязвимости"
            },
        }
    },

    "depression_anxiety": {
        "name": "Риск депрессии и тревожности",
        "description": "Генетические факторы психического здоровья",
        "snps": {
            "rs25531": {
                "gene": "SLC6A4",
                "description": "Транспортер серотонина - депрессия при стрессе",
                "interpretation": {
                    "GG": ("higher_risk", "S/S - Повышенный риск депрессии при жизненных стрессах"),
                    "AG": ("moderate_risk", "L/S - Умеренный риск"),
                    "AA": ("lower_risk", "L/L - Более устойчив к депрессии"),
                },
                "impact": "Взаимодействие генов и среды в развитии депрессии"
            },
            "rs6265": {
                "gene": "BDNF",
                "description": "Нейропластичность - депрессия",
                "interpretation": {
                    "TT": ("higher_risk", "Met/Met - Повышенный риск депрессии, особенно при стрессе"),
                    "AA": ("higher_risk", "Met/Met - Повышенный риск депрессии, особенно при стрессе"),
                    "CT": ("moderate_risk", "Val/Met - Умеренно повышенный риск"),
                    "AG": ("moderate_risk", "Val/Met - Умеренно повышенный риск"),
                    "CC": ("lower_risk", "Val/Val - Стандартный риск"),
                    "GG": ("lower_risk", "Val/Val - Стандартный риск"),
                },
                "impact": "Влияет на восстановление после стресса"
            },
            "rs4680": {
                "gene": "COMT",
                "description": "Тревожность и руминация",
                "interpretation": {
                    "AA": ("higher_anxiety", "Met/Met - Выше базовая тревожность, склонность к руминации"),
                    "AG": ("moderate", "Val/Met - Умеренный уровень"),
                    "GG": ("lower_anxiety", "Val/Val - Ниже базовая тревожность"),
                },
                "impact": "Влияет на уровень тревоги в покое"
            },
        }
    },

    "stress_resilience": {
        "name": "Стрессоустойчивость",
        "description": "Генетические факторы реакции на стресс",
        "snps": {
            "rs1360780": {
                "gene": "FKBP5",
                "description": "Регулятор кортизола - ПТСР и стрессовая реакция",
                "interpretation": {
                    "TT": ("sensitive", "Повышенная чувствительность к стрессу и травме, риск ПТСР"),
                    "CT": ("moderate", "Умеренная чувствительность"),
                    "CC": ("resilient", "Более устойчив к стрессу"),
                },
                "impact": "Ключевой регулятор стрессовой оси HPA"
            },
            "rs4680": {
                "gene": "COMT",
                "description": "Острый стресс",
                "interpretation": {
                    "GG": ("stress_resistant", "Warrior - хорошо работает под давлением"),
                    "AG": ("balanced", "Адаптивен к разным условиям"),
                    "AA": ("stress_sensitive", "Worrier - хуже работает под острым стрессом, лучше в спокойной обстановке"),
                },
                "impact": "Определяет реакцию на острый стресс"
            },
            "rs53576": {
                "gene": "OXTR",
                "description": "Социальная поддержка как буфер стресса",
                "interpretation": {
                    "GG": ("benefits_support", "Сильно выигрывает от социальной поддержки в стрессе"),
                    "AG": ("moderate_benefit", "Умеренная польза от поддержки"),
                    "AA": ("independent", "Менее зависим от социальной поддержки"),
                },
                "impact": "Влияет на эффективность социальных стратегий совладания"
            },
        }
    },

    "memory_cognition": {
        "name": "Память и когнитивные способности",
        "description": "Генетические факторы познавательных функций",
        "snps": {
            "rs17070145": {
                "gene": "KIBRA",
                "description": "Эпизодическая память",
                "interpretation": {
                    "TT": ("better_memory", "Лучшая эпизодическая память"),
                    "CT": ("average_memory", "Средняя память"),
                    "CC": ("lower_memory", "Немного сниженная эпизодическая память"),
                },
                "impact": "Влияет на запоминание событий и фактов"
            },
            "rs6265": {
                "gene": "BDNF",
                "description": "Рабочая память и обучение",
                "interpretation": {
                    "CC": ("normal", "Val/Val - Нормальная рабочая память"),
                    "GG": ("normal", "Val/Val - Нормальная рабочая память"),
                    "CT": ("reduced", "Val/Met - Немного снижена"),
                    "AG": ("reduced", "Val/Met - Немного снижена"),
                    "TT": ("lower", "Met/Met - Сниженная рабочая память"),
                    "AA": ("lower", "Met/Met - Сниженная рабочая память"),
                },
                "impact": "Влияет на способность удерживать информацию"
            },
            "rs4680": {
                "gene": "COMT",
                "description": "Когнитивная гибкость vs стабильность",
                "interpretation": {
                    "AA": ("stability", "Met/Met - Лучше когнитивная стабильность и рабочая память"),
                    "AG": ("balanced", "Val/Met - Баланс гибкости и стабильности"),
                    "GG": ("flexibility", "Val/Val - Лучше когнитивная гибкость и переключение"),
                },
                "impact": "Определяет когнитивный стиль"
            },
        }
    },
}


# =============================================================================
# COPING STRATEGIES based on genetic profile
# =============================================================================

COPING_STRATEGIES = {
    "warrior": {
        "title": "Стратегии для 'Воина' (Val/Val COMT)",
        "strengths": [
            "Хорошо работаете под давлением и в стрессовых ситуациях",
            "Быстро принимаете решения в критических условиях",
            "Устойчивы к эмоциональному выгоранию",
        ],
        "challenges": [
            "Можете быть импульсивны в спокойной обстановке",
            "Труднее концентрироваться на длительных когнитивных задачах",
            "Можете недооценивать эмоциональные нюансы",
        ],
        "strategies": [
            "Используйте дедлайны и умеренное давление для повышения продуктивности",
            "Разбивайте длинные задачи на короткие интенсивные сессии",
            "Практикуйте замедление перед важными решениями в спокойной обстановке",
            "Физические упражнения помогут канализировать энергию",
            "Медитация осознанности поможет развить внимание к деталям",
        ],
    },
    "worrier": {
        "title": "Стратегии для 'Мыслителя' (Met/Met COMT)",
        "strengths": [
            "Отличная рабочая память и когнитивные способности",
            "Внимательны к деталям и нюансам",
            "Глубокий анализ и продумывание решений",
        ],
        "challenges": [
            "Склонность к тревоге и руминации",
            "Хуже работаете под острым стрессом и давлением",
            "Можете 'застревать' в размышлениях",
        ],
        "strategies": [
            "Создавайте спокойную рабочую среду без внезапных дедлайнов",
            "Практикуйте техники управления тревогой (дыхание, прогрессивная релаксация)",
            "Готовьтесь к стрессовым ситуациям заранее через визуализацию",
            "Регулярные физические упражнения снижают базовый уровень тревоги",
            "Когнитивно-поведенческие техники для прерывания руминации",
            "L-теанин и магний могут помочь (после консультации с врачом)",
        ],
    },
    "balanced": {
        "title": "Стратегии для сбалансированного типа (Val/Met COMT)",
        "strengths": [
            "Адаптивны к разным условиям работы",
            "Хороший баланс скорости и точности",
            "Можете переключаться между режимами",
        ],
        "challenges": [
            "Можете недоиспользовать свою адаптивность",
            "Иногда сложно определить оптимальный режим",
        ],
        "strategies": [
            "Используйте свою гибкость - меняйте условия под задачу",
            "Экспериментируйте с разными рабочими режимами",
            "Развивайте оба навыка - и стрессоустойчивость, и глубокое мышление",
        ],
    },
    "high_empathy": {
        "title": "Стратегии для высокоэмпатичных (GG OXTR)",
        "strengths": [
            "Отличное понимание эмоций других людей",
            "Сильные социальные связи служат буфером стресса",
            "Хорошие коммуникативные навыки",
        ],
        "challenges": [
            "Риск эмоционального истощения от чужих проблем",
            "Сложнее ставить личные границы",
            "Чувствительность к социальному отвержению",
        ],
        "strategies": [
            "Практикуйте установку здоровых границ",
            "Выделяйте время на восстановление после интенсивного общения",
            "Используйте свои социальные сети как ресурс, но не перегружайте их",
            "Развивайте самосострадание наряду с состраданием к другим",
        ],
    },
    "lower_empathy": {
        "title": "Стратегии для независимого типа (AA OXTR)",
        "strengths": [
            "Независимость от социального одобрения",
            "Меньше риск эмоционального истощения",
            "Способность к объективным решениям",
        ],
        "challenges": [
            "Можете упускать социальные сигналы",
            "Труднее строить глубокие связи",
            "Меньше выигрываете от социальной поддержки",
        ],
        "strategies": [
            "Сознательно практикуйте 'чтение' эмоций других",
            "Развивайте навыки активного слушания",
            "Выбирайте качество связей над количеством",
            "Используйте другие стратегии совладания помимо социальных",
        ],
    },
    "stress_sensitive": {
        "title": "Стратегии при повышенной чувствительности к стрессу",
        "description": "Для носителей рисковых вариантов FKBP5, 5-HTTLPR, BDNF Met",
        "strategies": [
            "Приоритизируйте профилактику стресса над его преодолением",
            "Создавайте предсказуемую и стабильную среду",
            "Регулярный сон, питание и физическая активность критически важны",
            "Ограничьте воздействие негативных новостей и токсичных людей",
            "Рассмотрите регулярную работу с психологом как профилактику",
            "Практики осознанности особенно полезны для вас",
            "Избегайте алкоголя и других депрессантов в стрессе",
        ],
    },
    "addiction_prone": {
        "title": "Стратегии при повышенном риске зависимостей",
        "description": "Для носителей рисковых вариантов DRD2, OPRM1, CHRNA5",
        "strategies": [
            "Знание риска - это сила. Вы предупреждены.",
            "Избегайте 'попробовать' вещества с высоким аддиктивным потенциалом",
            "Развивайте здоровые источники дофамина: спорт, хобби, социальные связи",
            "Структурируйте свою жизнь - хаос увеличивает риск",
            "Обратите внимание на поведенческие зависимости (игры, соцсети, азарт)",
            "При назначении опиоидных обезболивающих - минимальный курс",
            "Рассмотрите профилактическую работу с аддиктологом",
        ],
    },
    "depression_risk": {
        "title": "Стратегии при повышенном риске депрессии",
        "description": "Для носителей S/S SLC6A4 + Met BDNF",
        "strategies": [
            "Регулярные физические упражнения - доказанный антидепрессант",
            "Поддерживайте социальные связи, даже когда не хочется",
            "Структура дня и рутины защищают от провалов",
            "Обратите внимание на ранние признаки: сон, аппетит, энергия",
            "Рассмотрите профилактическую терапию в периоды высокого стресса",
            "Омега-3 жирные кислоты и витамин D могут быть полезны",
            "При первых признаках депрессии - не ждите, обращайтесь за помощью",
        ],
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
        'impact': snp_info.get('impact', ''),
        'found': False,
        'genotype': None,
        'profile': None,
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
            result['profile'], result['interpretation'] = interpretations[raw_genotype]
        else:
            # Try normalized
            normalized = normalize_genotype(raw_genotype)
            if normalized in interpretations:
                result['profile'], result['interpretation'] = interpretations[normalized]
            else:
                # Try reversed
                reversed_gt = raw_genotype[::-1] if len(raw_genotype) == 2 else raw_genotype
                if reversed_gt in interpretations:
                    result['profile'], result['interpretation'] = interpretations[reversed_gt]

    return result


def analyze_psychology(genome):
    """Analyze all psychology-related SNPs"""
    all_results = {}

    for category, cat_info in PSYCHOLOGY_SNPS.items():
        results = []
        for snp_id, snp_info in cat_info['snps'].items():
            result = analyze_snp(snp_id, snp_info, genome)
            results.append(result)
        all_results[category] = results

    return all_results


def determine_profile(results):
    """Determine psychological profile from analysis results"""
    profile = {
        'comt_type': None,
        'oxtr_type': None,
        'stress_sensitivity': 'moderate',
        'addiction_risk': 'average',
        'depression_risk': 'average',
        'cognitive_style': None,
        'personality_traits': [],
        'risk_factors': [],
        'protective_factors': [],
    }

    # Extract key SNP results
    comt_result = None
    oxtr_result = None
    bdnf_result = None
    slc6a4_result = None
    fkbp5_result = None
    drd2_result = None
    oprm1_result = None
    chrna5_result = None
    kibra_result = None

    for category, cat_results in results.items():
        for r in cat_results:
            if r['snp_id'] == 'rs4680' and r['found']:
                comt_result = r
            elif r['snp_id'] == 'rs53576' and r['found']:
                oxtr_result = r
            elif r['snp_id'] == 'rs6265' and r['found']:
                bdnf_result = r
            elif r['snp_id'] == 'rs25531' and r['found']:
                slc6a4_result = r
            elif r['snp_id'] == 'rs1360780' and r['found']:
                fkbp5_result = r
            elif r['snp_id'] == 'rs1800497' and r['found']:
                drd2_result = r
            elif r['snp_id'] == 'rs1799971' and r['found']:
                oprm1_result = r
            elif r['snp_id'] == 'rs16969968' and r['found']:
                chrna5_result = r
            elif r['snp_id'] == 'rs17070145' and r['found']:
                kibra_result = r

    # Determine COMT type (Warrior/Worrier)
    if comt_result:
        gt = comt_result['genotype']
        if gt == 'GG':
            profile['comt_type'] = 'warrior'
            profile['personality_traits'].append('Стрессоустойчивость')
            profile['personality_traits'].append('Импульсивность')
            profile['protective_factors'].append('Устойчивость к острому стрессу')
        elif gt == 'AA':
            profile['comt_type'] = 'worrier'
            profile['personality_traits'].append('Высокие когнитивные способности')
            profile['personality_traits'].append('Склонность к тревожности')
            profile['risk_factors'].append('Повышенная тревожность')
        else:
            profile['comt_type'] = 'balanced'
            profile['personality_traits'].append('Адаптивность')

    # Determine OXTR type
    if oxtr_result:
        gt = oxtr_result['genotype']
        if gt == 'GG':
            profile['oxtr_type'] = 'high_empathy'
            profile['personality_traits'].append('Высокая эмпатия')
            profile['protective_factors'].append('Сильные социальные связи')
        elif gt == 'AA':
            profile['oxtr_type'] = 'lower_empathy'
            profile['personality_traits'].append('Независимость')
        else:
            profile['oxtr_type'] = 'moderate_empathy'

    # Cognitive style from COMT
    if comt_result:
        gt = comt_result['genotype']
        if gt == 'AA':
            profile['cognitive_style'] = 'Стабильность и глубокое мышление'
        elif gt == 'GG':
            profile['cognitive_style'] = 'Гибкость и быстрое переключение'
        else:
            profile['cognitive_style'] = 'Баланс гибкости и стабильности'

    # Stress sensitivity
    stress_risk_score = 0
    if slc6a4_result and slc6a4_result['genotype'] == 'GG':
        stress_risk_score += 2
        profile['risk_factors'].append('Чувствительность к негативным событиям (5-HTTLPR S/S)')
    elif slc6a4_result and 'G' in slc6a4_result['genotype']:
        stress_risk_score += 1

    if fkbp5_result and fkbp5_result['genotype'] == 'TT':
        stress_risk_score += 2
        profile['risk_factors'].append('Повышенная реактивность стрессовой оси (FKBP5)')
    elif fkbp5_result and 'T' in fkbp5_result['genotype']:
        stress_risk_score += 1

    if bdnf_result and bdnf_result['genotype'] in ['TT', 'AA']:
        stress_risk_score += 1
        profile['risk_factors'].append('Сниженная нейропластичность (BDNF Met/Met)')

    if stress_risk_score >= 3:
        profile['stress_sensitivity'] = 'high'
    elif stress_risk_score <= 1:
        profile['stress_sensitivity'] = 'low'

    # Addiction risk
    addiction_score = 0
    if drd2_result and drd2_result['genotype'] == 'AA':
        addiction_score += 2
        profile['risk_factors'].append('Сниженные D2 рецепторы (DRD2 A1/A1)')
    elif drd2_result and 'A' in drd2_result['genotype']:
        addiction_score += 1

    if oprm1_result and oprm1_result['genotype'] == 'GG':
        addiction_score += 2
        profile['risk_factors'].append('Изменённая опиоидная система (OPRM1 G/G)')
    elif oprm1_result and 'G' in oprm1_result['genotype']:
        addiction_score += 1

    if chrna5_result and chrna5_result['genotype'] == 'AA':
        addiction_score += 2
        profile['risk_factors'].append('Повышенный риск никотиновой зависимости (CHRNA5)')
    elif chrna5_result and 'A' in chrna5_result['genotype']:
        addiction_score += 1

    if addiction_score >= 3:
        profile['addiction_risk'] = 'elevated'
    elif addiction_score <= 1:
        profile['addiction_risk'] = 'low'

    # Depression risk
    depression_score = 0
    if slc6a4_result and slc6a4_result['genotype'] == 'GG':
        depression_score += 2
    elif slc6a4_result and 'G' in slc6a4_result['genotype']:
        depression_score += 1

    if bdnf_result and bdnf_result['genotype'] in ['TT', 'AA']:
        depression_score += 2
    elif bdnf_result and bdnf_result['genotype'] in ['CT', 'AG']:
        depression_score += 1

    if comt_result and comt_result['genotype'] == 'AA':
        depression_score += 1

    if depression_score >= 4:
        profile['depression_risk'] = 'elevated'
    elif depression_score <= 1:
        profile['depression_risk'] = 'low'

    # Memory traits
    if kibra_result and kibra_result['genotype'] == 'TT':
        profile['protective_factors'].append('Хорошая эпизодическая память (KIBRA T/T)')

    return profile


def generate_report(results, profile):
    """Generate comprehensive psychology report"""
    report = []

    # Header
    report.append("# Психологический и поведенческий анализ генома")
    report.append(f"\nДата анализа: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("\n---\n")

    # Disclaimer
    report.append("## Важный дисклеймер")
    report.append(DISCLAIMER)
    report.append("\n---\n")

    # Profile Summary
    report.append("## Психологический профиль\n")

    # COMT Type
    if profile['comt_type']:
        comt_labels = {
            'warrior': 'Воин (Warrior) - Val/Val',
            'worrier': 'Мыслитель (Worrier) - Met/Met',
            'balanced': 'Сбалансированный - Val/Met'
        }
        report.append(f"### Тип по COMT: **{comt_labels.get(profile['comt_type'], profile['comt_type'])}**\n")

        if profile['comt_type'] == 'warrior':
            report.append("Характеристики типа 'Воин':")
            report.append("- Быстрое разрушение дофамина в префронтальной коре")
            report.append("- Хорошо работаете под давлением")
            report.append("- Более импульсивны в спокойной обстановке")
            report.append("- Быстрее восстанавливаетесь от стресса")
        elif profile['comt_type'] == 'worrier':
            report.append("Характеристики типа 'Мыслитель':")
            report.append("- Медленное разрушение дофамина - выше базовый уровень")
            report.append("- Лучше рабочая память и когнитивные функции")
            report.append("- Склонность к тревоге и руминации")
            report.append("- Хуже переносите острый стресс")
        else:
            report.append("Характеристики сбалансированного типа:")
            report.append("- Адаптивны к разным условиям")
            report.append("- Можете переключаться между режимами")
        report.append("")

    # OXTR Type
    if profile['oxtr_type']:
        oxtr_labels = {
            'high_empathy': 'Высокая эмпатия (GG)',
            'moderate_empathy': 'Умеренная эмпатия (AG)',
            'lower_empathy': 'Независимый тип (AA)'
        }
        report.append(f"### Социальный тип по OXTR: **{oxtr_labels.get(profile['oxtr_type'], profile['oxtr_type'])}**\n")

    # Cognitive Style
    if profile['cognitive_style']:
        report.append(f"### Когнитивный стиль: **{profile['cognitive_style']}**\n")

    # Risk levels
    report.append("### Уровни риска\n")

    stress_labels = {'high': 'Повышенный', 'moderate': 'Умеренный', 'low': 'Пониженный'}
    addiction_labels = {'elevated': 'Повышенный', 'average': 'Средний', 'low': 'Пониженный'}
    depression_labels = {'elevated': 'Повышенный', 'average': 'Средний', 'low': 'Пониженный'}

    stress_emoji = {'high': '🔴', 'moderate': '🟡', 'low': '🟢'}
    addiction_emoji = {'elevated': '🔴', 'average': '🟡', 'low': '🟢'}
    depression_emoji = {'elevated': '🔴', 'average': '🟡', 'low': '🟢'}

    report.append(f"| Параметр | Уровень |")
    report.append(f"|----------|---------|")
    report.append(f"| Чувствительность к стрессу | {stress_emoji[profile['stress_sensitivity']]} {stress_labels[profile['stress_sensitivity']]} |")
    report.append(f"| Риск зависимостей | {addiction_emoji[profile['addiction_risk']]} {addiction_labels[profile['addiction_risk']]} |")
    report.append(f"| Риск депрессии | {depression_emoji[profile['depression_risk']]} {depression_labels[profile['depression_risk']]} |")
    report.append("")

    # Personality traits
    if profile['personality_traits']:
        report.append("### Личностные черты (генетическая предрасположенность)\n")
        for trait in profile['personality_traits']:
            report.append(f"- {trait}")
        report.append("")

    # Risk factors
    if profile['risk_factors']:
        report.append("### Факторы риска\n")
        for factor in profile['risk_factors']:
            report.append(f"- ⚠️ {factor}")
        report.append("")

    # Protective factors
    if profile['protective_factors']:
        report.append("### Защитные факторы\n")
        for factor in profile['protective_factors']:
            report.append(f"- 🛡️ {factor}")
        report.append("")

    report.append("\n---\n")

    # Detailed Results by Category
    report.append("## Детальные результаты по категориям\n")

    for category, cat_results in results.items():
        cat_info = PSYCHOLOGY_SNPS[category]
        report.append(f"### {cat_info['name']}")
        report.append(f"*{cat_info['description']}*\n")

        report.append("| SNP | Ген | Генотип | Интерпретация |")
        report.append("|-----|-----|---------|---------------|")

        for r in cat_results:
            if r['found']:
                interp = r['interpretation'] or 'Данные не интерпретированы'
                report.append(f"| {r['snp_id']} | {r['gene']} | **{r['genotype']}** | {interp} |")
            else:
                report.append(f"| {r['snp_id']} | {r['gene']} | - | *Не найден в геноме* |")

        report.append("")

    report.append("\n---\n")

    # Coping Strategies
    report.append("## Рекомендуемые стратегии адаптации\n")

    # Add relevant strategies based on profile
    strategies_to_include = []

    if profile['comt_type']:
        strategies_to_include.append(profile['comt_type'])

    if profile['oxtr_type'] in ['high_empathy', 'lower_empathy']:
        strategies_to_include.append(profile['oxtr_type'])

    if profile['stress_sensitivity'] == 'high':
        strategies_to_include.append('stress_sensitive')

    if profile['addiction_risk'] == 'elevated':
        strategies_to_include.append('addiction_prone')

    if profile['depression_risk'] == 'elevated':
        strategies_to_include.append('depression_risk')

    for strategy_key in strategies_to_include:
        if strategy_key in COPING_STRATEGIES:
            strategy = COPING_STRATEGIES[strategy_key]
            report.append(f"### {strategy['title']}\n")

            if 'description' in strategy:
                report.append(f"*{strategy['description']}*\n")

            if 'strengths' in strategy:
                report.append("**Ваши сильные стороны:**")
                for s in strategy['strengths']:
                    report.append(f"- ✅ {s}")
                report.append("")

            if 'challenges' in strategy:
                report.append("**Возможные сложности:**")
                for c in strategy['challenges']:
                    report.append(f"- ⚠️ {c}")
                report.append("")

            report.append("**Рекомендуемые стратегии:**")
            for s in strategy['strategies']:
                report.append(f"- 💡 {s}")
            report.append("")

    report.append("\n---\n")

    # Statistics
    report.append("## Статистика анализа\n")

    total_snps = 0
    found_snps = 0
    for cat, cat_results in results.items():
        total_snps += len(cat_results)
        found_snps += sum(1 for r in cat_results if r['found'])

    report.append(f"- Всего проанализировано SNP: {total_snps}")
    report.append(f"- Найдено в геноме: {found_snps}")
    report.append(f"- Не найдено: {total_snps - found_snps}")

    report.append("\n---\n")

    # Final reminder
    report.append("## Заключение\n")
    report.append("**Помните:** Генетика определяет склонности, но не судьбу. ")
    report.append("Осознание своих генетических предрасположенностей - это инструмент ")
    report.append("для более эффективной работы над собой, а не приговор.\n")
    report.append("\nВсе рекомендации носят общий характер. Для персонализированной ")
    report.append("помощи обратитесь к квалифицированному психологу или психотерапевту.")

    return '\n'.join(report)


def main():
    print("=" * 60)
    print("ПСИХОЛОГИЧЕСКИЙ АНАЛИЗ ГЕНОМА")
    print("=" * 60)

    print("\n[1/4] Загрузка генома...")
    genome = load_genome()
    print(f"      Загружено {len(genome)} SNP")

    print("\n[2/4] Анализ психологических маркеров...")
    results = analyze_psychology(genome)

    for category, cat_results in results.items():
        cat_name = PSYCHOLOGY_SNPS[category]['name']
        found = sum(1 for r in cat_results if r['found'])
        print(f"      → {cat_name}: {found}/{len(cat_results)}")

    print("\n[3/4] Определение психологического профиля...")
    profile = determine_profile(results)

    # Print profile summary
    comt_labels = {'warrior': 'Воин', 'worrier': 'Мыслитель', 'balanced': 'Сбалансированный'}
    if profile['comt_type']:
        print(f"      COMT тип: {comt_labels.get(profile['comt_type'], profile['comt_type'])}")

    oxtr_labels = {'high_empathy': 'Высокая эмпатия', 'moderate_empathy': 'Умеренная', 'lower_empathy': 'Независимый'}
    if profile['oxtr_type']:
        print(f"      OXTR тип: {oxtr_labels.get(profile['oxtr_type'], profile['oxtr_type'])}")

    print(f"      Стрессочувствительность: {profile['stress_sensitivity']}")
    print(f"      Риск зависимостей: {profile['addiction_risk']}")
    print(f"      Риск депрессии: {profile['depression_risk']}")

    print("\n[4/4] Генерация отчёта...")
    report = generate_report(results, profile)

    # Ensure directory exists
    os.makedirs(f"{REPORTS_PATH}/psychology", exist_ok=True)

    report_path = f"{REPORTS_PATH}/psychology/report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"      → {report_path}")

    print("\n" + "=" * 60)
    print("АНАЛИЗ ЗАВЕРШЁН")
    print("=" * 60)

    # Print key findings
    print("\n🔑 КЛЮЧЕВЫЕ НАХОДКИ:\n")

    if profile['comt_type']:
        comt_desc = {
            'warrior': 'Warrior - устойчивы к стрессу, хорошо работаете под давлением',
            'worrier': 'Worrier - высокие когнитивные способности, но склонность к тревоге',
            'balanced': 'Сбалансированный - адаптивны к разным условиям'
        }
        print(f"  📊 Тип COMT: {comt_desc.get(profile['comt_type'], profile['comt_type'])}")

    if profile['risk_factors']:
        print("\n  ⚠️  Факторы риска:")
        for factor in profile['risk_factors']:
            print(f"      • {factor}")

    if profile['protective_factors']:
        print("\n  🛡️  Защитные факторы:")
        for factor in profile['protective_factors']:
            print(f"      • {factor}")

    print(f"\n  📄 Полный отчёт: {report_path}")
    print("\n  ℹ️  Помните: гены - это предрасположенность, а НЕ судьба!")


if __name__ == "__main__":
    main()
