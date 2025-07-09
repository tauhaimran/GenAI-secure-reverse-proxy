FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install flask
RUN pip install requests

CMD ["python", "app.py"]
# Expose port 5000 for the Flask app
EXPOSE 5000