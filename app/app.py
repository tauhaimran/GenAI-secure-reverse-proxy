# app/app.py
import os
import requests
from flask import Flask, render_template, request, send_from_directory
from io import BytesIO

app = Flask(__name__)

# Environment token (store this securely IRL)
HF_TOKEN = os.environ.get("HF_TOKEN")

# HF API endpoints
IMG_API = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
TTS_API = "https://api-inference.huggingface.co/models/coqui/tts_en_ljspeech"

HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate-image", methods=["POST"])
def generate_image():
    prompt = request.form.get("prompt")
    res = requests.post(IMG_API, headers=HEADERS, json={"inputs": prompt})
    img_path = os.path.join("static", "output", "generated.png")
    with open(img_path, "wb") as f:
        f.write(res.content)
    return render_template("index.html", image_url="/static/output/generated.png")


@app.route("/generate-voice", methods=["POST"])
def generate_voice():
    text = request.form.get("text")
    res = requests.post(TTS_API, headers=HEADERS, json={"inputs": text})
    audio_path = os.path.join("static", "output", "speech.wav")
    with open(audio_path, "wb") as f:
        f.write(res.content)
    return render_template("index.html", audio_url="/static/output/speech.wav")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
