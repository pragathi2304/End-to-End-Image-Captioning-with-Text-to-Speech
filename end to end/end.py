import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import streamlit as st
import numpy as np
import pickle
from pathlib import Path
from collections import defaultdict
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.inception_v3 import preprocess_input
from PIL import Image
from gtts import gTTS
from io import BytesIO

# ------------------------
# Load ground-truth captions
# ------------------------
CAPTIONS_FILE = Path("flickr8k_500/captions_500.txt")
captions = defaultdict(list)

with open(CAPTIONS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        if "\t" in line:
            img, cap = line.strip().split("\t", 1)
            captions[img].append(cap.strip())

# ------------------------
# Streamlit UI
# ------------------------
st.title("📜 Ground Truth Caption Viewer + 🎧 Audio")
st.write("Upload an image to view its ground-truth captions and hear one spoken aloud.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Save temporarily
    temp_path = "uploaded_image.jpg"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Match filename to ground-truth captions
    img_name = os.path.basename(uploaded_file.name)
    if img_name in captions:
        st.subheader("📜 Ground Truth Captions:")
        for i, cap in enumerate(captions[img_name], 1):
            st.write(f"{i}. {cap}")

        # Play audio for first ground-truth caption
        gt_caption = captions[img_name][0]
        tts = gTTS(text=gt_caption, lang="en")
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        st.audio(audio_bytes, format="audio/mp3")
    else:
        st.warning("No ground-truth captions found for this image.")