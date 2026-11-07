#!/usr/bin/env python3
"""
Nutrition & Metabolism Analysis Script
Analyzes nutrition-related genetic markers from 23andMe data
"""

import os
from datetime import datetime
from collections import defaultdict

# Paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
GENOME_FILE = f"{BASE_PATH}/data/genome_data.txt"
REPORTS_PATH = f"{BASE_PATH}/reports"

# =============================================================================
# SNP DATABASE - Nutrition markers
# =============================================================================

NUTRITION_SNPS = {
    "lactose": {
        "name": "Лактоза",
        "snps": {
            "rs4988235": {
                "gene": "LCT (MCM6)",
                "description": "Переносимость лактозы",
                "interpretation": {
                    "TT": ("tolerant", "Переносит лактозу (персистенция лактазы)"),
                    "CT": ("partial", "Частичная переносимость"),
                    "CC": ("intolerant", "Непереносимость лактозы"),
                    "AA": ("tolerant", "Переносит лактозу"),
                    "AG": ("partial", "Частичная переносимость"),
                    "GG": ("intolerant", "Непереносимость лактозы"),
                }
            },
        }
    },

    "gluten": {
        "name": "Глютен (целиакия)",
        "snps": {
            "rs2187668": {
                "gene": "HLA-DQ2.5",
                "description": "Риск целиакии",
                "interpretation": {
                    "TT": ("high_risk", "HLA-DQ2.5 - высокий генетический риск целиакии"),
                    "CT": ("moderate_risk", "Носитель HLA-DQ2.5 - умеренный риск"),
                    "CC": ("low_risk", "Низкий генетический риск целиакии"),
                }
            },
            "rs7454108": {
                "gene": "HLA-DQ8",
                "description": "Риск целиакии",
                "interpretation": {
                    "CC": ("moderate_risk", "HLA-DQ8 - умеренный риск целиакии"),
                    "CT": ("low_risk", "Носитель"),
                    "TT": ("low_risk", "Низкий риск"),
                }
            },
        }
    },

    "caffeine": {
        "name": "Кофеин",
        "snps": {
            "rs762551": {
                "gene": "CYP1A2",
                "description": "Метаболизм кофеина",
                "interpretation": {
                    "AA": ("fast", "Быстрый метаболизатор - кофеин безопасен до 400мг/день"),
                    "AC": ("medium", "Средний метаболизатор - умеренное потребление"),
                    "CC": ("slow", "Медленный метаболизатор - риск для сердца при >200мг/день"),
                }
            },
            "rs5751876": {
                "gene": "ADORA2A",
                "description": "Тревожность от кофеина",
                "interpretation": {
                    "TT": ("low_anxiety", "Меньше тревожности от кофеина"),
                    "CT": ("moderate_anxiety", "Умеренная чувствительность"),
                    "CC": ("high_anxiety", "Больше тревожности от кофеина"),
                }
            },
        }
    },

    "alcohol": {
        "name": "Алкоголь",
        "snps": {
            "rs671": {
                "gene": "ALDH2",
                "description": "Метаболизм алкоголя (азиатский румянец)",
                "interpretation": {
                    "GG": ("normal", "Нормальный метаболизм"),
                    "AG": ("flush", "Asian flush - непереносимость, риск рака при употреблении"),
                    "AA": ("severe", "Сильная непереносимость алкоголя"),
                }
            },
            "rs1229984": {
                "gene": "ADH1B",
                "description": "Скорость метаболизма этанола",
                "interpretation": {
                    "CC": ("slow", "Медленный метаболизм - выше риск алкоголизма"),
                    "CT": ("fast", "Быстрый метаболизм - защита от алкоголизма"),
                    "TT": ("fast", "Очень быстрый метаболизм - защита"),
                }
            },
        }
    },

    "vitamin_d": {
        "name": "Витамин D",
        "snps": {
            "rs2282679": {
                "gene": "GC (VDBP)",
                "description": "Уровень витамина D в крови",
                "interpretation": {
                    "CC": ("low", "Сниженный уровень витамина D - нужна добавка"),
                    "AC": ("moderate", "Умеренно снижен - контроль уровня"),
                    "GT": ("moderate", "Умеренно снижен"),
                    "AA": ("normal", "Нормальный уровень"),
                    "TT": ("normal", "Нормальный уровень"),
                    "GG": ("normal", "Нормальный уровень"),
                }
            },
            "rs7041": {
                "gene": "GC",
                "description": "Витамин D связывающий белок",
                "interpretation": {
                    "TT": ("low", "Gc1F - сниженный витамин D"),
                    "GT": ("moderate", "Умеренно снижен"),
                    "AC": ("moderate", "Умеренно снижен"),
                    "GG": ("normal", "Gc1S - нормальный уровень"),
                    "AA": ("normal", "Нормальный уровень"),
                    "CC": ("normal", "Нормальный"),
                }
            },
            "rs12785878": {
                "gene": "DHCR7",
                "description": "Синтез витамина D от солнца",
                "interpretation": {
                    "TT": ("low", "Меньше синтез от солнца"),
                    "GT": ("moderate", "Умеренно снижен синтез"),
                    "GG": ("normal", "Нормальный синтез"),
                }
            },
        }
    },

    "vitamin_b": {
        "name": "Витамины группы B",
        "snps": {
            "rs1801133": {
                "gene": "MTHFR C677T",
                "description": "Метаболизм фолатов (B9)",
                "interpretation": {
                    "TT": ("impaired", "Активность ~30% - нужен метилфолат"),
                    "CT": ("moderate", "Активность ~65% - метилфолат предпочтителен"),
                    "AG": ("moderate", "Активность ~65%"),
                    "CC": ("normal", "Нормальная активность - фолиевая кислота OK"),
                    "AA": ("normal", "Нормальная активность"),
                }
            },
            "rs1801131": {
                "gene": "MTHFR A1298C",
                "description": "Метаболизм фолатов",
                "interpretation": {
                    "CC": ("impaired", "Сниженная активность"),
                    "AC": ("moderate", "Немного снижена"),
                    "GT": ("normal", "Нормальная активность"),
                    "AA": ("normal", "Нормальная активность"),
                    "TT": ("normal", "Нормальная"),
                }
            },
            "rs602662": {
                "gene": "FUT2",
                "description": "Всасывание витамина B12",
                "interpretation": {
                    "AA": ("impaired", "Сниженное всасывание B12 - нужна добавка"),
                    "AG": ("moderate", "Умеренно снижено"),
                    "GG": ("normal", "Нормальное всасывание"),
                }
            },
        }
    },

    "vitamin_a": {
        "name": "Витамин A",
        "snps": {
            "rs12934922": {
                "gene": "BCMO1",
                "description": "Конверсия бета-каротина в витамин A",
                "interpretation": {
                    "TT": ("impaired", "Плохая конверсия - нужен готовый витамин A (ретинол)"),
                    "AT": ("moderate", "Умеренная конверсия"),
                    "AA": ("normal", "Хорошая конверсия бета-каротина"),
                }
            },
            "rs7501331": {
                "gene": "BCMO1",
                "description": "Конверсия бета-каротина",
                "interpretation": {
                    "TT": ("impaired", "Плохая конверсия"),
                    "CT": ("moderate", "Умеренная"),
                    "CC": ("normal", "Нормальная конверсия"),
                }
            },
        }
    },

    "omega3": {
        "name": "Омега-3 жирные кислоты",
        "snps": {
            "rs174546": {
                "gene": "FADS1",
                "description": "Конверсия ALA в EPA/DHA",
                "interpretation": {
                    "TT": ("impaired", "Плохая конверсия - нужны готовые EPA/DHA (рыба, добавки)"),
                    "CT": ("moderate", "Умеренная конверсия"),
                    "CC": ("normal", "Хорошая конверсия из растительных источников"),
                }
            },
            "rs174547": {
                "gene": "FADS1",
                "description": "Метаболизм омега-3",
                "interpretation": {
                    "TT": ("impaired", "Сниженная конверсия"),
                    "CT": ("moderate", "Умеренная"),
                    "CC": ("normal", "Хорошая конверсия"),
                }
            },
        }
    },

    "salt": {
        "name": "Соль и давление",
        "snps": {
            "rs4961": {
                "gene": "ADD1",
                "description": "Чувствительность к соли",
                "interpretation": {
                    "TT": ("sensitive", "Соль-чувствительная гипертония - ограничить соль"),
                    "GT": ("moderate", "Умеренная чувствительность"),
                    "GG": ("normal", "Нормальная чувствительность к соли"),
                }
            },
            "rs699": {
                "gene": "AGT",
                "description": "Ангиотензиноген",
                "interpretation": {
                    "CC": ("sensitive", "Повышенное давление от соли"),
                    "CT": ("moderate", "Умеренная чувствительность"),
                    "TT": ("normal", "Нормальная реакция на соль"),
                }
            },
        }
    },

    "taste": {
        "name": "Вкусовые особенности",
        "snps": {
            "rs713598": {
                "gene": "TAS2R38",
                "description": "Чувствительность к горечи",
                "interpretation": {
                    "GG": ("supertaster", "Супертастер - сильно чувствует горечь (брокколи, кофе)"),
                    "CG": ("medium", "Средняя чувствительность к горечи"),
                    "CC": ("non_taster", "Не чувствует горечь PROP/PTC"),
                }
            },
            "rs72921001": {
                "gene": "OR6A2",
                "description": "Восприятие кориандра",
                "interpretation": {
                    "AA": ("soap", "Кориандр пахнет мылом"),
                    "AC": ("mild", "Слабое восприятие мыльного вкуса"),
                    "CC": ("normal", "Нормальное восприятие кориандра"),
                }
            },
        }
    },

    "iron": {
        "name": "Железо",
        "snps": {
            "rs1800562": {
                "gene": "HFE C282Y",
                "description": "Гемохроматоз (накопление железа)",
                "interpretation": {
                    "AA": ("high_risk", "Гемохроматоз - избегать добавок железа!"),
                    "AG": ("carrier", "Носитель - контроль уровня ферритина"),
                    "GG": ("normal", "Нормальный метаболизм железа"),
                }
            },
            "rs855791": {
                "gene": "TMPRSS6",
                "description": "Уровень железа",
                "interpretation": {
                    "TT": ("low", "Склонность к низкому железу"),
                    "CT": ("moderate", "Умеренно снижен"),
                    "AG": ("moderate", "Умеренно снижен уровень"),
                    "CC": ("normal", "Нормальный уровень"),
                    "AA": ("normal", "Нормальный"),
                    "GG": ("normal", "Нормальный"),
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


def analyze_nutrition(genome):
    """Analyze nutrition markers"""
    results = {}

    for category, cat_info in NUTRITION_SNPS.items():
        cat_results = []
        for snp_id, snp_info in cat_info['snps'].items():
            result = {
                'snp_id': snp_id,
                'gene': snp_info['gene'],
                'description': snp_info['description'],
                'found': False,
                'genotype': None,
                'status': None,
                'interpretation': None
            }

            if snp_id in genome:
                result['found'] = True
                genotype = genome[snp_id]['genotype']
                result['genotype'] = genotype

                interp = snp_info.get('interpretation', {})
                for gt in [genotype, genotype[::-1] if len(genotype) == 2 else genotype]:
                    if gt in interp:
                        result['status'], result['interpretation'] = interp[gt]
                        break

            cat_results.append(result)
        results[category] = cat_results

    return results


def generate_report(results):
    """Generate nutrition report"""
    report = []
    report.append("# 🥗 Анализ питания и метаболизма")
    report.append(f"\nДата анализа: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("\n---\n")

    # Summary of key findings
    report.append("## 📋 Ключевые находки\n")

    recommendations = []
    warnings = []

    for category, cat_results in results.items():
        for r in cat_results:
            if r['status'] in ['impaired', 'intolerant', 'slow', 'low', 'sensitive', 'high_risk', 'flush', 'severe']:
                warnings.append(f"⚠️ **{r['gene']}**: {r['interpretation']}")
            elif r['status'] in ['tolerant', 'fast', 'normal', 'low_risk']:
                pass  # Normal findings

    if warnings:
        report.append("### Требуют внимания\n")
        for w in warnings:
            report.append(f"- {w}")
        report.append("")

    report.append("---\n")

    # Detailed results by category
    for category, cat_results in results.items():
        cat_name = NUTRITION_SNPS[category]['name']
        report.append(f"## {cat_name}\n")
        report.append("| SNP | Ген | Генотип | Статус | Интерпретация |")
        report.append("|-----|-----|---------|--------|---------------|")

        for r in cat_results:
            if r['found']:
                status_emoji = {
                    'normal': '✅',
                    'tolerant': '✅',
                    'fast': '✅',
                    'low_risk': '✅',
                    'moderate': '🟡',
                    'partial': '🟡',
                    'medium': '🟡',
                    'carrier': '🟡',
                    'impaired': '🔴',
                    'intolerant': '🔴',
                    'slow': '🔴',
                    'low': '🔴',
                    'sensitive': '🔴',
                    'high_risk': '🔴',
                    'flush': '🔴',
                    'severe': '🔴',
                    'supertaster': 'ℹ️',
                    'non_taster': 'ℹ️',
                    'soap': 'ℹ️',
                }.get(r['status'], '•')
                interp = r['interpretation'] or 'Нет данных'
                status = r['status'] or 'н/д'
                report.append(f"| {r['snp_id']} | {r['gene']} | **{r['genotype']}** | {status_emoji} {status} | {interp} |")
            else:
                report.append(f"| {r['snp_id']} | {r['gene']} | - | - | Не найден |")
        report.append("")

    # Recommendations section
    report.append("---\n")
    report.append("## 💡 Персонализированные рекомендации\n")

    # Generate recommendations based on findings
    rec_map = {
        'lactose': {
            'intolerant': "**Лактоза**: Избегайте молочных продуктов или используйте безлактозные альтернативы",
            'partial': "**Лактоза**: Умеренное потребление молочных продуктов, можно использовать лактазу"
        },
        'caffeine': {
            'slow': "**Кофеин**: Ограничьте до 1-2 чашек кофе в день, избегайте после обеда",
            'high_anxiety': "**Кофеин**: Если испытываете тревожность от кофе - снизьте потребление"
        },
        'vitamin_d': {
            'low': "**Витамин D**: Рекомендуется добавка 2000-4000 МЕ/день, особенно зимой",
            'moderate': "**Витамин D**: Контролируйте уровень 25(OH)D, возможно нужна добавка"
        },
        'vitamin_b': {
            'impaired': "**Фолаты**: Используйте метилфолат вместо фолиевой кислоты (400-800 мкг/день)"
        },
        'vitamin_a': {
            'impaired': "**Витамин A**: Получайте из животных источников (печень, яйца) или добавок ретинола"
        },
        'omega3': {
            'impaired': "**Омега-3**: Употребляйте жирную рыбу 2-3 раза в неделю или добавки EPA/DHA"
        },
        'iron': {
            'high_risk': "**Железо**: ИЗБЕГАЙТЕ добавок железа! Регулярно контролируйте ферритин",
            'low': "**Железо**: Возможна склонность к анемии - контролируйте гемоглобин и ферритин"
        },
        'salt': {
            'sensitive': "**Соль**: Ограничьте до 5г/день, избегайте переработанных продуктов"
        },
        'alcohol': {
            'flush': "**Алкоголь**: Рекомендуется полный отказ - повышен риск рака пищевода",
            'severe': "**Алкоголь**: Полный отказ от алкоголя"
        }
    }

    has_recommendations = False
    for category, cat_results in results.items():
        if category in rec_map:
            for r in cat_results:
                if r['status'] in rec_map[category]:
                    report.append(f"- {rec_map[category][r['status']]}")
                    has_recommendations = True

    if not has_recommendations:
        report.append("- Нет критических находок, придерживайтесь сбалансированного питания")

    report.append("\n---\n")
    report.append("## ⚠️ Важно\n")
    report.append("- Генетика — это предрасположенность, не диагноз")
    report.append("- Перед приёмом добавок проконсультируйтесь с врачом")
    report.append("- Для витамина D и железа рекомендуется сдать анализы крови")

    return '\n'.join(report)


def main():
    print("=" * 60)
    print("АНАЛИЗ ПИТАНИЯ И МЕТАБОЛИЗМА")
    print("=" * 60)

    print("\n[1/3] Загрузка генома...")
    genome = load_genome()
    print(f"      Загружено {len(genome)} SNP")

    print("\n[2/3] Анализ маркеров...")
    results = analyze_nutrition(genome)

    total = sum(len(r) for r in results.values())
    found = sum(sum(1 for x in r if x['found']) for r in results.values())
    print(f"      Найдено: {found}/{total} маркеров")

    print("\n[3/3] Генерация отчёта...")
    report = generate_report(results)

    report_path = f"{REPORTS_PATH}/nutrition/report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"      → {report_path}")

    print("\n" + "=" * 60)
    print("АНАЛИЗ ЗАВЕРШЁН")
    print("=" * 60)


if __name__ == "__main__":
    main()
