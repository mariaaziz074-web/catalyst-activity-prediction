# Model Card: Catalyst Activity Prediction Model

## Model Details

- **Model Name**: Catalyst Activity Predictor
- **Model Type**: Supervised Machine Learning Regression
- **Algorithm**: [e.g., Random Forest Regressor / Gradient Boosting / Neural Network]
- **Version**: 1.0.0
- **Date**: 2024-01-01
- **Developers**: [Your Name, Institution]
- **Contact**: [your.email@example.com]
- **License**: MIT

## Intended Use

### Primary Use Cases
- Predicting catalyst activity for novel materials during computational screening
- Optimizing reaction conditions for catalytic processes
- Educational tool for teaching machine learning in chemistry

### Intended Users
- Computational chemists and materials scientists
- Chemical engineers working on catalyst design
- Researchers in sustainable chemistry

### Out-of-Scope Uses
- Predicting catalyst selectivity or stability
- Replacing experimental validation entirely
- Industrial-scale process control without experimental verification

## Training Data

### Data Sources
- [Describe data source - e.g., published literature, experimental database, etc.]
- Number of samples: [X]
- Time period: [YYYY-YYYY]

### Data Collection Methods
- Catalyst synthesis and characterization following standard protocols
- Activity measurements under controlled conditions
- Quality control: [describe QC procedures]

### Data Preprocessing
1. Missing value handling: [e.g., median imputation, removal]
2. Outlier detection: [e.g., IQR method, Z-score]
3. Feature scaling: [e.g., StandardScaler, MinMaxScaler]
4. Categorical encoding: Label encoding for metal types

## Evaluation Data

- **Train/Test Split**: [e.g., 80/20 split]
- **Cross-Validation**: [e.g., 5-fold CV]
- **Evaluation Set**: [describe holdout set characteristics]

## Model Architecture

### Features (Input Variables)
| Feature | Type | Description | Preprocessing |
|---------|------|-------------|---------------|
| Metal | Categorical | Catalyst metal type | Label encoded |
| Surface Area | Continuous | BET surface area (m²/g) | Standardized |
| Band Gap | Continuous | Electronic band gap (eV) | Standardized |
| Particle Size | Continuous | Crystallite size (nm) | Standardized |
| Pore Volume | Continuous | Total pore volume (cm³/g) | Standardized |
| Temperature | Continuous | Reaction temperature (°C) | Standardized |
| pH | Continuous | Solution pH | Standardized |
| Time | Continuous | Reaction time (min) | Standardized |

### Target Variable
- **Name**: Catalyst Activity
- **Unit**: Percentage (%)
- **Range**: [0-100%]

### Hyperparameters
```python
{
    "n_estimators": 100,
    "max_depth": 10,
    "min_samples_split": 5,
    "min_samples_leaf": 2,
    "random_state": 42
}
```

## Performance Metrics

### Overall Performance
| Metric | Train | Test | CV (5-fold) |
|--------|-------|------|-------------|
| R² | 0.XX | 0.XX | 0.XX ± 0.XX |
| RMSE | X.XX% | X.XX% | X.XX ± X.XX |
| MAE | X.XX% | X.XX% | X.XX ± X.XX |
| MAPE | X.XX% | X.XX% | X.XX ± X.XX |

### Performance by Metal Type
| Metal | R² | RMSE | MAE | N samples |
|-------|-----|------|-----|-----------|
| [Metal 1] | 0.XX | X.XX | X.XX | XX |
| [Metal 2] | 0.XX | X.XX | X.XX | XX |
| [Metal 3] | 0.XX | X.XX | X.XX | XX |

## Feature Importance

| Rank | Feature | Importance Score |
|------|---------|------------------|
| 1 | [Feature] | 0.XX |
| 2 | [Feature] | 0.XX |
| 3 | [Feature] | 0.XX |
| 4 | [Feature] | 0.XX |
| 5 | [Feature] | 0.XX |
| 6 | [Feature] | 0.XX |
| 7 | [Feature] | 0.XX |
| 8 | [Feature] | 0.XX |

## Limitations

### Data Limitations
- Limited to specific metal types in training data
- Experimental conditions may not cover all real-world scenarios
- Potential measurement errors in original data

### Model Limitations
- Predictions are interpolative; extrapolation may be unreliable
- Does not account for catalyst deactivation over time
- Assumes ideal mixing and mass transfer conditions
- May not generalize to significantly different catalyst classes

### Known Biases
- Overrepresentation of certain metal types in training data
- Laboratory-scale conditions may not reflect industrial performance

## Ethical Considerations

- Model predictions should be validated experimentally before implementation
- Not intended for safety-critical applications without verification
- Users should understand the limitations before making decisions

## Caveats and Recommendations

1. **Validation**: Always validate predictions with experiments
2. **Uncertainty**: Consider prediction uncertainty in decision-making
3. **Domain of Applicability**: Check if inputs fall within training data range
4. **Updates**: Model should be retrained as new data becomes available

## How to Use

```python
import joblib
import pandas as pd

# Load model and encoder
model = joblib.load("catalyst_model.pkl")
encoder = joblib.load("metal_encoder.pkl")

# Prepare input data
new_data = pd.DataFrame({
    "Metal": encoder.transform(["Pt"])[0],
    "SurfaceArea": [150.0],
    "BandGap": [2.1],
    "ParticleSize": [20.0],
    "PoreVolume": [0.6],
    "Temperature": [40.0],
    "pH": [7.0],
    "Time": [90.0]
})

# Make prediction
prediction = model.predict(new_data)
print(f"Predicted Activity: {prediction[0]:.2f}%")
```

## References

1. [Reference to related paper/publication]
2. [Reference to dataset]
3. [Reference to methodology]

## Changelog

- **v1.0.0** (2024-01-01): Initial release
