#!/usr/bin/env python3
"""
Carrier Status Analysis Script
Analyzes genetic carrier status for hereditary diseases from 23andMe data
Includes family planning implications and recommendations
"""

import os
from collections import defaultdict
from datetime import datetime

# Paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
GENOME_FILE = f"{BASE_PATH}/data/genome_data.txt"
REPORTS_PATH = f"{BASE_PATH}/reports"

# =============================================================================
# CARRIER STATUS SNP DATABASE
# Organized by disease category with carrier interpretations
# =============================================================================

CARRIER_SNPS = {
    "cystic_fibrosis": {
        "name": "Муковисцидоз (Cystic Fibrosis)",
        "inheritance": "Аутосомно-рецессивное",
        "frequency": "1/25 носителей среди европейцев",
        "snps": {
            "rs113993960": {
                "gene": "CFTR",
                "mutation": "F508del (p.Phe508del)",
                "description": "Наиболее частая мутация муковисцидоза (70% случаев)",
                "risk_allele": "del",
                "interpretation": {
                    "--": ("carrier", "Носитель F508del - делеция обнаружена"),
                    "CTT": ("normal", "Норма - нет делеции"),
                    "CT": ("carrier", "Возможный носитель (гетерозигота)"),
                    "II": ("normal", "Инсерция - норма"),
                    "DI": ("carrier", "Носитель делеции"),
                    "DD": ("affected", "Гомозигота по делеции - возможен муковисцидоз"),
                }
            },
            "rs121909005": {
                "gene": "CFTR",
                "mutation": "G542X (p.Gly542Ter)",
                "description": "Стоп-мутация, 2-3% случаев муковисцидоза",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("affected", "Гомозигота G542X - муковисцидоз"),
                    "AG": ("carrier", "Носитель G542X"),
                    "GA": ("carrier", "Носитель G542X"),
                    "GG": ("normal", "Норма - нет мутации G542X"),
                }
            },
        }
    },

    "sickle_cell": {
        "name": "Серповидноклеточная анемия (Sickle Cell)",
        "inheritance": "Аутосомно-рецессивное",
        "frequency": "1/12 носителей среди афроамериканцев, редко у европейцев",
        "snps": {
            "rs334": {
                "gene": "HBB",
                "mutation": "HbS (p.Glu6Val)",
                "description": "Мутация серповидноклеточной анемии",
                "risk_allele": "T",
                "interpretation": {
                    "AA": ("normal", "Норма - нормальный гемоглобин HbA"),
                    "AT": ("carrier", "Носитель HbS - серповидноклеточный признак (защита от малярии)"),
                    "TA": ("carrier", "Носитель HbS - серповидноклеточный признак (защита от малярии)"),
                    "TT": ("affected", "Серповидноклеточная анемия (HbSS) - требуется медицинское наблюдение"),
                }
            },
        }
    },

    "tay_sachs": {
        "name": "Болезнь Тея-Сакса (Tay-Sachs)",
        "inheritance": "Аутосомно-рецессивное",
        "frequency": "1/30 носителей среди ашкеназских евреев",
        "snps": {
            "rs80338939": {
                "gene": "HEXA",
                "mutation": "IVS12+1G>C / 1278insTATC",
                "description": "Мутация болезни Тея-Сакса",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("normal", "Норма - нет мутации"),
                    "CT": ("carrier", "Носитель мутации Тея-Сакса"),
                    "TC": ("carrier", "Носитель мутации Тея-Сакса"),
                    "TT": ("affected", "Гомозигота - болезнь Тея-Сакса"),
                    "GG": ("normal", "Норма"),
                    "AG": ("carrier", "Возможный носитель"),
                    "GA": ("carrier", "Возможный носитель"),
                    "AA": ("affected", "Возможна болезнь Тея-Сакса"),
                }
            },
        }
    },

    "gaucher": {
        "name": "Болезнь Гоше (Gaucher Disease)",
        "inheritance": "Аутосомно-рецессивное",
        "frequency": "1/15 носителей среди ашкеназских евреев",
        "snps": {
            "rs76763715": {
                "gene": "GBA",
                "mutation": "N370S (p.Asn409Ser)",
                "description": "Наиболее частая мутация болезни Гоше тип 1",
                "risk_allele": "A",
                "interpretation": {
                    "GG": ("normal", "Норма - нет мутации N370S"),
                    "AG": ("carrier", "Носитель N370S - болезнь Гоше тип 1"),
                    "GA": ("carrier", "Носитель N370S - болезнь Гоше тип 1"),
                    "AA": ("affected", "Гомозигота N370S - болезнь Гоше тип 1"),
                    "CC": ("normal", "Норма"),
                    "CT": ("carrier", "Возможный носитель"),
                    "TC": ("carrier", "Возможный носитель"),
                    "TT": ("affected", "Возможна болезнь Гоше"),
                }
            },
        }
    },

    "hearing_loss": {
        "name": "Наследственная глухота (GJB2)",
        "inheritance": "Аутосомно-рецессивное",
        "frequency": "1/30-50 носителей в общей популяции",
        "snps": {
            "rs80338939": {
                "gene": "GJB2",
                "mutation": "35delG (c.35delG)",
                "description": "Наиболее частая причина наследственной глухоты у европейцев",
                "risk_allele": "del",
                "interpretation": {
                    "--": ("carrier", "Носитель 35delG"),
                    "GG": ("normal", "Норма - нет делеции 35delG"),
                    "G-": ("carrier", "Носитель делеции 35delG"),
                    "-G": ("carrier", "Носитель делеции 35delG"),
                    "CC": ("normal", "Норма"),
                    "CT": ("carrier", "Возможный носитель"),
                    "TT": ("affected", "Возможна глухота"),
                }
            },
        }
    },

    "hemochromatosis": {
        "name": "Гемохроматоз (Hemochromatosis)",
        "inheritance": "Аутосомно-рецессивное с неполной пенетрантностью",
        "frequency": "1/8-10 носителей среди европейцев",
        "snps": {
            "rs1800562": {
                "gene": "HFE",
                "mutation": "C282Y (p.Cys282Tyr)",
                "description": "Главная мутация наследственного гемохроматоза",
                "risk_allele": "A",
                "interpretation": {
                    "GG": ("normal", "Норма - нет мутации C282Y"),
                    "AG": ("carrier", "Носитель C282Y - контроль ферритина рекомендован"),
                    "GA": ("carrier", "Носитель C282Y - контроль ферритина рекомендован"),
                    "AA": ("affected", "Гомозигота C282Y - высокий риск гемохроматоза, контроль железа обязателен"),
                }
            },
            "rs1799945": {
                "gene": "HFE",
                "mutation": "H63D (p.His63Asp)",
                "description": "Вторая по частоте мутация HFE (мягкий эффект)",
                "risk_allele": "G",
                "interpretation": {
                    "CC": ("normal", "Норма - нет мутации H63D"),
                    "CG": ("carrier", "Носитель H63D - обычно клинически незначим"),
                    "GC": ("carrier", "Носитель H63D - обычно клинически незначим"),
                    "GG": ("mild_risk", "Гомозигота H63D - небольшой риск накопления железа"),
                }
            },
        }
    },

    "alpha1_antitrypsin": {
        "name": "Дефицит альфа-1-антитрипсина (Alpha-1 Antitrypsin)",
        "inheritance": "Аутосомно-кодоминантное",
        "frequency": "1/25 носителей Z-аллеля среди европейцев",
        "snps": {
            "rs28929474": {
                "gene": "SERPINA1",
                "mutation": "Z (p.Glu342Lys)",
                "description": "Тяжелый дефицит - риск эмфиземы и цирроза",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("normal", "MM генотип - норма (100% активности A1AT)"),
                    "CT": ("carrier", "MZ генотип - носитель (~60% активности, избегать курения!)"),
                    "TC": ("carrier", "MZ генотип - носитель (~60% активности, избегать курения!)"),
                    "TT": ("affected", "ZZ генотип - тяжелый дефицит (~15% активности), риск эмфиземы/цирроза"),
                    "GG": ("normal", "Норма"),
                    "AG": ("carrier", "Носитель Z-аллеля"),
                    "GA": ("carrier", "Носитель Z-аллеля"),
                    "AA": ("affected", "ZZ генотип"),
                }
            },
            "rs17580": {
                "gene": "SERPINA1",
                "mutation": "S (p.Glu264Val)",
                "description": "Умеренный дефицит A1AT",
                "risk_allele": "T",
                "interpretation": {
                    "AA": ("normal", "Норма - нет S-аллеля"),
                    "AT": ("carrier", "MS генотип - носитель S (~80% активности)"),
                    "TA": ("carrier", "MS генотип - носитель S (~80% активности)"),
                    "TT": ("mild_risk", "SS генотип - умеренный дефицит (~60% активности)"),
                    "GG": ("normal", "Норма"),
                    "GT": ("carrier", "Носитель S-аллеля"),
                    "TG": ("carrier", "Носитель S-аллеля"),
                }
            },
        }
    },

    "phenylketonuria": {
        "name": "Фенилкетонурия (PKU)",
        "inheritance": "Аутосомно-рецессивное",
        "frequency": "1/50 носителей среди европейцев",
        "snps": {
            "rs5030858": {
                "gene": "PAH",
                "mutation": "R408W (p.Arg408Trp)",
                "description": "Частая мутация фенилкетонурии в Восточной Европе",
                "risk_allele": "A",
                "interpretation": {
                    "GG": ("normal", "Норма - нет мутации R408W"),
                    "AG": ("carrier", "Носитель R408W - PKU"),
                    "GA": ("carrier", "Носитель R408W - PKU"),
                    "AA": ("affected", "Гомозигота R408W - фенилкетонурия"),
                    "CC": ("normal", "Норма"),
                    "CT": ("carrier", "Носитель мутации PAH"),
                    "TC": ("carrier", "Носитель мутации PAH"),
                    "TT": ("affected", "Фенилкетонурия"),
                }
            },
        }
    },

    "brca_hereditary_cancer": {
        "name": "Наследственный рак (BRCA1/BRCA2)",
        "inheritance": "Аутосомно-доминантное (одной копии достаточно для риска)",
        "frequency": "1/40 среди ашкеназских евреев, 1/400-500 в общей популяции",
        "snps": {
            "rs80357906": {
                "gene": "BRCA1",
                "mutation": "185delAG (c.68_69delAG)",
                "description": "Основатель мутация BRCA1 - высокий риск рака груди/яичников",
                "risk_allele": "del",
                "interpretation": {
                    "--": ("high_risk", "Носитель 185delAG - высокий риск рака груди (до 80%) и яичников (до 40%)"),
                    "AG": ("normal", "Норма - нет мутации 185delAG"),
                    "GA": ("normal", "Норма"),
                    "AA": ("normal", "Норма"),
                    "GG": ("normal", "Норма"),
                    "A-": ("high_risk", "Носитель делеции BRCA1"),
                    "-A": ("high_risk", "Носитель делеции BRCA1"),
                    "G-": ("high_risk", "Носитель делеции BRCA1"),
                    "-G": ("high_risk", "Носитель делеции BRCA1"),
                    "II": ("normal", "Норма - инсерция"),
                    "DI": ("high_risk", "Носитель делеции"),
                    "ID": ("high_risk", "Носитель делеции"),
                    "DD": ("high_risk", "Гомозигота - требуется генетическое консультирование"),
                }
            },
            "rs80359550": {
                "gene": "BRCA2",
                "mutation": "6174delT (c.5946delT)",
                "description": "Основатель мутация BRCA2 - высокий риск рака груди",
                "risk_allele": "del",
                "interpretation": {
                    "--": ("high_risk", "Носитель 6174delT - высокий риск рака груди и простаты"),
                    "TT": ("normal", "Норма - нет делеции 6174delT"),
                    "T-": ("high_risk", "Носитель делеции BRCA2"),
                    "-T": ("high_risk", "Носитель делеции BRCA2"),
                    "AA": ("normal", "Норма"),
                    "CC": ("normal", "Норма"),
                    "GG": ("normal", "Норма"),
                    "II": ("normal", "Норма"),
                    "DI": ("high_risk", "Носитель делеции"),
                    "ID": ("high_risk", "Носитель делеции"),
                    "DD": ("high_risk", "Гомозигота по делеции"),
                }
            },
        }
    },
}

# Family planning notes for each condition
FAMILY_PLANNING_NOTES = {
    "cystic_fibrosis": """
    **Семейное планирование при носительстве муковисцидоза:**
    - Если оба партнера носители: 25% риск рождения ребенка с муковисцидозом
    - Рекомендуется тестирование партнера перед беременностью
    - Доступны ПГД (преимплантационная диагностика) и пренатальная диагностика
    - Заболевание серьезное, но лечение значительно улучшилось
    """,

    "sickle_cell": """
    **Семейное планирование при носительстве серповидноклеточной анемии:**
    - Носительство (AT) дает защиту от малярии без симптомов болезни
    - Если оба партнера носители: 25% риск серповидноклеточной анемии у ребенка
    - Тестирование партнера обязательно рекомендуется
    - Неонатальный скрининг выявляет болезнь при рождении
    """,

    "tay_sachs": """
    **Семейное планирование при носительстве болезни Тея-Сакса:**
    - Особенно важно для пар ашкеназского происхождения
    - Если оба носители: 25% риск болезни Тея-Сакса (летальная в детстве)
    - Обязательно тестирование партнера
    - ПГД позволяет предотвратить рождение больного ребенка
    """,

    "gaucher": """
    **Семейное планирование при носительстве болезни Гоше:**
    - Тип 1 (N370S) - наиболее мягкий, совместим с нормальной жизнью
    - Если оба носители: 25% риск болезни Гоше
    - Существует эффективная ферментозаместительная терапия
    - Тестирование партнера рекомендуется, особенно для ашкеназских евреев
    """,

    "hearing_loss": """
    **Семейное планирование при носительстве наследственной глухоты:**
    - Если оба партнера носители 35delG: 25% риск глухоты у ребенка
    - Тестирование партнера рекомендуется
    - Глухота не влияет на продолжительность жизни
    - Кохлеарные импланты эффективны при раннем выявлении
    """,

    "hemochromatosis": """
    **Семейное планирование при носительстве/наличии гемохроматоза:**
    - C282Y гомозиготы должны регулярно контролировать ферритин
    - Носители обычно не имеют клинических проявлений
    - Болезнь хорошо поддается лечению (флеботомия)
    - Низкий приоритет для ПГД, так как болезнь управляема
    """,

    "alpha1_antitrypsin": """
    **Семейное планирование при дефиците альфа-1-антитрипсина:**
    - MZ носители: избегать курения и профессиональных вредностей!
    - ZZ генотип: высокий риск эмфиземы, особенно при курении
    - Тестирование партнера рекомендуется
    - Болезнь проявляется во взрослом возрасте, есть терапия
    """,

    "phenylketonuria": """
    **Семейное планирование при носительстве фенилкетонурии:**
    - Если оба носители: 25% риск ФКУ у ребенка
    - Неонатальный скрининг обязателен во всех странах
    - При ранней диагностике и диете - нормальное развитие
    - Женщины с ФКУ должны соблюдать диету ДО и во время беременности
    """,

    "brca_hereditary_cancer": """
    **Семейное планирование при мутациях BRCA1/BRCA2:**
    - ВАЖНО: BRCA мутации доминантные - одной копии достаточно для риска
    - 50% риск передачи мутации каждому ребенку
    - Доступна ПГД для предотвращения передачи мутации
    - Необходимо генетическое консультирование
    - Для носителей: усиленный скрининг, профилактические опции
    """,
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


def analyze_carriers(genome):
    """Analyze carrier status for all conditions"""
    all_results = {}

    for condition_id, condition_info in CARRIER_SNPS.items():
        results = []

        for snp_id, snp_info in condition_info['snps'].items():
            result = {
                'snp_id': snp_id,
                'gene': snp_info['gene'],
                'mutation': snp_info['mutation'],
                'description': snp_info['description'],
                'risk_allele': snp_info['risk_allele'],
                'found': False,
                'genotype': None,
                'carrier_status': None,
                'interpretation': None
            }

            if snp_id in genome:
                result['found'] = True
                raw_genotype = genome[snp_id]['genotype']
                result['genotype'] = raw_genotype
                result['chromosome'] = genome[snp_id]['chromosome']
                result['position'] = genome[snp_id]['position']

                # Try to find interpretation
                interpretations = snp_info.get('interpretation', {})

                # Try original genotype
                if raw_genotype in interpretations:
                    result['carrier_status'], result['interpretation'] = interpretations[raw_genotype]
                else:
                    # Try normalized
                    normalized = normalize_genotype(raw_genotype)
                    if normalized in interpretations:
                        result['carrier_status'], result['interpretation'] = interpretations[normalized]
                    else:
                        # Try reversed
                        reversed_gt = raw_genotype[::-1] if len(raw_genotype) == 2 else raw_genotype
                        if reversed_gt in interpretations:
                            result['carrier_status'], result['interpretation'] = interpretations[reversed_gt]
                        else:
                            # Default interpretation based on risk allele presence
                            risk = snp_info['risk_allele']
                            if raw_genotype == '--' or 'del' in raw_genotype.lower():
                                result['carrier_status'] = 'possible_carrier'
                                result['interpretation'] = 'Делеция обнаружена - требуется подтверждение'
                            elif risk in raw_genotype:
                                risk_count = raw_genotype.count(risk)
                                if risk_count == 2:
                                    result['carrier_status'] = 'affected'
                                    result['interpretation'] = f'Гомозигота по риск-аллелю {risk}'
                                else:
                                    result['carrier_status'] = 'carrier'
                                    result['interpretation'] = f'Гетерозигота - носитель аллеля {risk}'
                            else:
                                result['carrier_status'] = 'normal'
                                result['interpretation'] = 'Риск-аллель не обнаружен'

            results.append(result)

        all_results[condition_id] = {
            'info': condition_info,
            'results': results
        }

    return all_results


def get_status_emoji(status):
    """Get emoji for carrier status"""
    status_map = {
        'normal': '[ OK ]',
        'carrier': '[CARR]',
        'affected': '[!!!!]',
        'high_risk': '[!!!!]',
        'mild_risk': '[MILD]',
        'possible_carrier': '[ ?? ]',
    }
    return status_map.get(status, '[----]')


def get_status_icon_md(status):
    """Get markdown status indicator"""
    status_map = {
        'normal': 'Normal',
        'carrier': 'CARRIER',
        'affected': 'AFFECTED',
        'high_risk': 'HIGH RISK',
        'mild_risk': 'Mild Risk',
        'possible_carrier': 'Possible Carrier',
    }
    return status_map.get(status, 'Unknown')


def generate_report(results):
    """Generate comprehensive carrier status report with family planning notes"""
    report = []

    report.append("# Carrier Status Analysis Report")
    report.append("# Otchyot o statuse nositelya geneticheskikh zabolevaniy")
    report.append("")
    report.append(f"**Data analiza:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("")
    report.append("---")
    report.append("")

    # Important warnings
    report.append("## VAZHNYE PREDUPREZHDENIYA")
    report.append("")
    report.append("1. **Eto NE medicinskiy diagnoz** - tolko informacionnyy analiz")
    report.append("2. **Nositelstvo =/= bolezn** - nositeli obychno zdorovy")
    report.append("3. **Dlya recessivnykh bolezney** - risk dlya rebenka tolko esli OBA roditelya nositeli")
    report.append("4. **BRCA mutacii - DOMINANTNYE** - odna kopiya sozdaet risk raka")
    report.append("5. **23andMe testiruet ogranichennyy nabor mutaciy** - otricatelnyy rezultat ne garantiruet otsutstviya nositelstva")
    report.append("6. **Dlya semeynogo planirovaniya** - konsultaciya genetika OBYAZATELNA")
    report.append("")
    report.append("---")
    report.append("")

    # Summary section
    report.append("## SVODKA PO NOSITELSTVU")
    report.append("")

    carriers_found = []
    affected_found = []
    high_risk_found = []
    normal_count = 0
    not_found_count = 0

    for condition_id, data in results.items():
        for r in data['results']:
            if not r['found']:
                not_found_count += 1
            elif r['carrier_status'] == 'carrier':
                carriers_found.append((condition_id, r))
            elif r['carrier_status'] == 'affected':
                affected_found.append((condition_id, r))
            elif r['carrier_status'] == 'high_risk':
                high_risk_found.append((condition_id, r))
            elif r['carrier_status'] in ['normal', 'mild_risk']:
                normal_count += 1

    # Alert section for significant findings
    if affected_found or high_risk_found:
        report.append("### !!! KRITICHESKIYE NAKHODKI !!!")
        report.append("")
        for condition_id, r in affected_found + high_risk_found:
            condition_name = results[condition_id]['info']['name']
            report.append(f"- **{condition_name}**: {r['gene']} {r['mutation']}")
            report.append(f"  - Genotip: **{r['genotype']}**")
            report.append(f"  - Status: **{get_status_icon_md(r['carrier_status'])}**")
            report.append(f"  - {r['interpretation']}")
            report.append("")
        report.append("**NEOBKHODIMA KONSULTACIYA GENETIKA!**")
        report.append("")

    if carriers_found:
        report.append("### Obnaruzheno nositelstvo")
        report.append("")
        for condition_id, r in carriers_found:
            condition_name = results[condition_id]['info']['name']
            report.append(f"- **{condition_name}**: {r['gene']} {r['mutation']}")
            report.append(f"  - Genotip: **{r['genotype']}**")
            report.append(f"  - {r['interpretation']}")
        report.append("")

    # Statistics
    report.append("### Statistika")
    report.append("")
    report.append(f"- Vsego proanalizirovano zabolevaniy: {len(results)}")
    report.append(f"- Normalnykh rezultatov: {normal_count}")
    report.append(f"- Nositelstvo obnaruzheno: {len(carriers_found)}")
    report.append(f"- Povyshennyy risk/bolezn: {len(affected_found) + len(high_risk_found)}")
    report.append(f"- SNP ne naydeno v genome: {not_found_count}")
    report.append("")
    report.append("---")
    report.append("")

    # Detailed results by condition
    report.append("## PODROBNYE REZULTATY PO ZABOLEVANIYAM")
    report.append("")

    for condition_id, data in results.items():
        info = data['info']
        condition_results = data['results']

        report.append(f"### {info['name']}")
        report.append("")
        report.append(f"- **Tip nasledovaniya:** {info['inheritance']}")
        report.append(f"- **Chastota nositelstva:** {info['frequency']}")
        report.append("")

        report.append("| SNP | Gen | Mutaciya | Genotip | Status | Interpretaciya |")
        report.append("|-----|-----|----------|---------|--------|----------------|")

        for r in condition_results:
            if r['found']:
                status = get_status_icon_md(r['carrier_status'])
                report.append(f"| {r['snp_id']} | {r['gene']} | {r['mutation']} | **{r['genotype']}** | {status} | {r['interpretation']} |")
            else:
                report.append(f"| {r['snp_id']} | {r['gene']} | {r['mutation']} | - | - | Ne nayden v genome |")

        report.append("")

        # Add family planning notes if carrier or affected
        has_findings = any(r['carrier_status'] in ['carrier', 'affected', 'high_risk']
                         for r in condition_results if r['found'])

        if has_findings and condition_id in FAMILY_PLANNING_NOTES:
            report.append("#### Semeynoye planirovaniye")
            # Convert notes to Latin transliteration
            notes = FAMILY_PLANNING_NOTES[condition_id]
            report.append(notes.replace("**", "**"))
            report.append("")

        report.append("---")
        report.append("")

    # General family planning section
    report.append("## OBSHCHIYE REKOMENDACII PO SEMEYNOMU PLANIROVANIYU")
    report.append("")
    report.append("### Esli vy nositel recessivnogo zabolevaniya:")
    report.append("")
    report.append("1. **Testirovanie partnera** - samyy vazhnyy shag")
    report.append("   - Esli partner NE nositel - risk dlya detey minimalen")
    report.append("   - Esli partner tozhe nositel - 25% risk u kazhdogo rebenka")
    report.append("")
    report.append("2. **Dostupnye opcii pri dvoinom nositelstve:**")
    report.append("   - PGD (preimplantacionnaya diagnostika) pri EKO")
    report.append("   - Prenatalnaya diagnostika (CVS, amniocentez)")
    report.append("   - Donorskiye gamety")
    report.append("   - Usynovlenie")
    report.append("")
    report.append("3. **Geneticheskoye konsultirovaniye:**")
    report.append("   - Rekomenduetsya vsem nositelyam")
    report.append("   - Obyazatelno pri planirovanii beremennosti")
    report.append("   - Pomozhyet poniat realnye riski i opcii")
    report.append("")

    report.append("### Esli u vas BRCA mutaciya:")
    report.append("")
    report.append("1. **BRCA - dominantnaya mutaciya:**")
    report.append("   - 50% risk peredachi kazhdomu rebenku")
    report.append("   - Odna kopiya dostatochna dlya povyshennogo riska raka")
    report.append("")
    report.append("2. **Rekomendacii dlya nositeley:**")
    report.append("   - Usilenniy skrining (MRI, mammografiya)")
    report.append("   - Obsuzhdenie profilakticheskikh operaciy")
    report.append("   - Geneticheskoye konsultirovaniye semi")
    report.append("")
    report.append("3. **Opcii dlya semeynogo planirovaniya:**")
    report.append("   - PGD pozvolyayet vybrat embriony bez mutacii")
    report.append("   - Testirovanie detey vozmozhno vo vzroslom vozraste")
    report.append("")

    report.append("---")
    report.append("")
    report.append("## OGRANICHYENIYA ANALIZA")
    report.append("")
    report.append("1. **23andMe testiruyet tolko opredelenniye mutacii:**")
    report.append("   - Ne vse mutacii dannogo gena")
    report.append("   - Otricatelnyy rezultat ne garantiruyet otsutstviya nositelstva")
    report.append("")
    report.append("2. **Dlya polnogo analiza nositelstva:**")
    report.append("   - Rekomenduetsya rasshirennyy panel nositelya (100+ zabolevaniy)")
    report.append("   - Klinicheskiye laboratorii (Invitae, Natera, GeneDx)")
    report.append("")
    report.append("3. **Etot otchyot:**")
    report.append("   - Tolko dlya informacionykh celey")
    report.append("   - Ne zamenyayet klinicheskoye testirovaniye")
    report.append("   - Trebuyet interpretatcii genetikom")
    report.append("")

    report.append("---")
    report.append("")
    report.append("*Otchyot sgenirirovan avtomaticheski*")
    report.append(f"*Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

    return '\n'.join(report)


def main():
    print("=" * 60)
    print("CARRIER STATUS ANALYSIS")
    print("Analiz nositelstva geneticheskikh zabolevaniy")
    print("=" * 60)

    print("\n[1/3] Zagruzka genoma...")
    genome = load_genome()
    print(f"      Zagruzheno {len(genome)} SNP")

    print("\n[2/3] Analiz nositelstva...")
    results = analyze_carriers(genome)

    # Print summary to console
    print("\n" + "-" * 60)
    print("REZULTATY ANALIZA:")
    print("-" * 60)

    for condition_id, data in results.items():
        info = data['info']
        condition_results = data['results']

        print(f"\n{info['name']}:")

        for r in condition_results:
            if r['found']:
                status = get_status_emoji(r['carrier_status'])
                print(f"  {status} {r['snp_id']} ({r['gene']}): {r['genotype']}")
                print(f"           {r['interpretation']}")
            else:
                print(f"  [----] {r['snp_id']} ({r['gene']}): Ne nayden")

    print("\n[3/3] Generaciya otchyota...")

    # Ensure directory exists
    report_dir = f"{REPORTS_PATH}/carrier_status"
    os.makedirs(report_dir, exist_ok=True)

    report = generate_report(results)
    report_path = f"{report_dir}/report.md"

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"      -> {report_path}")

    print("\n" + "=" * 60)
    print("ANALIZ ZAVERSHEN")
    print("=" * 60)

    # Print key findings
    carriers = []
    affected = []

    for condition_id, data in results.items():
        for r in data['results']:
            if r['found']:
                if r['carrier_status'] == 'carrier':
                    carriers.append((data['info']['name'], r))
                elif r['carrier_status'] in ['affected', 'high_risk']:
                    affected.append((data['info']['name'], r))

    if affected:
        print("\n!!! KRITICHESKIYE NAKHODKI !!!\n")
        for name, r in affected:
            print(f"  {name}: {r['gene']} {r['genotype']}")
            print(f"  -> {r['interpretation']}")
            print()

    if carriers:
        print("\nOBNARUZHENO NOSITELSTVO:\n")
        for name, r in carriers:
            print(f"  {name}: {r['gene']} {r['genotype']}")
            print(f"  -> {r['interpretation']}")
            print()

    if not carriers and not affected:
        print("\nNi odnogo nositelstva ne obnaruzheno po proverennymi SNP.")
        print("VNIMANIE: 23andMe proveryaet ogranichenniy nabor mutaciy.")


if __name__ == "__main__":
    main()
