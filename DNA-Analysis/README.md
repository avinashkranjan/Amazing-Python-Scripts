## DNA Analysis

### Details of the script

A personal genome analysis toolkit that processes raw DNA data (23andMe / AncestryDNA format) through Python scripts and generates a single-page HTML report with a terminal/hacker aesthetic.

The toolkit analyses 17 biological categories:

- Ancestry composition
- Health risks
- Nutrition and metabolism
- Sports and fitness traits
- Psychology markers
- Cognitive traits
- Longevity indicators
- Sleep patterns
- Immune system variants
- Pain sensitivity
- Detoxification pathways
- Skin traits
- Vision and hearing
- Physical traits
- Pharmacogenomics (drug response)
- Carrier status

Each analysis script reads raw SNP data, looks up known genetic variants, and writes a markdown report. A final generation step combines all reports into a self-contained HTML file styled as a green-on-black terminal dashboard.

### How to use

1. Place your raw DNA file (e.g. `genome.txt`) in the `data/` directory.
2. Set the `GENOME_FILE` variable in each script to point to your file.
3. Run all analysis scripts:

```bash
cd scripts
for f in *_analysis.py; do python "$f"; done
```

4. Open `webpage/dna_terminal.html` in your browser to view the interactive report.

### Modules used

- `re` — regex parsing of raw SNP data
- `json` — structured output
- `pathlib` — file path handling
- Standard library only; no external dependencies required for analysis scripts

### Output preview

The generated HTML report displays all findings colour-coded by risk level (green / amber / red) in a fixed-header, single-page layout with section navigation.

### Project repository

[https://github.com/shmlkv/dna-claude-analysis](https://github.com/shmlkv/dna-claude-analysis)

### Note

This tool is not intended as medical advice. Always consult a qualified healthcare professional regarding any genetic findings.
