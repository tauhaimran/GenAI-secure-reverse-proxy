# app/app.py
import os
import requests
import markdown
from flask import Flask, render_template, request
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"

@app.route("/", methods=["GET", "POST"])
def index():
    response_html = None
    error = None

    if request.method == "POST":
        user_input = request.form.get("prompt")
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{"parts": [{"text": user_input}]}]
        }
        url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"
        
        try:
            res = requests.post(url, headers=headers, json=payload)
            if res.status_code == 200:
                raw_text = res.json()["candidates"][0]["content"]["parts"][0]["text"]
                response_html = markdown.markdown(raw_text)
            else:
                error = f"Error {res.status_code}: {res.text}"
        except Exception as e:
            error = str(e)

    return render_template("index.html", result=response_html, error=error)

if __name__ == "__main__":
    app.run(debug=True)
# app/templates/index.html