from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
print(f"Using Gemini API key: {api_key}")


models = genai.list_models()
for m in models:
    print(m.name, "-", m.supported_generation_methods)

# Load model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            prompt = request.form.get("input_value", "")
            response = model.generate_content(prompt)
            result = response.text
        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
# This is the main entry point for the Flask application.
# It initializes the app, configures the Gemini API, and defines the main route.