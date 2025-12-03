import streamlit as st
from PIL import Image
import numpy as np

from model.segmentation import SegmentationModel
from model.sky_generation import SkyGenerator
from model.color_grading import apply_twilight_tone
from model.lighting import add_window_light
from model.utils import mask_to_pil

st.set_page_config(page_title="Real Estate Twilight Converter", layout="wide")
st.title("🏡 AI Real Estate Twilight Converter")

uploaded_file = st.file_uploader("Upload a daytime exterior photo", type=["jpg","png","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Original Daytime Image", use_column_width=True)

    if st.button("Convert to Twilight"):
        with st.spinner("Processing..."):
            # Initialize models
            seg_model = SegmentationModel()
            sky_gen = SkyGenerator()

            # Step 1: Segmentation
            masks = seg_model.segment_image(image)
            sky_mask = mask_to_pil(masks["sky"])
            window_mask = masks["windows"]

            # Step 2: Generate Twilight Sky
            twilight_image = sky_gen.generate_twilight_sky(image, sky_mask)

            # Step 3: Color Grading
            graded_image = apply_twilight_tone(twilight_image)

            # Step 4: Add window/exterior lights
            final_image = add_window_light(graded_image, window_mask)

            st.image(final_image, caption="Twilight Image", use_column_width=True)
            st.success("Conversion Complete!")
