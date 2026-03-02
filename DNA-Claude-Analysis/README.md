# DNA Claude Analysis

A personal genome analysis toolkit that parses raw DNA data (23andMe format) and generates detailed markdown reports across 17 health and trait categories. Optionally produces a single-page HTML visualization with a terminal/hacker aesthetic.

## Features

- Analyzes 500+ SNP markers across multiple categories
- Zero external dependencies — uses only Python standard library
- Generates markdown reports for each category
- Categories include: ancestry, health risks, nutrition, sports/fitness, psychology, cognitive traits, longevity, sleep, immunity, pain sensitivity, detoxification, skin, vision/hearing, physical traits, pharmacogenomics, and carrier status

## Setup

1. Export your raw DNA data from 23andMe (or similar service)
2. Place your genome file as `data/genome_data.txt` in the script directory
3. Run any analysis script:

```bash
python health_analysis.py
```

Or run all analyses at once:

```bash
for f in *_analysis.py; do python "$f"; done
```

Reports will be saved to the `reports/` directory.

## Scripts

| Script | Description |
|--------|-------------|
| `analyze_dna.py` | General DNA data overview (ancestry, computed traits, phenotypes) |
| `ancestry_analysis.py` | Ethnic composition and haplogroup analysis |
| `health_analysis.py` | Cardiovascular, diabetes, oncology and other health risk markers |
| `nutrition_analysis.py` | Nutrient metabolism, food sensitivities, dietary recommendations |
| `sports_fitness_analysis.py` | Muscle fiber type, endurance, injury risk |
| `psychology_analysis.py` | Behavioral traits, stress response, personality markers |
| `cognitive_analysis.py` | Memory, learning ability, neuroprotection |
| `longevity_analysis.py` | Aging markers, telomere length, cellular repair |
| `sleep_chronotype_analysis.py` | Circadian rhythm, sleep quality, chronotype |
| `immunity_analysis.py` | Immune response, autoimmune risk, inflammation |
| `pain_sensitivity_analysis.py` | Pain perception and analgesic response |
| `detoxification_analysis.py` | Liver enzyme activity, toxin metabolism |
| `skin_analysis.py` | Skin aging, UV sensitivity, collagen markers |
| `vision_hearing_analysis.py` | Eye disease risk, hearing loss markers |
| `physical_traits_analysis.py` | Height, hair, eye color and other trait predictions |
| `carrier_status_analysis.py` | Recessive disease carrier screening |
| `reproductive_analysis.py` | Fertility and reproductive health markers |

## Input Format

The scripts expect a 23andMe raw data export file (`genome_data.txt`) in standard tab-separated format:

```
# rsid  chromosome  position  genotype
rs4477212	1	82154	AA
rs3094315	1	752566	AG
...
```

## Output

Each script generates a markdown report in the `reports/` directory with:
- SNP-level findings with risk assessment
- Color-coded risk levels (normal / moderate / high)
- Summary statistics and recommendations

## Disclaimer

This tool is for educational and informational purposes only. It is not medical advice. Always consult a qualified healthcare professional for medical decisions.
