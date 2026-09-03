# Dataset Documentation

This directory contains documentation for the dataset used by the **Catalyst Activity Prediction** machine-learning project.

The dataset contains catalyst descriptors and measured catalyst activity values used to train and evaluate the prediction model.

The current dataset contains **15 observations** and **9 columns**.

---

## Dataset Files

| File                                           | Description                               |
| ---------------------------------------------- | ----------------------------------------- |
| [`../catalyst_data.csv`](../catalyst_data.csv) | Main dataset used by the project          |
| [`data_dictionary.md`](data_dictionary.md)     | Detailed definitions of dataset variables |

---

## Dataset Schema

The dataset contains **15 observations and 9 columns**.

| Variable       | Unit  | Role    | Description                                  |
| -------------- | ----- | ------- | -------------------------------------------- |
| `Metal`        | —     | Feature | Metal used as the active catalytic component |
| `SurfaceArea`  | m²/g  | Feature | Specific surface area of the catalyst        |
| `BandGap`      | eV    | Feature | Electronic band-gap energy                   |
| `ParticleSize` | nm    | Feature | Average particle or crystallite size         |
| `PoreVolume`   | cm³/g | Feature | Total pore volume of the catalyst            |
| `Temperature`  | °C    | Feature | Reaction temperature                         |
| `pH`           | —     | Feature | Reaction-solution pH                         |
| `Time`         | min   | Feature | Reaction duration                            |
| `Activity`     | %     | Target  | Measured catalyst activity                   |

For more detailed variable definitions, see [`data_dictionary.md`](data_dictionary.md).

---

## Dataset Contents

The dataset contains seven metal categories:

* Cu
* Co
* Ni
* Zn
* Fe
* Mn
* Ti

The numerical descriptors represent catalyst properties and reaction conditions.

`Activity` is the prediction target.

---

## Data Quality

The dataset is intentionally small, containing **15 observations**.

Because of this limited sample size:

* Model performance should be interpreted cautiously.
* Predictions should not be assumed to generalize to catalysts outside the represented data domain.
* Reported performance metrics are descriptive of this dataset and modeling workflow.
* Independent experimental validation is recommended before using predictions for research decisions.

The dataset should therefore be regarded as a **small proof-of-concept scientific ML dataset**, rather than a comprehensive representation of catalyst chemistry.

---

## Preprocessing

The categorical `Metal` feature is encoded numerically before being supplied to the machine-learning model.

The trained encoder is stored in the project root:

```text
metal_encoder.pkl
```

The trained prediction model is stored in:

```text
catalyst_model.pkl
```

The preprocessing and modeling workflow can be inspected in:

[`../activity_prediction.ipynb`](../activity_prediction.ipynb)

---

## Important Scientific Considerations

### Domain Dependence

The dataset covers only a limited range of catalyst descriptors and reaction conditions. Predictions for substantially different systems may therefore be unreliable.

### Dataset Size

With only 15 observations, the dataset is too small to support strong claims of generalization to unseen catalyst families or broad chemical space.

### Experimental Context

Catalyst activity can depend on many variables that are not represented in this dataset, including:

* Catalyst composition and structure
* Preparation conditions
* Reactant identity and concentration
* Solvent
* Irradiation or energy source
* Mass-transfer effects
* Measurement protocol

### Prediction Is Not Validation

A machine-learning prediction should be considered a **screening estimate**, rather than an experimental result.

Candidate predictions should be experimentally validated before scientific conclusions are drawn.

---

## Data Provenance

The repository currently does not provide sufficient verified provenance information to establish a specific external database, publication, or collection period for every observation.

Therefore, unsupported provenance claims are intentionally not made here.

If the dataset is expanded or formally published, provenance information should be added for each data source where appropriate.

---

## Reproducibility

To reproduce the analysis, use the workflow provided in the parent repository:

[`../activity_prediction.ipynb`](../activity_prediction.ipynb)

The trained model and encoder are also provided in the repository for running the interactive application without retraining.

---

## Responsible Use

This dataset and its associated model are intended for:

* Educational scientific machine-learning work
* Exploratory catalyst screening
* Reproducibility demonstrations
* Development and testing of catalyst-activity prediction workflows

They should **not** be used as a substitute for experimental validation or as evidence of catalyst superiority without appropriate experimental confirmation.

---

## Related Documentation

* [Main Project README](../README.md)
* [Data Dictionary](data_dictionary.md)
* [Model Card](../models/model_card.md)
* [Analysis Notebook](../activity_prediction.ipynb)
* [Dataset](../catalyst_data.csv)
