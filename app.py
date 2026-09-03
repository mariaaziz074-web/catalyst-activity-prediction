import joblib
import pandas as pd
import streamlit as st


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Catalyst Activity Prediction",
    page_icon="[CAT]",
    layout="centered",
)


# ---------------------------------------------------------
# Load model and encoder
# ---------------------------------------------------------
@st.cache_resource
def load_model():
    """Load the pre-trained model and metal encoder."""
    model = joblib.load("catalyst_model.pkl")
    encoder = joblib.load("metal_encoder.pkl")
    return model, encoder


try:
    model, encoder = load_model()
except FileNotFoundError as e:
    st.error(f"Model files not found: {e}")
    st.info(
        "Please ensure 'catalyst_model.pkl' and "
        "'metal_encoder.pkl' are in the project directory."
    )
    st.stop()


# ---------------------------------------------------------
# Application title and description
# ---------------------------------------------------------
st.title("[CAT] Catalyst Activity Prediction")

st.markdown(
    """
    Predict catalyst activity using machine-learning descriptors.

    Adjust the input parameters below and click **Predict Activity**
    to generate a prediction.
    """
)

st.divider()


# ---------------------------------------------------------
# Input fields
# ---------------------------------------------------------
col1, col2 = st.columns(2)


with col1:
    metal = st.selectbox(
        "Metal",
        encoder.classes_,
        help="Select the type of metal used in the catalyst.",
    )

    surface_area = st.number_input(
        "Surface Area (m2/g)",
        value=150.0,
        min_value=0.0,
        help="Specific surface area of the catalyst.",
    )

    band_gap = st.number_input(
        "Band Gap (eV)",
        value=2.1,
        min_value=0.0,
        help="Electronic band gap energy.",
    )

    particle_size = st.number_input(
        "Particle Size (nm)",
        value=20.0,
        min_value=0.0,
        help="Average particle size of the catalyst.",
    )


with col2:
    pore_volume = st.number_input(
        "Pore Volume (cm3/g)",
        value=0.6,
        min_value=0.0,
        help="Total pore volume of the catalyst.",
    )

    temperature = st.number_input(
        "Temperature (C)",
        value=40.0,
        help="Reaction temperature.",
    )

    pH = st.number_input(
        "pH",
        value=7.0,
        min_value=0.0,
        max_value=14.0,
        help="Solution pH (0-14).",
    )

    time = st.number_input(
        "Reaction Time (min)",
        value=90.0,
        min_value=0.0,
        help="Duration of the reaction.",
    )


st.divider()


# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------
if st.button(
    "[PREDICT] Predict Activity",
    type="primary",
    use_container_width=True,
):
    try:
        # Encode the selected metal
        metal_encoded = encoder.transform([metal])[0]

        # Create model input
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

        # Generate prediction
        prediction = model.predict(new_data)

        # Display prediction
        st.success(
            f"### Predicted Activity: {prediction[0]:.2f}%"
        )

        # Display input summary
        with st.expander("View Input Summary"):
            st.json(
                {
                    "Metal": metal,
                    "Surface Area (m2/g)": surface_area,
                    "Band Gap (eV)": band_gap,
                    "Particle Size (nm)": particle_size,
                    "Pore Volume (cm3/g)": pore_volume,
                    "Temperature (C)": temperature,
                    "pH": pH,
                    "Reaction Time (min)": time,
                }
            )

    except Exception as e:
        st.error(
            f"An error occurred during prediction: {e}"
        )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.divider()
st.caption("Built with Streamlit | Machine Learning Catalyst Activity Predictor")