#!/usr/bin/env python3
"""
Detoxification SNP Analysis Script
Analyzes detoxification-related genetic markers from 23andMe data
"""

import os
from collections import defaultdict
from datetime import datetime

# Paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
GENOME_FILE = f"{BASE_PATH}/data/genome_data.txt"
REPORTS_PATH = f"{BASE_PATH}/reports"

# =============================================================================
# SNP DATABASE - Organized by detoxification category
# =============================================================================

DETOX_SNPS = {
    "phase1_cyp450": {
        "name": "Фаза I детоксикации CYP450",
        "snps": {
            "rs762551": {
                "gene": "CYP1A2",
                "description": "Метаболизм кофеина",
                "risk_allele": "C",
                "interpretation": {
                    "AA": ("fast", "Быстрый метаболизатор кофеина - кофеин выводится быстро"),
                    "AC": ("intermediate", "Средний метаболизатор кофеина"),
                    "CA": ("intermediate", "Средний метаболизатор кофеина"),
                    "CC": ("slow", "Медленный метаболизатор кофеина - кофеин задерживается дольше"),
                }
            },
            "rs1056836": {
                "gene": "CYP1B1",
                "description": "Метаболизм эстрогенов",
                "risk_allele": "G",
                "interpretation": {
                    "GG": ("high", "Повышенное образование 4-OH эстрогенов (более канцерогенных)"),
                    "CG": ("moderate", "Умеренно повышенное образование 4-OH эстрогенов"),
                    "GC": ("moderate", "Умеренно повышенное образование 4-OH эстрогенов"),
                    "CC": ("normal", "Нормальный метаболизм эстрогенов (больше 2-OH)"),
                }
            },
            "rs1799853": {
                "gene": "CYP2C9*2",
                "description": "Метаболизм НПВС, варфарина",
                "risk_allele": "T",
                "interpretation": {
                    "TT": ("slow", "Медленный метаболизатор - снизить дозу НПВС/варфарина"),
                    "CT": ("intermediate", "Промежуточный метаболизатор"),
                    "TC": ("intermediate", "Промежуточный метаболизатор"),
                    "CC": ("normal", "Нормальный метаболизатор CYP2C9"),
                }
            },
            "rs1057910": {
                "gene": "CYP2C9*3",
                "description": "Метаболизм НПВС, варфарина",
                "risk_allele": "C",
                "interpretation": {
                    "CC": ("slow", "Медленный метаболизатор - значительно снизить дозу"),
                    "AC": ("intermediate", "Промежуточный метаболизатор"),
                    "CA": ("intermediate", "Промежуточный метаболизатор"),
                    "AA": ("normal", "Нормальный метаболизатор CYP2C9*3"),
                }
            },
            "rs4244285": {
                "gene": "CYP2C19*2",
                "description": "Метаболизм: клопидогрел, омепразол, антидепрессанты",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("slow", "Плохой метаболизатор - клопидогрел НЕ эффективен!"),
                    "AG": ("intermediate", "Промежуточный метаболизатор"),
                    "GA": ("intermediate", "Промежуточный метаболизатор"),
                    "GG": ("normal", "Нормальный метаболизатор CYP2C19"),
                }
            },
            "rs12248560": {
                "gene": "CYP2C19*17",
                "description": "Ультрабыстрый метаболизм",
                "risk_allele": "T",
                "interpretation": {
                    "TT": ("ultrafast", "Ультрабыстрый метаболизатор - может потребоваться увеличение дозы"),
                    "CT": ("fast", "Быстрый метаболизатор"),
                    "TC": ("fast", "Быстрый метаболизатор"),
                    "CC": ("normal", "Нормальный метаболизатор CYP2C19"),
                }
            },
        }
    },

    "phase2_conjugation": {
        "name": "Фаза II конъюгация",
        "snps": {
            "rs1695": {
                "gene": "GSTP1",
                "description": "Глутатион S-трансфераза - детоксикация через глутатион",
                "risk_allele": "G",
                "interpretation": {
                    "AA": ("normal", "Нормальная активность GSTP1 - эффективная детоксикация"),
                    "AG": ("moderate", "Немного сниженная активность GSTP1"),
                    "GA": ("moderate", "Немного сниженная активность GSTP1"),
                    "GG": ("low", "Сниженная активность GSTP1 - менее эффективная детоксикация"),
                }
            },
            "rs1801280": {
                "gene": "NAT2",
                "description": "N-ацетилтрансфераза 2 - ацетилирование",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("slow", "Медленный ацетилятор - повышен риск токсичности изониазида"),
                    "AG": ("intermediate", "Промежуточный ацетилятор"),
                    "GA": ("intermediate", "Промежуточный ацетилятор"),
                    "GG": ("fast", "Быстрый ацетилятор"),
                }
            },
            "rs1799930": {
                "gene": "NAT2",
                "description": "N-ацетилтрансфераза 2 - вторая мутация",
                "risk_allele": "A",
                "interpretation": {
                    "AA": ("slow", "Медленный ацетилятор"),
                    "AG": ("intermediate", "Промежуточный ацетилятор"),
                    "GA": ("intermediate", "Промежуточный ацетилятор"),
                    "GG": ("fast", "Быстрый ацетилятор"),
                }
            },
            "rs8175347": {
                "gene": "UGT1A1*28",
                "description": "Синдром Жильбера - конъюгация билирубина",
                "risk_allele": "TA7",
                "interpretation": {
                    "6/6": ("normal", "Нормальная активность UGT1A1"),
                    "6/7": ("moderate", "Носитель - умеренно сниженная конъюгация билирубина"),
                    "7/7": ("low", "Синдром Жильбера - желтуха при стрессе/голодании"),
                    "AA": ("normal", "Вероятно нормальная активность UGT1A1"),
                    "AT": ("moderate", "Вероятно носитель UGT1A1*28"),
                    "TA": ("moderate", "Вероятно носитель UGT1A1*28"),
                    "TT": ("low", "Вероятно синдром Жильбера"),
                }
            },
        }
    },

    "antioxidants": {
        "name": "Антиоксидантная защита",
        "snps": {
            "rs4880": {
                "gene": "SOD2 (MnSOD)",
                "description": "Супероксиддисмутаза - митохондриальная защита",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("high", "Высокая активность SOD2 - эффективная защита митохондрий"),
                    "CT": ("moderate", "Средняя активность SOD2"),
                    "TC": ("moderate", "Средняя активность SOD2"),
                    "TT": ("low", "Низкая активность SOD2 - нужны антиоксиданты"),
                    "AA": ("low", "Низкая активность SOD2 (Ala/Ala) - нужны антиоксиданты"),
                    "AG": ("moderate", "Средняя активность SOD2"),
                    "GA": ("moderate", "Средняя активность SOD2"),
                    "GG": ("high", "Высокая активность SOD2"),
                }
            },
            "rs1050450": {
                "gene": "GPX1",
                "description": "Глутатионпероксидаза - защита от перекисей",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("normal", "Нормальная активность GPX1"),
                    "CT": ("moderate", "Немного сниженная активность GPX1"),
                    "TC": ("moderate", "Немного сниженная активность GPX1"),
                    "TT": ("low", "Сниженная активность GPX1 - нужен селен"),
                }
            },
            "rs1001179": {
                "gene": "CAT",
                "description": "Каталаза - разложение перекиси водорода",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("normal", "Нормальная активность каталазы"),
                    "CT": ("moderate", "Немного сниженная активность каталазы"),
                    "TC": ("moderate", "Немного сниженная активность каталазы"),
                    "TT": ("low", "Сниженная активность каталазы"),
                }
            },
        }
    },

    "methylation": {
        "name": "Метилирование",
        "snps": {
            "rs1801133": {
                "gene": "MTHFR C677T",
                "description": "Метилентетрагидрофолатредуктаза - ключевой фермент",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("normal", "100% активность MTHFR - нормальное метилирование"),
                    "CT": ("moderate", "~65% активность MTHFR - немного снижено метилирование"),
                    "TC": ("moderate", "~65% активность MTHFR - немного снижено метилирование"),
                    "TT": ("low", "~30% активность MTHFR - значительно снижено метилирование"),
                    "AA": ("normal", "Нормальная активность MTHFR"),
                    "AG": ("moderate", "Гетерозигота C677T - умеренно сниженная активность (~65%)"),
                    "GA": ("moderate", "Гетерозигота C677T - умеренно сниженная активность (~65%)"),
                    "GG": ("normal", "Нормальная активность MTHFR"),
                }
            },
            "rs1801131": {
                "gene": "MTHFR A1298C",
                "description": "Вторая мутация MTHFR",
                "risk_allele": "C",
                "interpretation": {
                    "AA": ("normal", "Нормальная активность A1298C"),
                    "AC": ("low", "Незначительное снижение активности"),
                    "CA": ("low", "Незначительное снижение активности"),
                    "CC": ("moderate", "Сниженная активность MTHFR"),
                    "TT": ("normal", "Нормальная активность"),
                    "GT": ("normal", "Нормальная активность A1298C"),
                    "TG": ("normal", "Нормальная активность A1298C"),
                    "GG": ("moderate", "Сниженная активность A1298C"),
                }
            },
            "rs1805087": {
                "gene": "MTR (MS)",
                "description": "Метионин синтаза - B12-зависимое метилирование",
                "risk_allele": "G",
                "interpretation": {
                    "AA": ("normal", "Нормальная активность MTR"),
                    "AG": ("moderate", "Немного сниженная активность MTR - нужен B12"),
                    "GA": ("moderate", "Немного сниженная активность MTR - нужен B12"),
                    "GG": ("low", "Сниженная активность MTR - нужен B12"),
                }
            },
            "rs1801394": {
                "gene": "MTRR",
                "description": "Метионин синтаза редуктаза - регенерация B12",
                "risk_allele": "G",
                "interpretation": {
                    "AA": ("normal", "Нормальная активность MTRR"),
                    "AG": ("moderate", "Немного сниженная регенерация B12"),
                    "GA": ("moderate", "Немного сниженная регенерация B12"),
                    "GG": ("low", "Сниженная регенерация B12 - нужен метил-B12"),
                }
            },
        }
    },

    "heavy_metals": {
        "name": "Тяжёлые металлы",
        "snps": {
            "rs662": {
                "gene": "PON1 Q192R",
                "description": "Параоксоназа - детоксикация пестицидов и ртути",
                "risk_allele": "A",
                "interpretation": {
                    "GG": ("normal", "Нормальная активность PON1 - хорошая защита от пестицидов"),
                    "AG": ("moderate", "Умеренно сниженная активность PON1"),
                    "GA": ("moderate", "Умеренно сниженная активность PON1"),
                    "AA": ("low", "Сниженная активность PON1 - уязвимость к пестицидам/ртути"),
                }
            },
            "rs11191439": {
                "gene": "AS3MT",
                "description": "Арсенит метилтрансфераза - метаболизм мышьяка",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("normal", "Эффективное выведение мышьяка"),
                    "CT": ("moderate", "Умеренно сниженное выведение мышьяка"),
                    "TC": ("moderate", "Умеренно сниженное выведение мышьяка"),
                    "TT": ("low", "Сниженное выведение мышьяка - избегать экспозиции"),
                }
            },
        }
    },

    "transporters": {
        "name": "Транспортёры",
        "snps": {
            "rs1045642": {
                "gene": "ABCB1 (MDR1/P-гликопротеин)",
                "description": "Выведение токсинов и лекарств из клеток",
                "risk_allele": "T",
                "interpretation": {
                    "CC": ("high", "Высокая активность P-гликопротеина - быстрое выведение"),
                    "CT": ("normal", "Нормальная активность P-гликопротеина"),
                    "TC": ("normal", "Нормальная активность P-гликопротеина"),
                    "TT": ("low", "Сниженная активность P-гликопротеина - накопление токсинов"),
                }
            },
            "rs4149056": {
                "gene": "SLCO1B1",
                "description": "Транспорт статинов в печень",
                "risk_allele": "C",
                "interpretation": {
                    "TT": ("normal", "Нормальный транспорт статинов"),
                    "TC": ("moderate", "Повышен риск миопатии от статинов (~4x)"),
                    "CT": ("moderate", "Повышен риск миопатии от статинов (~4x)"),
                    "CC": ("high", "Высокий риск миопатии от статинов (~17x) - избегать высоких доз!"),
                }
            },
        }
    },

    "alcohol": {
        "name": "Алкоголь",
        "snps": {
            "rs1229984": {
                "gene": "ADH1B",
                "description": "Алкогольдегидрогеназа - окисление алкоголя",
                "risk_allele": "A",
                "interpretation": {
                    "GG": ("slow", "Медленное окисление алкоголя - дольше опьянение"),
                    "AG": ("fast", "Быстрое окисление алкоголя - быстрее отрезвление"),
                    "GA": ("fast", "Быстрое окисление алкоголя - быстрее отрезвление"),
                    "AA": ("fast", "Очень быстрое окисление алкоголя"),
                }
            },
            "rs671": {
                "gene": "ALDH2",
                "description": "Альдегиддегидрогеназа - расщепление ацетальдегида",
                "risk_allele": "A",
                "interpretation": {
                    "GG": ("normal", "Нормальная активность ALDH2 - хорошая переносимость алкоголя"),
                    "AG": ("low", "Сниженная активность ALDH2 - флашинг, тошнота от алкоголя"),
                    "GA": ("low", "Сниженная активность ALDH2 - флашинг, тошнота от алкоголя"),
                    "AA": ("very_low", "Отсутствие ALDH2 - сильный флашинг, непереносимость алкоголя"),
                }
            },
        }
    }
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


def determine_mthfr_status(results):
    """Determine combined MTHFR status from methylation results"""
    c677t = None
    a1298c = None

    for r in results:
        if r['snp_id'] == 'rs1801133':
            c677t = r['genotype']
        elif r['snp_id'] == 'rs1801131':
            a1298c = r['genotype']

    if not c677t or not a1298c:
        return None

    # Count risk alleles
    c677t_risk = c677t.count('T') if c677t else 0
    a1298c_risk = a1298c.count('C') + a1298c.count('G') if a1298c else 0

    # Check for homozygous risk
    is_c677t_homo = c677t in ['TT', 'AA']
    is_c677t_hetero = 'T' in c677t and 'C' in c677t or 'A' in c677t and 'G' in c677t
    is_a1298c_homo = a1298c in ['CC', 'GG']
    is_a1298c_hetero = len(set(a1298c)) == 2 if a1298c else False

    if c677t == 'AG':
        is_c677t_hetero = True
    if a1298c == 'GT':
        is_a1298c_hetero = False

    if is_c677t_homo and is_a1298c_homo:
        status = ('severe', 'Значительное снижение активности MTHFR (~10-20%)')
    elif is_c677t_homo and is_a1298c_hetero:
        status = ('severe', 'Значительное снижение активности MTHFR')
    elif is_c677t_homo:
        status = ('moderate', 'C677T гомозигота - сниженная активность MTHFR (~30%)')
    elif is_c677t_hetero and is_a1298c_homo:
        status = ('moderate', 'Компаунд - умеренное снижение активности')
    elif is_c677t_hetero and is_a1298c_hetero:
        status = ('moderate', 'Компаунд гетерозигота - умеренное снижение')
    elif is_c677t_hetero:
        status = ('mild', 'C677T гетерозигота - незначительное снижение (~65%)')
    elif is_a1298c_homo:
        status = ('mild', 'A1298C гомозигота - незначительное снижение')
    else:
        status = ('normal', 'Нормальная активность MTHFR')

    return {
        'c677t': c677t,
        'a1298c': a1298c,
        'status': status[0],
        'interpretation': status[1]
    }


def determine_nat2_status(results):
    """Determine NAT2 acetylator status"""
    rs1801280 = None
    rs1799930 = None

    for r in results:
        if r['snp_id'] == 'rs1801280':
            rs1801280 = r
        elif r['snp_id'] == 'rs1799930':
            rs1799930 = r

    if not rs1801280 or not rs1799930:
        return None

    slow_count = 0
    if rs1801280['risk_level'] == 'slow':
        slow_count += 2
    elif rs1801280['risk_level'] == 'intermediate':
        slow_count += 1

    if rs1799930['risk_level'] == 'slow':
        slow_count += 2
    elif rs1799930['risk_level'] == 'intermediate':
        slow_count += 1

    if slow_count >= 3:
        status = ('slow', 'Медленный ацетилятор - повышен риск токсичности изониазида, сульфаниламидов')
    elif slow_count >= 1:
        status = ('intermediate', 'Промежуточный ацетилятор')
    else:
        status = ('fast', 'Быстрый ацетилятор')

    return {
        'rs1801280': rs1801280['genotype'] if rs1801280['found'] else 'н/д',
        'rs1799930': rs1799930['genotype'] if rs1799930['found'] else 'н/д',
        'status': status[0],
        'interpretation': status[1]
    }


def determine_cyp2c19_status(results):
    """Determine CYP2C19 metabolizer status"""
    rs4244285 = None  # *2
    rs12248560 = None  # *17

    for r in results:
        if r['snp_id'] == 'rs4244285':
            rs4244285 = r
        elif r['snp_id'] == 'rs12248560':
            rs12248560 = r

    if not rs4244285 or not rs12248560:
        return None

    is_slow = rs4244285['risk_level'] == 'slow'
    is_intermediate_slow = rs4244285['risk_level'] == 'intermediate'
    is_ultrafast = rs12248560['risk_level'] == 'ultrafast'
    is_fast = rs12248560['risk_level'] == 'fast'

    if is_slow:
        status = ('poor', 'Плохой метаболизатор CYP2C19 - клопидогрел неэффективен!')
    elif is_intermediate_slow and is_ultrafast:
        status = ('normal', 'Нормальный метаболизатор (компенсация)')
    elif is_intermediate_slow:
        status = ('intermediate', 'Промежуточный метаболизатор CYP2C19')
    elif is_ultrafast:
        status = ('ultrarapid', 'Ультрабыстрый метаболизатор CYP2C19 - может потребоваться увеличение дозы')
    elif is_fast:
        status = ('rapid', 'Быстрый метаболизатор CYP2C19')
    else:
        status = ('normal', 'Нормальный метаболизатор CYP2C19')

    return {
        'rs4244285': rs4244285['genotype'] if rs4244285['found'] else 'н/д',
        'rs12248560': rs12248560['genotype'] if rs12248560['found'] else 'н/д',
        'status': status[0],
        'interpretation': status[1]
    }


def determine_alcohol_tolerance(results):
    """Determine alcohol tolerance based on ADH1B and ALDH2"""
    adh1b = None
    aldh2 = None

    for r in results:
        if r['snp_id'] == 'rs1229984':
            adh1b = r
        elif r['snp_id'] == 'rs671':
            aldh2 = r

    if not adh1b and not aldh2:
        return None

    adh_fast = adh1b and adh1b['risk_level'] in ['fast', 'ultrafast'] if adh1b else False
    aldh_low = aldh2 and aldh2['risk_level'] in ['low', 'very_low'] if aldh2 else False

    if aldh_low:
        status = ('intolerant', 'Непереносимость алкоголя - флашинг, тошнота')
    elif adh_fast and not aldh_low:
        status = ('sensitive', 'Быстрое опьянение, но хорошее расщепление ацетальдегида')
    elif not adh_fast and not aldh_low:
        status = ('normal', 'Стандартная переносимость алкоголя')
    else:
        status = ('unknown', 'Не удалось определить')

    return {
        'adh1b': adh1b['genotype'] if adh1b and adh1b['found'] else 'н/д',
        'aldh2': aldh2['genotype'] if aldh2 and aldh2['found'] else 'н/д',
        'status': status[0],
        'interpretation': status[1]
    }


def generate_category_report(category, results, genome):
    """Generate report for a category"""
    cat_info = DETOX_SNPS[category]

    report = []
    report.append(f"# {cat_info['name']}")
    report.append(f"\nДата анализа: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("\n## Результаты\n")

    # Statistics
    found = sum(1 for r in results if r['found'])
    report.append(f"Найдено маркеров: {found}/{len(results)}\n")

    # Risk summary
    risk_counts = defaultdict(int)
    for r in results:
        if r['risk_level']:
            risk_counts[r['risk_level']] += 1

    if risk_counts:
        report.append("### Сводка по статусам\n")
        status_emoji = {
            'high': '🔴',
            'very_high': '🔴🔴',
            'moderate': '🟡',
            'low': '🟠',
            'very_low': '🔴',
            'normal': '✅',
            'fast': '⚡',
            'slow': '🐢',
            'ultrafast': '⚡⚡',
            'intermediate': '🟡',
            'info': 'ℹ️'
        }
        for risk, count in sorted(risk_counts.items()):
            emoji = status_emoji.get(risk, '•')
            report.append(f"- {emoji} {risk}: {count}")

    report.append("\n### Детальные результаты\n")
    report.append("| SNP | Ген | Генотип | Статус | Интерпретация |")
    report.append("|-----|-----|---------|--------|---------------|")

    for r in results:
        if r['found']:
            risk_label = r['risk_level'] or 'н/д'
            interp = r['interpretation'] or 'Нет данных'
            report.append(f"| {r['snp_id']} | {r['gene']} | **{r['genotype']}** | {risk_label} | {interp} |")
        else:
            report.append(f"| {r['snp_id']} | {r['gene']} | - | - | Не найден в геноме |")

    # Special sections
    if category == 'methylation':
        mthfr = determine_mthfr_status(results)
        if mthfr:
            report.append("\n### MTHFR статус (комбинированный)\n")
            report.append(f"- C677T (rs1801133): {mthfr['c677t']}")
            report.append(f"- A1298C (rs1801131): {mthfr['a1298c']}")
            report.append(f"- **Статус: {mthfr['status']}**")
            report.append(f"- {mthfr['interpretation']}")

    if category == 'phase2_conjugation':
        nat2 = determine_nat2_status(results)
        if nat2:
            report.append("\n### NAT2 статус ацетилятора\n")
            report.append(f"- rs1801280: {nat2['rs1801280']}")
            report.append(f"- rs1799930: {nat2['rs1799930']}")
            report.append(f"- **Статус: {nat2['status']}**")
            report.append(f"- {nat2['interpretation']}")

    if category == 'phase1_cyp450':
        cyp2c19 = determine_cyp2c19_status(results)
        if cyp2c19:
            report.append("\n### CYP2C19 статус метаболизатора\n")
            report.append(f"- *2 (rs4244285): {cyp2c19['rs4244285']}")
            report.append(f"- *17 (rs12248560): {cyp2c19['rs12248560']}")
            report.append(f"- **Статус: {cyp2c19['status']}**")
            report.append(f"- {cyp2c19['interpretation']}")

    if category == 'alcohol':
        alcohol = determine_alcohol_tolerance(results)
        if alcohol:
            report.append("\n### Переносимость алкоголя\n")
            report.append(f"- ADH1B (rs1229984): {alcohol['adh1b']}")
            report.append(f"- ALDH2 (rs671): {alcohol['aldh2']}")
            report.append(f"- **Статус: {alcohol['status']}**")
            report.append(f"- {alcohol['interpretation']}")

    return '\n'.join(report)


def generate_summary_report(all_results, genome):
    """Generate overall summary report"""
    report = []
    report.append("# Сводный отчёт по детоксикации")
    report.append(f"\nДата анализа: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("\n---\n")

    report.append("## Важные предупреждения\n")
    report.append("1. **Это НЕ медицинский диагноз** - только информационный анализ")
    report.append("2. **Генетика - не приговор** - образ жизни и среда важнее")
    report.append("3. **Для медицинских решений** - консультация врача обязательна")
    report.append("4. **Дозировки лекарств** - определяет только врач\n")

    report.append("---\n")

    # Collect findings by status
    critical = []
    attention = []
    optimal = []

    for category, results in all_results.items():
        for r in results:
            if r['risk_level'] in ['slow', 'low', 'very_low', 'high']:
                critical.append((category, r))
            elif r['risk_level'] in ['moderate', 'intermediate']:
                attention.append((category, r))
            elif r['risk_level'] in ['normal', 'fast', 'high'] and r['risk_level'] == 'normal':
                optimal.append((category, r))

    if critical:
        report.append("## Требует внимания\n")
        report.append("| Категория | SNP | Ген | Генотип | Описание |")
        report.append("|-----------|-----|-----|---------|----------|")
        for cat, r in critical:
            cat_name = DETOX_SNPS[cat]['name']
            report.append(f"| {cat_name} | {r['snp_id']} | {r['gene']} | **{r['genotype']}** | {r['interpretation']} |")
        report.append("")

    if attention:
        report.append("## Умеренные отклонения\n")
        report.append("| Категория | SNP | Ген | Генотип | Описание |")
        report.append("|-----------|-----|-----|---------|----------|")
        for cat, r in attention:
            cat_name = DETOX_SNPS[cat]['name']
            report.append(f"| {cat_name} | {r['snp_id']} | {r['gene']} | **{r['genotype']}** | {r['interpretation']} |")
        report.append("")

    # Special analyses
    report.append("---\n")
    report.append("## Специальные анализы\n")

    # MTHFR
    methylation_results = all_results.get('methylation', [])
    mthfr = determine_mthfr_status(methylation_results)
    if mthfr:
        report.append("### MTHFR (Метилирование)\n")
        report.append(f"- C677T: {mthfr['c677t']}, A1298C: {mthfr['a1298c']}")
        report.append(f"- **Статус: {mthfr['status']}**")
        report.append(f"- {mthfr['interpretation']}")
        if mthfr['status'] in ['moderate', 'severe', 'mild']:
            report.append("- **Рекомендации:** метилфолат, метил-B12, избегать фолиевой кислоты\n")
        else:
            report.append("")

    # NAT2
    phase2_results = all_results.get('phase2_conjugation', [])
    nat2 = determine_nat2_status(phase2_results)
    if nat2:
        report.append("### NAT2 (Ацетилирование)\n")
        report.append(f"- **Статус: {nat2['status']}**")
        report.append(f"- {nat2['interpretation']}")
        if nat2['status'] == 'slow':
            report.append("- **Рекомендации:** осторожность с изониазидом, сульфаниламидами\n")
        else:
            report.append("")

    # CYP2C19
    phase1_results = all_results.get('phase1_cyp450', [])
    cyp2c19 = determine_cyp2c19_status(phase1_results)
    if cyp2c19:
        report.append("### CYP2C19 (Метаболизм лекарств)\n")
        report.append(f"- **Статус: {cyp2c19['status']}**")
        report.append(f"- {cyp2c19['interpretation']}")
        if cyp2c19['status'] == 'poor':
            report.append("- **ВАЖНО:** Клопидогрел неэффективен - требуется альтернатива!\n")
        else:
            report.append("")

    # Alcohol
    alcohol_results = all_results.get('alcohol', [])
    alcohol = determine_alcohol_tolerance(alcohol_results)
    if alcohol:
        report.append("### Алкоголь\n")
        report.append(f"- **Статус: {alcohol['status']}**")
        report.append(f"- {alcohol['interpretation']}\n")

    # SLCO1B1 Statin warning
    transporter_results = all_results.get('transporters', [])
    for r in transporter_results:
        if r['snp_id'] == 'rs4149056' and r['found']:
            if r['risk_level'] in ['moderate', 'high']:
                report.append("### SLCO1B1 (Статины)\n")
                report.append(f"- Генотип: {r['genotype']}")
                report.append(f"- **{r['interpretation']}**")
                if r['risk_level'] == 'high':
                    report.append("- **ВАЖНО:** Избегать высоких доз симвастатина, аторвастатина!\n")
                else:
                    report.append("")

    report.append("---\n")
    report.append("## Статистика анализа\n")

    total_snps = 0
    found_snps = 0
    for cat, results in all_results.items():
        total_snps += len(results)
        found_snps += sum(1 for r in results if r['found'])

    report.append(f"- Всего проанализировано SNP: {total_snps}")
    report.append(f"- Найдено в геноме: {found_snps}")
    report.append(f"- Не найдено: {total_snps - found_snps}")

    return '\n'.join(report)


def main():
    print("=" * 60)
    print("АНАЛИЗ ДЕТОКСИКАЦИИ ПО ГЕНОМУ 23andMe")
    print("=" * 60)

    print("\n[1/4] Загрузка генома...")
    genome = load_genome()
    print(f"      Загружено {len(genome)} SNP")

    print("\n[2/4] Анализ маркеров по категориям...")
    all_results = {}

    for category, cat_info in DETOX_SNPS.items():
        print(f"      -> {cat_info['name']}...")
        results = []
        for snp_id, snp_info in cat_info['snps'].items():
            result = analyze_snp(snp_id, snp_info, genome)
            results.append(result)
        all_results[category] = results

        # Count found
        found = sum(1 for r in results if r['found'])
        print(f"        Найдено: {found}/{len(results)}")

    print("\n[3/4] Генерация отчётов по категориям...")
    for category, results in all_results.items():
        report = generate_category_report(category, results, genome)
        report_dir = f"{REPORTS_PATH}/detox"
        os.makedirs(report_dir, exist_ok=True)
        report_path = f"{report_dir}/{category}.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"      -> {report_path}")

    print("\n[4/4] Генерация сводного отчёта...")
    summary = generate_summary_report(all_results, genome)
    summary_path = f"{REPORTS_PATH}/detox/report.md"
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"      -> {summary_path}")

    print("\n" + "=" * 60)
    print("АНАЛИЗ ЗАВЕРШЁН")
    print("=" * 60)

    # Print key findings to console
    print("\nКЛЮЧЕВЫЕ НАХОДКИ:\n")

    for category, results in all_results.items():
        important = [r for r in results if r['risk_level'] in ['slow', 'low', 'very_low', 'high']]
        if important:
            print(f"  {DETOX_SNPS[category]['name']}:")
            for r in important:
                print(f"    - {r['gene']} ({r['genotype']}): {r['interpretation']}")
            print()


if __name__ == "__main__":
    main()
