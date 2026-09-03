"""
Unit tests for the Catalyst Activity Prediction application.
"""

import pytest
import pandas as pd
import numpy as np
import joblib
from unittest.mock import patch, MagicMock


class TestDataPreparation:
    """Tests for data preparation and validation."""

    def test_input_dataframe_creation(self):
        """Test that input DataFrame is created correctly."""
        metal_encoded = 1
        surface_area = 150.0
        band_gap = 2.1
        particle_size = 20.0
        pore_volume = 0.6
        temperature = 40.0
        pH = 7.0
        time = 90.0

        new_data = pd.DataFrame(
            {
                "Metal": [metal_encoded],
                "SurfaceArea": [surface_area],
                "BandGap": [band_gap],
                "ParticleSize": [particle_size],
                "PoreVolume": [pore_volume],
                "Temperature": [temperature],
                "pH": [pH],
                "Time": [time],
            }
        )

        assert list(new_data.columns) == [
            "Metal",
            "SurfaceArea",
            "BandGap",
            "ParticleSize",
            "PoreVolume",
            "Temperature",
            "pH",
            "Time",
        ]
        assert len(new_data) == 1
        assert new_data["SurfaceArea"].iloc[0] == 150.0

    def test_input_ranges(self):
        """Test that input values are within expected ranges."""
        # Surface area should be positive
        assert 10 <= 150.0 <= 500
        # Band gap should be positive
        assert 0.5 <= 2.1 <= 5.0
        # pH should be 0-14
        assert 0 <= 7.0 <= 14
        # Particle size should be positive
        assert 5 <= 20.0 <= 100


class TestModelLoading:
    """Tests for model loading functionality."""

    def test_model_files_exist(self):
        """Test that model files are present."""
        import os

        assert os.path.exists("catalyst_model.pkl"), "Model file not found"
        assert os.path.exists("metal_encoder.pkl"), "Encoder file not found"

    def test_model_can_predict(self):
        """Test that loaded model can make predictions."""
        model = joblib.load("catalyst_model.pkl")
        encoder = joblib.load("metal_encoder.pkl")

        # Create sample input
        metal = encoder.classes_[0]
        metal_encoded = encoder.transform([metal])[0]

        new_data = pd.DataFrame(
            {
                "Metal": [metal_encoded],
                "SurfaceArea": [150.0],
                "BandGap": [2.1],
                "ParticleSize": [20.0],
                "PoreVolume": [0.6],
                "Temperature": [40.0],
                "pH": [7.0],
                "Time": [90.0],
            }
        )

        prediction = model.predict(new_data)
        assert len(prediction) == 1
        assert isinstance(prediction[0], (int, float, np.floating))

    def test_encoder_classes(self):
        """Test that encoder has valid classes."""
        encoder = joblib.load("metal_encoder.pkl")
        assert len(encoder.classes_) > 0
        assert all(isinstance(c, str) for c in encoder.classes_)


class TestPredictionOutput:
    """Tests for prediction output validation."""

    def test_prediction_range(self):
        """Test that predictions are within valid range."""
        model = joblib.load("catalyst_model.pkl")
        encoder = joblib.load("metal_encoder.pkl")

        # Test with multiple inputs
        for metal in encoder.classes_[:3]:  # Test first 3 metals
            metal_encoded = encoder.transform([metal])[0]
            new_data = pd.DataFrame(
                {
                    "Metal": [metal_encoded],
                    "SurfaceArea": [150.0],
                    "BandGap": [2.1],
                    "ParticleSize": [20.0],
                    "PoreVolume": [0.6],
                    "Temperature": [40.0],
                    "pH": [7.0],
                    "Time": [90.0],
                }
            )
            prediction = model.predict(new_data)
            # Activity should be between 0 and 100
            assert 0 <= prediction[0] <= 100, f"Prediction {prediction[0]} out of range for {metal}"


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_minimum_values(self):
        """Test prediction with minimum input values."""
        model = joblib.load("catalyst_model.pkl")
        encoder = joblib.load("metal_encoder.pkl")

        metal_encoded = encoder.transform([encoder.classes_[0]])[0]
        new_data = pd.DataFrame(
            {
                "Metal": [metal_encoded],
                "SurfaceArea": [10.0],
                "BandGap": [0.5],
                "ParticleSize": [5.0],
                "PoreVolume": [0.1],
                "Temperature": [20.0],
                "pH": [1.0],
                "Time": [10.0],
            }
        )
        prediction = model.predict(new_data)
        assert len(prediction) == 1

    def test_maximum_values(self):
        """Test prediction with maximum input values."""
        model = joblib.load("catalyst_model.pkl")
        encoder = joblib.load("metal_encoder.pkl")

        metal_encoded = encoder.transform([encoder.classes_[0]])[0]
        new_data = pd.DataFrame(
            {
                "Metal": [metal_encoded],
                "SurfaceArea": [500.0],
                "BandGap": [5.0],
                "ParticleSize": [100.0],
                "PoreVolume": [2.0],
                "Temperature": [200.0],
                "pH": [14.0],
                "Time": [300.0],
            }
        )
        prediction = model.predict(new_data)
        assert len(prediction) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
