import streamlit as st
import requests
import io
from PIL import Image

st.set_page_config(page_title="Image Generation App", layout="wide")

# Function to load and display the logo
def load_logo():
    logo = Image.open("logo.png")
    return logo

# Display logo
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(load_logo(), width=150)

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


def generate_image(prompt):
    image_bytes = query({
        "inputs": prompt,
    })
    image = Image.open(io.BytesIO(image_bytes))
    image.save("astronaut_riding_horse.png")
    return None

with col2:

    st.title("Image Generation App")

# Text input for the image prompt
    prompt = st.text_input("Enter a prompt for image generation:", "Astronaut riding a horse")

    if st.button("Generate Image"):
        with st.spinner("Generating image..."):
            generate_image(prompt)
            image=Image.open('astronaut_riding_horse.png') 
            st.image(image, caption=prompt, use_column_width=True)

    st.write("Note: Image generation may take a few seconds.")