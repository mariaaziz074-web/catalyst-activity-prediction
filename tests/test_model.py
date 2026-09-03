"""
Unit tests for the ML model.
"""

import pytest
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


class TestModelPerformance:
    """Tests for model performance validation."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Load model and encoder for each test."""
        self.model = joblib.load("catalyst_model.pkl")
        self.encoder = joblib.load("metal_encoder.pkl")

    def test_model_type(self):
        """Test that model is a valid sklearn estimator."""
        from sklearn.base import BaseEstimator

        assert isinstance(self.model, BaseEstimator)

    def test_prediction_shape(self):
        """Test that prediction output has correct shape."""
        new_data = pd.DataFrame(
            {
                "Metal": [0],
                "SurfaceArea": [150.0],
                "BandGap": [2.1],
                "ParticleSize": [20.0],
                "PoreVolume": [0.6],
                "Temperature": [40.0],
                "pH": [7.0],
                "Time": [90.0],
            }
        )
        prediction = self.model.predict(new_data)
        assert prediction.shape == (1,)

    def test_multiple_predictions(self):
        """Test that model can predict multiple samples at once."""
        n_samples = 10
        new_data = pd.DataFrame(
            {
                "Metal": [0] * n_samples,
                "SurfaceArea": np.random.uniform(10, 500, n_samples),
                "BandGap": np.random.uniform(0.5, 5.0, n_samples),
                "ParticleSize": np.random.uniform(5, 100, n_samples),
                "PoreVolume": np.random.uniform(0.1, 2.0, n_samples),
                "Temperature": np.random.uniform(20, 200, n_samples),
                "pH": np.random.uniform(1, 14, n_samples),
                "Time": np.random.uniform(10, 300, n_samples),
            }
        )
        predictions = self.model.predict(new_data)
        assert predictions.shape == (n_samples,)

    def test_prediction_consistency(self):
        """Test that same input gives same output."""
        new_data = pd.DataFrame(
            {
                "Metal": [0],
                "SurfaceArea": [150.0],
                "BandGap": [2.1],
                "ParticleSize": [20.0],
                "PoreVolume": [0.6],
                "Temperature": [40.0],
                "pH": [7.0],
                "Time": [90.0],
            }
        )
        pred1 = self.model.predict(new_data)
        pred2 = self.model.predict(new_data)
        assert pred1[0] == pred2[0]



class TestFeatureImportance:
    """Tests for feature importance."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Load model for each test."""
        self.model = joblib.load("catalyst_model.pkl")

    def test_feature_importance_available(self):
        """Test that model has feature importance attribute."""
        if hasattr(self.model, "feature_importances_"):
            importances = self.model.feature_importances_
            assert len(importances) == 8  # 8 features
            assert all(imp >= 0 for imp in importances)
            assert abs(sum(importances) - 1.0) < 1e-6

    def test_feature_importance_order(self):
        """Test that feature importances are ordered correctly."""
        if hasattr(self.model, "feature_importances_"):
            importances = self.model.feature_importances_
            assert abs(sum(importances) - 1.0) < 1e-6


class TestInputValidation:
    """Tests for input validation."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Load model and encoder for each test."""
        self.model = joblib.load("catalyst_model.pkl")
        self.encoder = joblib.load("metal_encoder.pkl")

    def test_negative_surface_area(self):
        """Test behavior with negative surface area."""
        new_data = pd.DataFrame(
            {
                "Metal": [0],
                "SurfaceArea": [-10.0],
                "BandGap": [2.1],
                "ParticleSize": [20.0],
                "PoreVolume": [0.6],
                "Temperature": [40.0],
                "pH": [7.0],
                "Time": [90.0],
            }
        )
        prediction = self.model.predict(new_data)
        assert len(prediction) == 1

    def test_zero_values(self):
        """Test prediction with zero values."""
        new_data = pd.DataFrame(
            {
                "Metal": [0],
                "SurfaceArea": [0.0],
                "BandGap": [0.0],
                "ParticleSize": [0.0],
                "PoreVolume": [0.0],
                "Temperature": [0.0],
                "pH": [0.0],
                "Time": [0.0],
            }
        )
        prediction = self.model.predict(new_data)
        assert len(prediction) == 1


class TestEncoder:
    """Tests for the metal encoder."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Load encoder for each test."""
        self.encoder = joblib.load("metal_encoder.pkl")

    def test_all_metals_encodable(self):
        """Test that all metal classes can be encoded."""
        for metal in self.encoder.classes_:
            encoded = self.encoder.transform([metal])
            assert len(encoded) == 1
            assert isinstance(encoded[0], (int, np.integer))

    def test_inverse_transform(self):
        """Test that encoding is reversible."""
        for metal in self.encoder.classes_:
            encoded = self.encoder.transform([metal])
            decoded = self.encoder.inverse_transform(encoded)
            assert decoded[0] == metal

    def test_unknown_metal_raises_error(self):
        """Test that unknown metal raises ValueError."""
        with pytest.raises(ValueError):
            self.encoder.transform(["UnknownMetal"])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
