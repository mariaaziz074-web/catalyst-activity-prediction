# Catalyst Activity Prediction

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-19%20passed-brightgreen.svg)](#testing)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red.svg)](https://streamlit.io/)

A reproducible machine-learning workflow for predicting catalyst activity from catalyst descriptors and reaction conditions.

The project combines a structured scientific dataset, preprocessing, a trained machine-learning model, model documentation, automated tests, and an interactive Streamlit application.

---

## Overview

Catalyst performance depends on a combination of material properties and reaction conditions. Machine learning can help identify relationships between these variables and measured catalytic activity.

This project demonstrates an end-to-end scientific machine-learning workflow:

1. Prepare a structured catalyst dataset.
2. Encode categorical catalyst information.
3. Train a machine-learning regression model.
4. Evaluate predictive performance.
5. Inspect feature importance.
6. Save the trained model and encoder.
7. Provide an interactive prediction interface.
8. Document the dataset, model, limitations, and reproducibility workflow.

The project is designed as a **reproducibility-first scientific ML example**, rather than a claim of universal catalyst-performance prediction.

---

## Scientific Problem

The objective is to predict measured catalyst activity from a set of catalyst descriptors and experimental conditions.

### Input Variables

| Variable       |  Unit | Role    | Description                                  |
| -------------- | ----: | ------- | -------------------------------------------- |
| `Metal`        |     — | Feature | Metal used as the active catalytic component |
| `SurfaceArea`  |  m²/g | Feature | Specific surface area                        |
| `BandGap`      |    eV | Feature | Electronic band-gap energy                   |
| `ParticleSize` |    nm | Feature | Average particle or crystallite size         |
| `PoreVolume`   | cm³/g | Feature | Total pore volume                            |
| `Temperature`  |    °C | Feature | Reaction temperature                         |
| `pH`           |     — | Feature | Reaction-solution pH                         |
| `Time`         |   min | Feature | Reaction duration                            |
| `Activity`     |     % | Target  | Measured catalyst activity                   |

---

## Dataset

The current dataset contains:

* **15 observations**
* **9 columns**
* **7 metal categories**
* **8 predictor variables**
* **1 continuous target variable**

The dataset should be considered a **small proof-of-concept scientific ML dataset**.

Because of the limited sample size, model performance should be interpreted cautiously and predictions should not be assumed to generalize beyond the represented chemical and experimental domain.

See:

* [`catalyst_data.csv`](catalyst_data.csv)
* [`data/README.md`](data/README.md)
* [`data/data_dictionary.md`](data/data_dictionary.md)

---

## Model Performance

The current model achieves:

| Metric |                        Value |
| ------ | ---------------------------: |
| R²     |                   **0.8161** |
| MAE    | **2.4933 percentage points** |

These values describe performance for the current dataset and modeling workflow.

They should **not** be interpreted as evidence that the model will achieve the same performance on unseen catalyst systems or independent experimental datasets.

### Important Considerations

Model performance may be affected by:

* Small dataset size
* Experimental variability
* Limited feature representation
* Catalyst-specific effects
* Distribution differences between training data and new systems
* Unrepresented reaction variables

Independent experimental validation is recommended before using predictions for research decisions.

---

## Repository Structure

```text
catalyst-activity-prediction/
│
├── activity_prediction.ipynb
├── app.py
├── catalyst_data.csv
├── catalyst_model.pkl
├── metal_encoder.pkl
│
├── data/
│   ├── README.md
│   └── data_dictionary.md
│
├── models/
│   ├── feature_importance.csv
│   └── model_card.md
│
├── tests/
│   ├── __init__.py
│   ├── test_app.py
│   └── test_model.py
│
├── docs/
│   ├── CHANGELOG.md
│   └── CONTRIBUTING.md
│
├── CITATION.cff
├── Dockerfile
├── environment.yml
├── requirements.txt
├── setup.py
├── LICENSE
└── .gitignore
```

---

## Interactive Application

The repository includes an interactive Streamlit application for generating catalyst-activity predictions.

### Run Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then launch the application:

```bash
streamlit run app.py
```

The application allows users to enter:

* Metal
* Surface area
* Band gap
* Particle size
* Pore volume
* Temperature
* pH
* Reaction time

and obtain a model prediction.

---

## Installation

### Option 1 — pip

```bash
git clone https://github.com/mariaaziz074-web/catalyst-activity-prediction.git
cd catalyst-activity-prediction
pip install -r requirements.txt
```

Then:

```bash
streamlit run app.py
```

### Option 2 — Conda

```bash
conda env create -f environment.yml
conda activate catalyst-activity-prediction
```

Then:

```bash
streamlit run app.py
```

### Option 3 — Docker

Build the image:

```bash
docker build -t catalyst-activity-prediction .
```

Run the container according to the port configuration defined by the Dockerfile.

---

## Reproducing the Analysis

The primary analysis workflow is provided in:

[`activity_prediction.ipynb`](activity_prediction.ipynb)

The notebook contains the analysis and modeling workflow used to develop the prediction model.

For reproducibility, users should run the notebook in the documented Python environment rather than assuming that a previously saved model is interchangeable with a newly trained model.

---

## Model Files

The repository includes the trained model and categorical encoder used by the application:

```text
catalyst_model.pkl
metal_encoder.pkl
```

Additional model documentation is available in:

[`models/model_card.md`](models/model_card.md)

Feature-importance results are available in:

[`models/feature_importance.csv`](models/feature_importance.csv)

---

## Testing

The repository includes automated tests using `pytest`.

Run:

```bash
pytest -q
```

The current test suite contains **19 tests**.

A successful run should report:

```text
19 passed
```

You can also check Python syntax with:

```bash
python -m py_compile app.py
```

---

## Data Documentation

Detailed information about the dataset is available in:

* [`data/README.md`](data/README.md)
* [`data/data_dictionary.md`](data/data_dictionary.md)

The data documentation describes the variables, units, roles, preprocessing, data-quality considerations, provenance limitations, and responsible-use considerations.

---

## Limitations

This project has several important limitations.

### Small Dataset

The dataset contains only 15 observations. This substantially limits the statistical strength and generalizability of the model.

### Limited Chemical Representation

Catalyst activity can depend on variables not represented in the current feature set, including:

* Catalyst synthesis conditions
* Surface chemistry
* Crystal structure
* Active-site characteristics
* Reaction mechanism
* Solvent
* Substrate identity
* Irradiation conditions
* Reactor configuration
* Measurement protocol

### Extrapolation Risk

Predictions outside the feature ranges represented in the dataset may be unreliable.

### Correlation Does Not Imply Causation

Feature importance and predictive relationships should not automatically be interpreted as causal chemical mechanisms.

### Experimental Validation

Machine-learning predictions should be treated as computational estimates and hypotheses rather than replacements for experimental measurements.

---

## Intended Use

This project is intended for:

* Scientific machine-learning education
* Exploratory catalyst analysis
* Reproducible computational workflows
* Model-development demonstrations
* Hypothesis generation
* Scientific software and portfolio demonstration

It is **not intended to replace experimental catalyst characterization or validation**.

---

## Reproducibility Philosophy

The project follows a simple principle:

> A scientific ML result is more useful when the data, preprocessing, model, evaluation, tests, and limitations are documented together.

The repository therefore keeps the analysis notebook, trained artifacts, tests, data documentation, model documentation, and application code together.

---

## Contributing

Contributions are welcome.

Before submitting changes:

1. Keep scientific calculations reproducible.
2. Avoid undocumented changes to the dataset.
3. Add or update tests when appropriate.
4. Document changes that affect model behavior.
5. Run the test suite before submitting a pull request.

See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md).

---

## Citation

If you use this repository in research, teaching, or derivative work, please see [`CITATION.cff`](CITATION.cff) for citation information.

---

## License

This project is released under the MIT License.

See [`LICENSE`](LICENSE) for details.

---

## Author

**Maria Aziz**

Computational Chemistry | Scientific Machine Learning | Data-Driven Materials Research

---

## Repository

GitHub:

https://github.com/mariaaziz074-web/catalyst-activity-prediction
