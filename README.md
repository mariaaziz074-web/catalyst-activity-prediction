# Catalyst Activity Prediction

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)

A machine learning web application for predicting catalyst activity based on chemical descriptors. Built with reproducibility and open science principles.

## Overview

This application uses a pre-trained ML model to predict catalyst activity (%) based on:

| Feature | Unit | Description | Typical Range |
|---------|------|-------------|---------------|
| Metal | - | Catalyst metal type | Categorical |
| Surface Area | m²/g | BET specific surface area | 10-500 |
| Band Gap | eV | Electronic band gap energy | 0.5-5.0 |
| Particle Size | nm | Average crystallite size (XRD) | 5-100 |
| Pore Volume | cm³/g | Total pore volume (BJH method) | 0.1-2.0 |
| Temperature | °C | Reaction temperature | 20-200 |
| pH | - | Solution pH | 1-14 |
| Reaction Time | min | Reaction duration | 10-300 |

## Scientific Background

Catalyst activity prediction enables:
- **Materials Discovery**: Accelerating identification of novel catalysts
- **Process Optimization**: Finding optimal reaction conditions
- **Sustainable Chemistry**: Reducing experimental waste

Key descriptors influencing catalytic performance:
- **Electronic properties**: Band gap affects charge carrier dynamics
- **Structural properties**: Surface area and particle size determine active sites
- **Textural properties**: Pore volume influences mass transfer
- **Reaction conditions**: Temperature, pH, and time control kinetics

## Project Structure

```
catalyst-activity/
├── app.py                      # Main Streamlit application
├── catalyst_model.pkl          # Pre-trained ML model
├── metal_encoder.pkl           # Label encoder for metals
├── requirements.txt            # Python dependencies
├── environment.yml             # Conda environment
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Docker orchestration
├── setup.py                    # Package setup
├── README.md                   # This file
├── LICENSE                     # MIT License
├── CITATION.cff                # Citation metadata
├── .gitignore                  # Git ignore rules
├── .streamlit/
│   └── config.toml             # Streamlit config
├── data/
│   ├── README.md               # Data documentation
│   └── data_dictionary.md      # Feature descriptions
├── models/

## Installation

### Option 1: Using pip

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/catalyst-activity.git
   cd catalyst-activity
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Using Conda (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/catalyst-activity.git
   cd catalyst-activity
   ```

2. Create conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate catalyst-activity
   ```

### Option 3: Using Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/catalyst-activity.git
   cd catalyst-activity
   ```

2. Build and run:
   ```bash
   docker-compose up --build
   ```

3. Open browser at `http://localhost:8501`

## Usage

1. Ensure model files (`catalyst_model.pkl` and `metal_encoder.pkl`) are in project root.

2. Run the application:
   ```bash
   streamlit run app.py
   ```

3. Navigate to `http://localhost:8501` in your browser.

4. Input catalyst parameters and click **Predict Activity**.

## Model Documentation

See [models/model_card.md](models/model_card.md) for:
- Model architecture and algorithm
- Training methodology
- Performance metrics
- Limitations and intended use

## Reproducibility

This project follows FAIR principles:

1. **Version Pinning**: All dependencies pinned to specific versions
2. **Environment Files**: Both `requirements.txt` and `environment.yml` provided
3. **Containerization**: Dockerfile ensures identical execution environment
4. **Notebooks**: Complete training pipeline in Jupyter notebooks
5. **Tests**: Unit tests validate functionality
6. **Model Card**: Comprehensive model documentation

## Running Tests

```bash
pip install pytest pytest-cov
pytest tests/ -v
pytest tests/ --cov=app --cov-report=html
```

## Performance Metrics

| Metric | Value |
|--------|-------|
| R² Score | 0.XX |
| RMSE | X.XX% |
| MAE | X.XX% |
| CV Score | 0.XX ± 0.XX |

*Update with actual model performance metrics*

## Citation

```bibtex
@software{catalyst_activity_2024,
  author = {Author Name},
  title = {Catalyst Activity Prediction using Machine Learning},
  year = {2024},
  url = {https://github.com/yourusername/catalyst-activity}
}
```

See [CITATION.cff](CITATION.cff) for full citation information.

## Contributing

Read our [Contributing Guidelines](docs/CONTRIBUTING.md) before submitting a pull request.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE).

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- ML powered by [Scikit-learn](https://scikit-learn.org/)
- Data analysis with [Pandas](https://pandas.pydata.org/)

## Contact

For questions or feedback, please open an issue on GitHub.

