End-to-End Image Captioning with Text-to-Speech

An end-to-end deep learning system that automatically generates captions for images and converts them into spoken audio, designed to improve accessibility for visually impaired users. The project combines Computer Vision and Natural Language Processing (NLP) using a CNN–LSTM Encoder–Decoder architecture with real-time Text-to-Speech (TTS).

🚀 Features
CNN-based Feature Extraction: Uses pre-trained models (VGG16 / InceptionV3) to extract rich visual features from images
LSTM Caption Generator: Produces grammatically correct and context-aware image captions
Text-to-Speech (gTTS): Converts generated captions into natural-sounding audio
End-to-End Pipeline: Image → Text → Speech with low latency
Model Evaluation: Trained on Flickr8k and evaluated using BLEU, METEOR, and CIDEr scores
Scalable Architecture: Easily extendable with attention mechanisms, transformers, or multilingual TTS

🧠 Tech Stack
Programming Language: Python
Deep Learning: TensorFlow / Keras
Models: CNN (VGG16/InceptionV3), LSTM
NLP & Utils: NLTK, NumPy
Visualization: Matplotlib
TTS: Google Text-to-Speech (gTTS)

📊 Dataset
Flickr8k – 8,000 images with 40,000 human-annotated captions

⚙️ How It Works
Input image is preprocessed and passed through a CNN encoder
Extracted features are fed into an LSTM decoder
Caption is generated word-by-word
Final caption is converted into speech using gTTS

📈 Results
Strong caption quality with competitive BLEU & CIDEr scores
Fast inference suitable for real-time applications
Seamless integration of captioning and audio output

🔮 Future Enhancements

Add attention mechanisms for better region-focused captions
Replace LSTM with Transformer-based decoders
Enable multilingual captioning and speech output
Upgrade TTS to neural speech models (Tacotron / FastSpeech)
