FROM python:3.10-slim

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask python-dotenv google-generativeai

CMD ["python", "app.py"]

# Expose the port the app runs on
EXPOSE 5000