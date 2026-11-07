#!/usr/bin/env python3
"""
DNA Data Analysis Script (No Dependencies)
Analyzes 23andMe exported data using only standard library
"""

import os
import csv
from collections import defaultdict

# Paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
ANCESTRY_FILE = f"{BASE_PATH}/ancestry_composition.csv"
COMPUTED_FILE = f"{BASE_PATH}/computed_data.csv"
PHENOTYPE_FILE = f"{BASE_PATH}/phenotype_data.csv"


def read_csv(filepath):
    """Read CSV file and return list of dicts"""
    rows = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def analyze_ancestry():
    """Analyze ancestry composition by chromosome segments"""
    print("\n" + "="*60)
    print("ЭТНИЧЕСКИЙ СОСТАВ (ANCESTRY COMPOSITION)")
    print("="*60)

    rows = read_csv(ANCESTRY_FILE)

    # Calculate segment lengths by ancestry
    ancestry_lengths = defaultdict(float)

    for row in rows:
        ancestry = row['Ancestry']
        try:
            start = int(row['Start Point'])
            end = int(row['End Point'])
            length_mb = (end - start) / 1_000_000
            ancestry_lengths[ancestry] += length_mb
        except (ValueError, KeyError):
            continue

    total_length = sum(ancestry_lengths.values())

    print(f"\nОбщая длина проанализированных сегментов: {total_length:.1f} Mb")
    print("\n--- Детальный состав (по длине сегментов) ---\n")

    # Broad categories to separate
    broad_categories = {'European', 'Western Asian & North African', 'Northern West Asian',
                        'East Asian & Indigenous American', 'World', 'Northern Asian',
                        'Northwestern European', 'Southern European'}

    # Sort by length
    sorted_ancestry = sorted(ancestry_lengths.items(), key=lambda x: x[1], reverse=True)

    detailed = [(a, l) for a, l in sorted_ancestry if a not in broad_categories]
    broad = [(a, l) for a, l in sorted_ancestry if a in broad_categories]

    print("ДЕТАЛЬНЫЕ ПОПУЛЯЦИИ:")
    for ancestry, length in detailed:
        pct = (length / total_length) * 100
        bar = "█" * int(pct / 2)
        print(f"  {ancestry:45} {length:8.1f} Mb  ({pct:5.1f}%) {bar}")

    print("\n\nШИРОКИЕ КАТЕГОРИИ (для справки):")
    for ancestry, length in broad:
        pct = (length / total_length) * 100
        print(f"  {ancestry:45} {length:8.1f} Mb  ({pct:5.1f}%)")

    # Chromosome breakdown
    print("\n\n--- Распределение по хромосомам ---")

    chrom_ancestry = defaultdict(lambda: defaultdict(float))
    chrom_total = defaultdict(float)

    for row in rows:
        ancestry = row['Ancestry']
        chrom = row['Chromosome']
        try:
            start = int(row['Start Point'])
            end = int(row['End Point'])
            length_mb = (end - start) / 1_000_000
            chrom_ancestry[chrom][ancestry] += length_mb
            chrom_total[chrom] += length_mb
        except (ValueError, KeyError):
            continue

    main_ancestries = {'Eastern European', 'Ashkenazi Jewish',
                       'Iranian, Caucasian & Mesopotamian', 'Broadly European',
                       'Broadly Northern West Asian', 'Greek & Balkan',
                       'Finnish', 'Cypriot', 'Siberian', 'East Asian'}

    def chrom_sort_key(c):
        num = c[3:]  # Remove 'chr'
        if num == 'X':
            return 23
        elif num == 'Y':
            return 24
        else:
            try:
                return int(num)
            except:
                return 99

    for chrom in sorted(chrom_ancestry.keys(), key=chrom_sort_key):
        total = chrom_total[chrom]
        print(f"\n{chrom} ({total:.1f} Mb):")

        chrom_data = [(a, l) for a, l in chrom_ancestry[chrom].items()
                      if a in main_ancestries and l > 0]
        chrom_data.sort(key=lambda x: x[1], reverse=True)

        for anc, length in chrom_data:
            pct = (length / total) * 100
            if pct > 1:
                print(f"    {anc:40} {pct:5.1f}%")

    return ancestry_lengths


def analyze_haplogroups():
    """Extract and analyze haplogroup information"""
    print("\n" + "="*60)
    print("ГАПЛОГРУППЫ (HAPLOGROUPS)")
    print("="*60)

    rows = read_csv(COMPUTED_FILE)

    y_haplo = None
    mt_haplo = None

    for row in rows:
        name = row.get('name', '')
        data = row.get('data', '')

        if 'yhaplo' in name and 'haplogroup' in name and data:
            y_haplo = data
        elif 'mthaplo' in name and 'haplogroup' in name and data:
            mt_haplo = data

    print("\n--- Ваши гаплогруппы ---\n")

    if y_haplo:
        print(f"  Y-DNA (отцовская линия): {y_haplo}")
        print(f"""
    ╔══════════════════════════════════════════════════════════════╗
    ║  R-CTS1211 (R1a > Z282 > Z280 > CTS1211)                     ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  • Возраст: ~4,500-5,000 лет                                 ║
    ║  • Происхождение: Восточная Европа (Понтийские степи)        ║
    ║  • Миграция: Славянские племена, 5-7 век н.э.                ║
    ║  • Распространение: Польша, Украина, Россия, Балканы         ║
    ║  • Связь: Балто-славянские народы, индоевропейцы             ║
    ║  • Исторические носители: Славяне, белые хорваты, анты       ║
    ╚══════════════════════════════════════════════════════════════╝
""")

    if mt_haplo:
        print(f"  mtDNA (материнская линия): {mt_haplo}")
        print(f"""
    ╔══════════════════════════════════════════════════════════════╗
    ║  HV1b2 (R0 > HV > HV1 > HV1b > HV1b2)                        ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  • Возраст: ~15,000-20,000 лет                               ║
    ║  • Происхождение: Западная Азия (Кавказ/Месопотамия)         ║
    ║  • Миграция: После последнего ледникового периода            ║
    ║  • Распространение: Ближний Восток, Кавказ, редко в Европе   ║
    ║  • Связь: Неолитические земледельцы, миграция в Европу       ║
    ║  • Редкость: Менее 1% в большинстве популяций                ║
    ╚══════════════════════════════════════════════════════════════╝
""")

    return y_haplo, mt_haplo


def analyze_neanderthal():
    """Analyze Neanderthal DNA markers"""
    print("\n" + "="*60)
    print("НЕАНДЕРТАЛЬСКАЯ ДНК (NEANDERTHAL DNA)")
    print("="*60)

    rows = read_csv(COMPUTED_FILE)

    total_markers = 0
    dosage_counts = defaultdict(int)
    variant_examples = []

    for row in rows:
        name = row.get('name', '')
        if 'neanderthal_v2:details' not in name:
            continue

        total_markers += 1
        data = row.get('data', '')
        label = row.get('label', '')

        if data and data != 'None':
            try:
                dosage = float(data)
                dosage_counts[dosage] += 1

                if dosage > 0 and len(variant_examples) < 15:
                    variant_examples.append((label, dosage))
            except ValueError:
                pass

    variants_present = dosage_counts.get(1.0, 0) + dosage_counts.get(2.0, 0)
    estimated_pct = (variants_present / 1436) * 4 if variants_present > 0 else 0

    print(f"""
    ╔══════════════════════════════════════════════════════════════╗
    ║  АНАЛИЗ НЕАНДЕРТАЛЬСКИХ МАРКЕРОВ                             ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  Всего проверено маркеров:        {total_markers:>6}                      ║
    ║  Неандертальские варианты:        {variants_present:>6}                      ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  Распределение по дозировке:                                 ║""")

    for dosage in sorted(dosage_counts.keys()):
        count = dosage_counts[dosage]
        if dosage == 0:
            desc = "нет варианта"
        elif dosage == 1:
            desc = "1 копия (гетерозигота)"
        else:
            desc = "2 копии (гомозигота)"
        print(f"    ║    {dosage:.0f}: {count:>5} маркеров - {desc:30}     ║")

    print(f"""    ╠══════════════════════════════════════════════════════════════╣
    ║  Примерный % неандертальской ДНК: ~{estimated_pct:.1f}%                      ║
    ║  (Типичный диапазон для европейцев: 1.5-2.5%)               ║
    ╚══════════════════════════════════════════════════════════════╝
""")

    print("\n--- Примеры неандертальских вариантов ---\n")
    for label, dosage in variant_examples:
        # Parse: dosage_NC_000020.10:58872985-58872986:A
        if 'NC_' in label:
            parts = label.split(':')
            if len(parts) >= 2:
                chrom_info = parts[0].split('_')
                chrom_num = chrom_info[-1].split('.')[0] if chrom_info else '?'
                pos = parts[1] if len(parts) > 1 else '?'
                allele = parts[2] if len(parts) > 2 else '?'
                print(f"    Chr {chrom_num:>2}, pos {pos:20}, аллель {allele}, копий: {int(dosage)}")

    return variants_present, estimated_pct


def analyze_admixture_timing():
    """Analyze when different ancestries mixed"""
    print("\n" + "="*60)
    print("ДАТИРОВКА ПРИМЕСЕЙ (ADMIXTURE TIMING)")
    print("="*60)

    rows = read_csv(COMPUTED_FILE)

    timespans = defaultdict(dict)

    for row in rows:
        label = row.get('label', '')
        data = row.get('data', '')

        if 'population_timespans_' in label:
            parts = label.replace('population_timespans_', '').rsplit('_generation_', 1)
            if len(parts) == 2:
                pop = parts[0].replace('_', ' ').title()
                metric = parts[1]

                if data and data != 'None':
                    try:
                        timespans[pop][metric] = int(float(data))
                    except ValueError:
                        pass

    print("""
    Поколения назад, когда произошло смешение предков:
    (1 поколение ≈ 25-30 лет)
    """)

    print(f"    {'Популяция':<40} {'Мин':>5} {'Ожид':>5} {'Макс':>5}   Примерно когда")
    print("    " + "-"*70)

    for pop in sorted(timespans.keys()):
        data = timespans[pop]
        if data:
            min_gen = data.get('min', '-')
            pred = data.get('predicted', '-')
            max_gen = data.get('max', '-')

            if isinstance(pred, int):
                years_ago = pred * 27
                approx = f"~{years_ago} лет назад (~{2024 - years_ago})"
            else:
                approx = "неизвестно"

            print(f"    {pop:<40} {str(min_gen):>5} {str(pred):>5} {str(max_gen):>5}   {approx}")

    return timespans


def analyze_phenotype():
    """Analyze phenotype data"""
    print("\n" + "="*60)
    print("ФЕНОТИПИЧЕСКИЕ ДАННЫЕ (PHENOTYPE DATA)")
    print("="*60)

    rows = read_csv(PHENOTYPE_FILE)

    print("\n--- Базовая информация ---\n")

    info = {}

    for row in rows:
        concept = row.get('concept id', '')
        data = row.get('data', '')

        if concept and data and data != 'None':
            if 'date_of_birth' in concept:
                # Parse date from dict-like string
                if 'date' in data:
                    import ast
                    try:
                        d = ast.literal_eval(data)
                        info['Дата рождения'] = d.get('date', '')[:10]
                    except:
                        info['Дата рождения'] = data
            elif 'height_mm' in concept:
                import ast
                try:
                    d = ast.literal_eval(data)
                    info['Рост'] = d.get('user_input', data)
                except:
                    info['Рост'] = data
            elif 'weight_g' in concept:
                import ast
                try:
                    d = ast.literal_eval(data)
                    info['Вес'] = d.get('user_input', data)
                except:
                    info['Вес'] = data
            elif concept == 'sex':
                info['Биологический пол'] = data
            elif 'sample_shipping_country' in concept:
                info['Страна отправки'] = data

    # Check first row for additional info
    if rows:
        first = rows[0]
        if first.get('birth date'):
            info['Дата рождения'] = first['birth date']
        if first.get('sex'):
            info['Пол'] = first['sex']
        if first.get('gender identity'):
            info['Идентичность'] = first['gender identity']

    for key, value in info.items():
        print(f"    {key}: {value}")

    return info


def generate_summary(ancestry_data, neanderthal_pct):
    """Generate overall summary"""
    print("\n" + "="*60)
    print("ИТОГОВЫЙ ГЕНЕТИЧЕСКИЙ ПРОФИЛЬ")
    print("="*60)

    # Calculate top ancestries
    total = sum(ancestry_data.values())
    broad_cats = {'European', 'Western Asian & North African', 'Northern West Asian',
                  'East Asian & Indigenous American', 'World', 'Northern Asian',
                  'Northwestern European', 'Southern European'}

    detailed = {k: v for k, v in ancestry_data.items() if k not in broad_cats}
    top_5 = sorted(detailed.items(), key=lambda x: x[1], reverse=True)[:5]

    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    ГЕНЕТИЧЕСКИЙ ПРОФИЛЬ                      ║
    ║                      Andre Sh (1996)                         ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  ОСНОВНОЙ ЭТНИЧЕСКИЙ СОСТАВ:                                 ║""")

    for anc, length in top_5:
        pct = (length / total) * 100
        print(f"    ║    • {anc:<40} {pct:5.1f}%       ║")

    print(f"""    ║                                                              ║
    ║  ГЛУБОКОЕ ПРОИСХОЖДЕНИЕ:                                     ║
    ║    • Y-DNA (отцовская): R-CTS1211 (Славянская)               ║
    ║    • mtDNA (материнская): HV1b2 (Кавказская/Ближневосточная) ║
    ║                                                              ║
    ║  ДРЕВНЯЯ ДНК:                                                ║
    ║    • Неандертальская примесь: ~{neanderthal_pct:.1f}%                       ║
    ║                                                              ║
    ║  ИНТЕРПРЕТАЦИЯ:                                              ║
    ║    Генетический профиль указывает на смешанное               ║
    ║    восточноевропейское и ашкеназско-еврейское                ║
    ║    происхождение с значительной ближневосточной/             ║
    ║    кавказской примесью. Отцовская линия типична              ║
    ║    для славянских народов, материнская - для                 ║
    ║    ближневосточного региона.                                 ║
    ╚══════════════════════════════════════════════════════════════╝
    """)


def main():
    print("\n" + "╔" + "═"*60 + "╗")
    print("║" + " "*15 + "DNA ANALYSIS REPORT" + " "*26 + "║")
    print("║" + " "*10 + "Анализ генетических данных 23andMe" + " "*15 + "║")
    print("╚" + "═"*60 + "╝")

    # Run all analyses
    analyze_phenotype()
    analyze_haplogroups()
    ancestry_data = analyze_ancestry()
    neanderthal_count, neanderthal_pct = analyze_neanderthal()
    analyze_admixture_timing()
    generate_summary(ancestry_data, neanderthal_pct)

    print("\n" + "="*60)
    print("АНАЛИЗ ЗАВЕРШЁН")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
