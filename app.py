import cv2
import numpy as np
import streamlit as st
from PIL import Image
import base64

def load_css():
    st.markdown("""
        <style>
        /* Custom font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

        /* General styles */
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f0f2f6;
        }

        h1, h2, h3 {
            color: #333;
            text-align: center;
            font-weight: 600;
        }

        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: 500;
        }

        .stButton>button:hover {
            background-color: #45a049;
        }

        .stFileUploader label {
            font-weight: 500;
            font-size: 1rem;
            color: #333;
        }

        /* Image display */
        .uploaded-image {
            border: 2px solid #ddd;
            border-radius: 10px;
            margin: 10px 0;
        }

        .stImage img {
            border-radius: 10px;
        }

        </style>
        """, unsafe_allow_html=True)

def add_background_image():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://images.unsplash.com/photo-1557683316-973673baf926");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def pencil_sketch(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred_image = 255 - blurred_image
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    return pencil_sketch_image

# Apply custom styles and background
load_css()
add_background_image()

# Title and description
st.title("✨ Picture to Pencil Sketch App ✨")
st.subheader("Transform your photos into beautiful pencil sketches with just a click!")

# Upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the uploaded file to an image
    image = np.array(Image.open(uploaded_file))

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True, channels="RGB")

    # Convert to pencil sketch
    sketch = pencil_sketch(image)

    # Display the pencil sketch
    st.image(sketch, caption="Pencil Sketch", use_column_width=True)

    # Provide a download button for the pencil sketch
    sketch_pil = Image.fromarray(sketch)
    st.download_button(label="📥 Download Pencil Sketch", data=sketch_pil.tobytes(), file_name="pencil_sketch.jpg", mime="image/jpeg")

# Add a footer
st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <small>Developed with ❤️ by VictorCode </small>
    </div>
    """, unsafe_allow_html=True)
