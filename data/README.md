# Data Documentation

## Overview

This directory contains data files and documentation for the catalyst activity prediction model.

## Files

| File | Description |
|------|-------------|
| `data_dictionary.md` | Detailed description of all features and target variable |
| `catalyst_data.csv` | Main dataset (if included) |
| `processed_data.csv` | Preprocessed dataset used for model training |

## Data Description

The dataset contains catalyst characterization data and corresponding activity measurements. See [data_dictionary.md](data_dictionary.md) for detailed feature descriptions.

## Data Collection

- **Source**: [Experimental measurements / Literature compilation / Database]
- **Collection Period**: [YYYY-YYYY]
- **Sample Size**: [X] observations
- **Quality Control**: [Description of QC procedures]

## Data Usage

### Access
Data is available for research and educational purposes under the project's MIT License.

### Citation
If you use this data, please cite:
```
[Author Name]. (2024). Catalyst Activity Dataset. 
https://github.com/yourusername/catalyst-activity
```

### Redistribution
Please do not redistribute without permission. Direct users to the original repository.

## Data Processing

Raw data undergoes the following preprocessing steps:
1. Missing value imputation (median for continuous features)
2. Outlier detection and treatment (IQR method)
3. Feature scaling (StandardScaler)
4. Categorical encoding (Label encoding for metals)

## Missing Data

| Feature | % Missing | Imputation Method |
|---------|-----------|-------------------|
| Metal | 0% | N/A |
| Surface Area | X% | Median |
| Band Gap | X% | Median |
| Particle Size | X% | Median |
| Pore Volume | X% | Median |
| Temperature | 0% | N/A |
| pH | 0% | N/A |
| Time | 0% | N/A |
| Activity | 0% | N/A |

## Contact

For questions about the data, please open an issue on GitHub or contact [your.email@example.com].
