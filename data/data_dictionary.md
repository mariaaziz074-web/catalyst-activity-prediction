# Data Dictionary: Catalyst Activity Dataset

## Overview

This document describes the features and target variable used in the catalyst activity prediction model.

## Target Variable

### Catalyst Activity
- **Variable Name**: `Activity`
- **Description**: Percentage of substrate converted to product under specified conditions
- **Unit**: Percentage (%)
- **Range**: 0-100%
- **Type**: Continuous numeric
- **Measurement Method**: [e.g., GC analysis, spectrophotometry]

## Feature Variables

### Metal
- **Variable Name**: `Metal`
- **Description**: Type of metal used as the active catalytic component
- **Type**: Categorical
- **Categories**: [List all metals - e.g., Pt, Pd, Ni, Cu, Fe, Co, Au, Ag]
- **Encoding**: Label encoded for model input
- **Source**: Experimental design

### Surface Area
- **Variable Name**: `SurfaceArea`
- **Description**: Specific surface area of the catalyst material
- **Unit**: m²/g
- **Range**: 10-500 m²/g
- **Type**: Continuous numeric
- **Measurement Method**: Brunauer-Emmett-Teller (BET) method
- **Instrument**: [e.g., Micromeritics ASAP 2020]
- **Notes**: Measured using N₂ adsorption at 77K

### Band Gap
- **Variable Name**: `BandGap`
- **Description**: Energy difference between valence band and conduction band
- **Unit**: eV
- **Range**: 0.5-5.0 eV
- **Type**: Continuous numeric
- **Measurement Method**: [e.g., UV-Vis diffuse reflectance spectroscopy (DRS)]
- **Calculation**: Tauc plot method for indirect/direct bandgap determination
- **Instrument**: [e.g., Shimadzu UV-2600]

### Particle Size
- **Variable Name**: `ParticleSize`
- **Description**: Average crystallite size of catalyst nanoparticles
- **Unit**: nm
- **Range**: 5-100 nm
- **Type**: Continuous numeric
- **Measurement Method**: X-ray Diffraction (XRD) - Scherrer equation
- **Instrument**: [e.g., Bruker D8 Advance]
- **Notes**: Calculated from full width at half maximum (FWHM) of characteristic peaks

### Pore Volume
- **Variable Name**: `PoreVolume`
- **Description**: Total pore volume of the catalyst material
- **Unit**: cm³/g
- **Range**: 0.1-2.0 cm³/g
- **Type**: Continuous numeric
- **Measurement Method**: Barrett-Joyner-Halenda (BJH) method
- **Instrument**: [e.g., Micromeritics ASAP 2020]
- **Notes**: Calculated from N₂ adsorption-desorption isotherms

### Temperature
- **Variable Name**: `Temperature`
- **Description**: Reaction temperature during catalytic testing
- **Unit**: °C
- **Range**: 20-200°C
- **Type**: Continuous numeric
- **Control Method**: [e.g., oil bath, heating mantle with PID controller]
- **Measurement**: Thermocouple/RTD with ±1°C accuracy

### pH
- **Variable Name**: `pH`
- **Description**: Acidity/basicity of the reaction solution
- **Unit**: pH scale (dimensionless)
- **Range**: 1-14
- **Type**: Continuous numeric
- **Measurement Method**: pH meter with glass electrode
- **Instrument**: [e.g., Mettler Toledo SevenExcellence]
- **Calibration**: Calibrated with standard buffer solutions (pH 4, 7, 10)

### Reaction Time
- **Variable Name**: `Time`
- **Description**: Duration of the catalytic reaction
- **Unit**: minutes (min)
- **Range**: 10-300 min
- **Type**: Continuous numeric
- **Measurement**: Digital timer with ±1 min accuracy

## Data Quality

### Missing Values
- **Handling Strategy**: [e.g., median imputation, row removal]
- **Percentage Missing**: <5% for all features

### Outlier Detection
- **Method**: [e.g., IQR method, Z-score > 3]
- **Treatment**: [e.g., Winsorization, removal]

### Data Validation
- Range checks applied to all continuous variables
- Cross-referenced with literature values where possible

## Preprocessing Steps

1. **Missing Value Imputation**: Median imputation for continuous features
2. **Outlier Treatment**: Winsorization at 1st and 99th percentiles
3. **Feature Scaling**: StandardScaler (zero mean, unit variance)
4. **Categorical Encoding**: Label encoding for metal types
5. **Train/Test Split**: 80/20 stratified split by metal type

## Data Provenance

- **Source**: [Experimental data from laboratory / Published database / Literature compilation]
- **Collection Period**: [YYYY-YYYY]
- **Number of Samples**: [X]
- **Number of Unique Catalysts**: [Y]
- **Publication**: [Reference if applicable]

## Usage Notes

- All measurements should follow standard protocols for comparability
- Report measurement uncertainty when available
- Document any deviations from standard conditions
- Consider catalyst stability and reusability in interpretation

## Example Data Row

| Metal | SurfaceArea | BandGap | ParticleSize | PoreVolume | Temperature | pH | Time | Activity |
|-------|-------------|---------|--------------|------------|-------------|-----|------|----------|
| Pt | 150.0 | 2.1 | 20.0 | 0.6 | 40.0 | 7.0 | 90.0 | 85.3 |
