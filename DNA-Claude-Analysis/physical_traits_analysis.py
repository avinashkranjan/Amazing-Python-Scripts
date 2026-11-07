#!/usr/bin/env python3
"""
Physical Traits Analysis Script
Analyzes physical traits markers from 23andMe data
"""

import os
from datetime import datetime
from collections import defaultdict

# Paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
GENOME_FILE = f"{BASE_PATH}/data/genome_data.txt"
REPORTS_PATH = f"{BASE_PATH}/reports"

# =============================================================================
# SNP DATABASE - Physical traits markers
# =============================================================================

PHYSICAL_SNPS = {
    "eye_color": {
        "name": "Цвет глаз",
        "snps": {
            "rs12913832": {
                "gene": "HERC2",
                "description": "Главный детерминант цвета глаз",
                "interpretation": {
                    "GG": ("blue", "Голубые/серые глаза (основной генотип)"),
                    "AG": ("mixed", "Зелёные или светло-карие глаза"),
                    "AA": ("brown", "Карие глаза"),
                }
            },
            "rs1800407": {
                "gene": "OCA2",
                "description": "Модификатор цвета глаз",
                "interpretation": {
                    "GG": ("standard", "Стандартный вариант"),
                    "AG": ("modifier", "Может осветлять карий цвет"),
                    "AA": ("green_modifier", "Часто связан с зелёными глазами"),
                    "CT": ("modifier", "Может модифицировать цвет"),
                    "TT": ("green_modifier", "Часто связан с зелёными глазами"),
                }
            },
            "rs12896399": {
                "gene": "SLC24A4",
                "description": "Модификатор цвета глаз",
                "interpretation": {
                    "GG": ("darker", "Склонность к более тёмному цвету"),
                    "GT": ("intermediate", "Промежуточный эффект"),
                    "TT": ("lighter", "Склонность к более светлому цвету"),
                }
            },
            "rs16891982": {
                "gene": "SLC45A2",
                "description": "Пигментация глаз и кожи",
                "interpretation": {
                    "GG": ("dark", "Тёмная пигментация (типично для африканцев/азиатов)"),
                    "CG": ("mixed", "Смешанная пигментация"),
                    "CC": ("light", "Светлая пигментация (типично для европейцев)"),
                }
            },
            "rs1393350": {
                "gene": "TYR",
                "description": "Тирозиназа - пигментация",
                "interpretation": {
                    "GG": ("standard", "Стандартный вариант"),
                    "AG": ("lighter", "Немного светлее пигментация"),
                    "AA": ("lighter", "Склонность к более светлым глазам"),
                }
            },
        }
    },

    "hair_color": {
        "name": "Цвет волос",
        "snps": {
            "rs12913832": {
                "gene": "HERC2",
                "description": "Влияет на цвет волос",
                "interpretation": {
                    "GG": ("light", "Склонность к светлым волосам"),
                    "AG": ("mixed", "Средний цвет волос"),
                    "AA": ("dark", "Склонность к тёмным волосам"),
                }
            },
            "rs1805007": {
                "gene": "MC1R R151C",
                "description": "Рыжие волосы (вариант 1)",
                "interpretation": {
                    "CC": ("normal", "Нет влияния на рыжий цвет"),
                    "CT": ("carrier", "Носитель рыжего - может быть рыжеватый оттенок"),
                    "TT": ("red", "Высокая вероятность рыжих волос"),
                }
            },
            "rs1805008": {
                "gene": "MC1R R160W",
                "description": "Рыжие волосы (вариант 2)",
                "interpretation": {
                    "CC": ("normal", "Нет влияния на рыжий цвет"),
                    "CT": ("carrier", "Носитель рыжего"),
                    "TT": ("red", "Высокая вероятность рыжих волос"),
                }
            },
            "rs1805009": {
                "gene": "MC1R D294H",
                "description": "Рыжие волосы (вариант 3)",
                "interpretation": {
                    "GG": ("normal", "Нет влияния на рыжий цвет"),
                    "CG": ("carrier", "Носитель рыжего"),
                    "CC": ("red", "Высокая вероятность рыжих волос"),
                }
            },
            "rs12821256": {
                "gene": "KITLG",
                "description": "Блондинизм",
                "interpretation": {
                    "TT": ("dark", "Тёмные волосы"),
                    "CT": ("light_carrier", "Может осветлять цвет волос"),
                    "CC": ("blonde", "Склонность к светлым/блондинистым волосам"),
                }
            },
        }
    },

    "hair_structure": {
        "name": "Структура волос",
        "snps": {
            "rs11803731": {
                "gene": "TCHH",
                "description": "Кудрявость волос",
                "interpretation": {
                    "AA": ("straight", "Прямые волосы"),
                    "AT": ("wavy", "Волнистые волосы"),
                    "TT": ("curly", "Кудрявые волосы"),
                }
            },
            "rs3827760": {
                "gene": "EDAR",
                "description": "Толщина волос (азиатский вариант)",
                "interpretation": {
                    "AA": ("thin", "Тонкие волосы (европейский вариант)"),
                    "AG": ("intermediate", "Средняя толщина"),
                    "GG": ("thick", "Толстые, жёсткие волосы (азиатский вариант)"),
                    "CC": ("thin", "Тонкие волосы"),
                    "CT": ("intermediate", "Средняя толщина"),
                    "TT": ("thick", "Толстые волосы"),
                }
            },
        }
    },

    "baldness": {
        "name": "Облысение (мужское)",
        "snps": {
            "rs2180439": {
                "gene": "HDAC9",
                "description": "Андрогенная алопеция",
                "interpretation": {
                    "CC": ("high_risk", "Повышенный риск раннего облысения"),
                    "CT": ("moderate_risk", "Умеренный риск облысения"),
                    "TT": ("low_risk", "Низкий риск раннего облысения"),
                }
            },
            "rs6625163": {
                "gene": "AR",
                "description": "Андрогенная алопеция (X-хромосома)",
                "interpretation": {
                    "AA": ("high_risk", "Повышенный риск облысения"),
                    "AC": ("moderate_risk", "Умеренный риск"),
                    "CC": ("low_risk", "Низкий риск облысения"),
                }
            },
        }
    },

    "skin": {
        "name": "Пигментация кожи",
        "snps": {
            "rs1426654": {
                "gene": "SLC24A5",
                "description": "Главный ген светлой кожи у европейцев",
                "interpretation": {
                    "AA": ("light", "Светлая кожа (европейский вариант)"),
                    "AG": ("intermediate", "Промежуточная пигментация"),
                    "GG": ("dark", "Тёмная кожа (африканский/азиатский вариант)"),
                }
            },
            "rs16891982": {
                "gene": "SLC45A2",
                "description": "Пигментация кожи",
                "interpretation": {
                    "GG": ("dark", "Тёмная пигментация"),
                    "CG": ("intermediate", "Промежуточная"),
                    "CC": ("light", "Светлая кожа"),
                }
            },
        }
    },

    "freckles": {
        "name": "Веснушки",
        "snps": {
            "rs1805007": {
                "gene": "MC1R",
                "description": "Веснушки и чувствительность к солнцу",
                "interpretation": {
                    "CC": ("no_freckles", "Меньше веснушек, лучше загар"),
                    "CT": ("some_freckles", "Склонность к веснушкам, осторожно на солнце"),
                    "TT": ("many_freckles", "Много веснушек, высокая чувствительность к солнцу"),
                }
            },
        }
    },

    "earwax": {
        "name": "Тип ушной серы",
        "snps": {
            "rs17822931": {
                "gene": "ABCC11",
                "description": "Тип ушной серы и запах тела",
                "interpretation": {
                    "CC": ("dry", "Сухая ушная сера (азиатский тип), меньше запаха тела"),
                    "CT": ("intermediate", "Промежуточный тип"),
                    "TT": ("wet", "Влажная ушная сера (европейский тип), обычный запах тела"),
                }
            },
        }
    },

    "light_sneeze": {
        "name": "Световой чихательный рефлекс (ACHOO)",
        "snps": {
            "rs10427255": {
                "gene": "Около ZEB2",
                "description": "Чихание от яркого света",
                "interpretation": {
                    "CC": ("no_achoo", "Нет светового рефлекса"),
                    "CT": ("mild_achoo", "Слабый световой рефлекс"),
                    "TT": ("achoo", "Чихание при взгляде на яркий свет"),
                }
            },
        }
    },

    "taste": {
        "name": "Вкусовое восприятие",
        "snps": {
            "rs713598": {
                "gene": "TAS2R38",
                "description": "Чувствительность к горечи (PROP/PTC)",
                "interpretation": {
                    "GG": ("supertaster", "Супертастер - сильно чувствует горечь (брокколи, кофе)"),
                    "CG": ("medium", "Средняя чувствительность к горечи"),
                    "CC": ("non_taster", "Не чувствует горечь PROP/PTC"),
                }
            },
            "rs72921001": {
                "gene": "OR6A2",
                "description": "Восприятие кориандра (кинзы)",
                "interpretation": {
                    "AA": ("soap", "Кориандр пахнет мылом"),
                    "AC": ("mild_soap", "Слабое восприятие мыльного вкуса"),
                    "CC": ("normal", "Нормальное восприятие кориандра - травяной аромат"),
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


def analyze_traits(genome):
    """Analyze physical traits markers"""
    results = {}

    for category, cat_info in PHYSICAL_SNPS.items():
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
                # Try original, reversed, and sorted genotypes
                for gt in [genotype, genotype[::-1] if len(genotype) == 2 else genotype]:
                    if gt in interp:
                        result['status'], result['interpretation'] = interp[gt]
                        break

            cat_results.append(result)
        results[category] = cat_results

    return results


def predict_eye_color(results):
    """
    IrisPlex-like eye color prediction based on multiple SNPs
    Uses rs12913832 (HERC2) as main predictor with modifications from other SNPs
    """
    eye_results = {r['snp_id']: r for r in results.get('eye_color', [])}

    # Main predictor: rs12913832 (HERC2)
    herc2 = eye_results.get('rs12913832', {})
    herc2_gt = herc2.get('genotype', '')

    # Base prediction from HERC2
    if herc2_gt == 'GG':
        blue_prob = 0.85
        green_prob = 0.10
        brown_prob = 0.05
    elif herc2_gt in ['AG', 'GA']:
        blue_prob = 0.25
        green_prob = 0.35
        brown_prob = 0.40
    elif herc2_gt == 'AA':
        blue_prob = 0.02
        green_prob = 0.15
        brown_prob = 0.83
    else:
        return None

    # Modify with OCA2 rs1800407
    oca2 = eye_results.get('rs1800407', {})
    oca2_gt = oca2.get('genotype', '')
    if oca2_gt in ['AA', 'TT']:
        green_prob += 0.15
        brown_prob -= 0.10
        blue_prob -= 0.05
    elif oca2_gt in ['AG', 'CT']:
        green_prob += 0.05

    # Modify with SLC24A4 rs12896399
    slc24a4 = eye_results.get('rs12896399', {})
    slc24a4_gt = slc24a4.get('genotype', '')
    if slc24a4_gt == 'TT':
        blue_prob += 0.05
        brown_prob -= 0.05
    elif slc24a4_gt == 'GG':
        brown_prob += 0.05
        blue_prob -= 0.05

    # Modify with SLC45A2 rs16891982
    slc45a2 = eye_results.get('rs16891982', {})
    slc45a2_gt = slc45a2.get('genotype', '')
    if slc45a2_gt == 'CC':
        blue_prob += 0.05
        green_prob += 0.02
    elif slc45a2_gt == 'GG':
        brown_prob += 0.15
        blue_prob -= 0.10

    # Normalize probabilities
    total = blue_prob + green_prob + brown_prob
    blue_prob = max(0, min(1, blue_prob / total))
    green_prob = max(0, min(1, green_prob / total))
    brown_prob = max(0, min(1, brown_prob / total))

    # Determine most likely color
    if blue_prob >= green_prob and blue_prob >= brown_prob:
        prediction = "Голубые/серые"
    elif green_prob >= blue_prob and green_prob >= brown_prob:
        prediction = "Зелёные"
    else:
        prediction = "Карие"

    return {
        'prediction': prediction,
        'blue_probability': round(blue_prob * 100, 1),
        'green_probability': round(green_prob * 100, 1),
        'brown_probability': round(brown_prob * 100, 1),
    }


def predict_hair_color(results):
    """
    Predict hair color based on MC1R variants and other genes
    Checks for red hair (MC1R) and blonde tendency (KITLG)
    """
    hair_results = {r['snp_id']: r for r in results.get('hair_color', [])}

    # Count MC1R red hair variants
    mc1r_variants = ['rs1805007', 'rs1805008', 'rs1805009']
    red_alleles = 0
    carrier_alleles = 0

    for snp_id in mc1r_variants:
        snp = hair_results.get(snp_id, {})
        status = snp.get('status', '')
        if status == 'red':
            red_alleles += 2
        elif status == 'carrier':
            carrier_alleles += 1

    # Check HERC2 for light/dark
    herc2 = hair_results.get('rs12913832', {})
    herc2_status = herc2.get('status', '')

    # Check KITLG for blonde
    kitlg = hair_results.get('rs12821256', {})
    kitlg_status = kitlg.get('status', '')

    # Determine prediction
    is_red = red_alleles >= 2 or (carrier_alleles >= 2)
    red_carrier = carrier_alleles >= 1

    if is_red:
        prediction = "Рыжие волосы"
        confidence = "высокая" if red_alleles >= 2 else "умеренная"
    elif kitlg_status == 'blonde' and herc2_status == 'light':
        prediction = "Светлые/блонд волосы"
        confidence = "высокая"
    elif kitlg_status in ['blonde', 'light_carrier'] or herc2_status == 'light':
        prediction = "Светлые волосы"
        confidence = "умеренная"
    elif herc2_status == 'dark':
        prediction = "Тёмные волосы"
        confidence = "высокая"
    else:
        prediction = "Средний цвет волос"
        confidence = "низкая"

    return {
        'prediction': prediction,
        'confidence': confidence,
        'red_carrier': red_carrier,
        'red_alleles': red_alleles + carrier_alleles,
        'mc1r_note': "Носитель MC1R - возможен рыжеватый оттенок у детей" if red_carrier else None
    }


def generate_report(results):
    """Generate physical traits markdown report"""
    report = []
    report.append("# Анализ физических признаков")
    report.append(f"\nДата анализа: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("\n---\n")

    # Predictions section
    report.append("## Предсказания\n")

    # Eye color prediction
    eye_pred = predict_eye_color(results)
    if eye_pred:
        report.append("### Цвет глаз (IrisPlex-подобный анализ)\n")
        report.append(f"**Предсказание: {eye_pred['prediction']}**\n")
        report.append("| Цвет | Вероятность |")
        report.append("|------|-------------|")
        report.append(f"| Голубые/серые | {eye_pred['blue_probability']}% |")
        report.append(f"| Зелёные | {eye_pred['green_probability']}% |")
        report.append(f"| Карие | {eye_pred['brown_probability']}% |")
        report.append("")

    # Hair color prediction
    hair_pred = predict_hair_color(results)
    if hair_pred:
        report.append("### Цвет волос\n")
        report.append(f"**Предсказание: {hair_pred['prediction']}** (уверенность: {hair_pred['confidence']})\n")
        if hair_pred['red_carrier']:
            report.append(f"- MC1R аллели: {hair_pred['red_alleles']}")
            report.append(f"- {hair_pred['mc1r_note']}")
        report.append("")

    report.append("---\n")

    # Key physical traits summary
    report.append("## Ключевые особенности\n")

    trait_highlights = []

    # Hair structure
    for r in results.get('hair_structure', []):
        if r['found'] and r['status']:
            if r['snp_id'] == 'rs11803731':
                trait_highlights.append(f"**Волосы**: {r['interpretation']}")
            elif r['snp_id'] == 'rs3827760':
                trait_highlights.append(f"**Толщина волос**: {r['interpretation']}")

    # Baldness risk
    for r in results.get('baldness', []):
        if r['found'] and r['status'] == 'high_risk':
            trait_highlights.append(f"**Облысение**: {r['interpretation']}")

    # Skin
    for r in results.get('skin', []):
        if r['found'] and r['snp_id'] == 'rs1426654':
            trait_highlights.append(f"**Кожа**: {r['interpretation']}")

    # Freckles
    for r in results.get('freckles', []):
        if r['found'] and r['status'] in ['some_freckles', 'many_freckles']:
            trait_highlights.append(f"**Веснушки**: {r['interpretation']}")

    # Earwax
    for r in results.get('earwax', []):
        if r['found']:
            trait_highlights.append(f"**Ушная сера**: {r['interpretation']}")

    # Light sneeze
    for r in results.get('light_sneeze', []):
        if r['found'] and r['status'] in ['mild_achoo', 'achoo']:
            trait_highlights.append(f"**ACHOO синдром**: {r['interpretation']}")

    # Taste
    for r in results.get('taste', []):
        if r['found']:
            if r['snp_id'] == 'rs713598':
                trait_highlights.append(f"**Горечь**: {r['interpretation']}")
            elif r['snp_id'] == 'rs72921001' and r['status'] in ['soap', 'mild_soap']:
                trait_highlights.append(f"**Кориандр**: {r['interpretation']}")

    if trait_highlights:
        for h in trait_highlights:
            report.append(f"- {h}")
    else:
        report.append("- Нет особых находок")

    report.append("\n---\n")

    # Detailed results by category
    report.append("## Детальные результаты по категориям\n")

    for category, cat_results in results.items():
        cat_name = PHYSICAL_SNPS[category]['name']
        report.append(f"### {cat_name}\n")
        report.append("| SNP | Ген | Генотип | Статус | Интерпретация |")
        report.append("|-----|-----|---------|--------|---------------|")

        for r in cat_results:
            if r['found']:
                status_emoji = {
                    # Eye/hair color
                    'blue': '&#128309;',
                    'green': '&#128994;',
                    'brown': '&#129424;',
                    'light': '&#11036;',
                    'dark': '&#11035;',
                    'mixed': '&#128993;',
                    # Hair
                    'straight': '|',
                    'wavy': '~',
                    'curly': '@',
                    'red': '&#128308;',
                    'blonde': '&#128993;',
                    'carrier': '(c)',
                    # Risk
                    'high_risk': '&#128308;',
                    'moderate_risk': '&#128993;',
                    'low_risk': '&#128994;',
                    # Other
                    'normal': '&#9989;',
                    'standard': '&#9989;',
                    'dry': '&#128167;',
                    'wet': '&#128166;',
                    'achoo': '&#129319;',
                    'supertaster': '&#128293;',
                    'non_taster': '-',
                    'soap': '&#129532;',
                }.get(r['status'], '')

                interp = r['interpretation'] or 'Нет данных'
                status = r['status'] or 'н/д'
                report.append(f"| {r['snp_id']} | {r['gene']} | **{r['genotype']}** | {status_emoji} {status} | {interp} |")
            else:
                report.append(f"| {r['snp_id']} | {r['gene']} | - | - | Не найден |")
        report.append("")

    report.append("---\n")

    # Statistics
    report.append("## Статистика анализа\n")
    total = sum(len(r) for r in results.values())
    found = sum(sum(1 for x in r if x['found']) for r in results.values())
    report.append(f"- Всего проанализировано SNP: {total}")
    report.append(f"- Найдено в геноме: {found}")
    report.append(f"- Не найдено: {total - found}")

    report.append("\n---\n")
    report.append("## Примечания\n")
    report.append("- Физические признаки определяются множеством генов и факторов среды")
    report.append("- Предсказания носят вероятностный характер")
    report.append("- Цвет глаз и волос может меняться с возрастом")
    report.append("- MC1R варианты также связаны с повышенной чувствительностью к солнцу")

    return '\n'.join(report)


def main():
    print("=" * 60)
    print("АНАЛИЗ ФИЗИЧЕСКИХ ПРИЗНАКОВ")
    print("=" * 60)

    print("\n[1/4] Загрузка генома...")
    genome = load_genome()
    print(f"      Загружено {len(genome)} SNP")

    print("\n[2/4] Анализ маркеров...")
    results = analyze_traits(genome)

    total = sum(len(r) for r in results.values())
    found = sum(sum(1 for x in r if x['found']) for r in results.values())
    print(f"      Найдено: {found}/{total} маркеров")

    print("\n[3/4] Предсказания...")

    # Eye color prediction
    eye_pred = predict_eye_color(results)
    if eye_pred:
        print(f"      Глаза: {eye_pred['prediction']} "
              f"(голубые {eye_pred['blue_probability']}%, "
              f"зелёные {eye_pred['green_probability']}%, "
              f"карие {eye_pred['brown_probability']}%)")

    # Hair color prediction
    hair_pred = predict_hair_color(results)
    if hair_pred:
        print(f"      Волосы: {hair_pred['prediction']} ({hair_pred['confidence']})")

    print("\n[4/4] Генерация отчёта...")
    report = generate_report(results)

    report_path = f"{REPORTS_PATH}/physical_traits/report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"      -> {report_path}")

    print("\n" + "=" * 60)
    print("АНАЛИЗ ЗАВЕРШЁН")
    print("=" * 60)

    # Print key findings to console
    print("\nКЛЮЧЕВЫЕ НАХОДКИ:\n")

    for category, cat_results in results.items():
        cat_name = PHYSICAL_SNPS[category]['name']
        found_items = [r for r in cat_results if r['found'] and r['interpretation']]
        if found_items:
            print(f"{cat_name}:")
            for r in found_items:
                print(f"    {r['gene']} ({r['genotype']}): {r['interpretation']}")
            print()


if __name__ == "__main__":
    main()
