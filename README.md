
# GenAI Secure Reverse Proxy

This repository contains a secure reverse proxy setup using **Nginx**, **SSL (self-signed)**, and **Docker** to run and serve a containerized web application.

> Includes: Flask app (as an example), reverse proxy, SSL termination, Dockerized setup

---

## 📦 Project Structure

```

.
├── app/                   # Flask or backend application
│   └── ...
├── nginx/
│   └── nginx.conf         # Nginx reverse proxy config
├── docs/
│   ├── app-demo.jpg   
│   └── app-demo.jpg        
├── certs/
│   ├── selfsigned.crt     # SSL certificate
│   └── selfsigned.key     # SSL private key
├── docker-compose.yaml    # Compose config for web + nginx
├──.env                    # Add by yourself for API keys 
└── README.md

````

---

## 🚀 Running Locally

it should look like this when run


### 1. ✅ Generate self-signed SSL cert (if not already there)

```bash
mkdir -p certs
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout certs/selfsigned.key \
  -out certs/selfsigned.crt \
  -subj "/CN=localhost"
````

### 2. ✅ Run the app using Docker Compose

```bash
docker-compose up --build
```

### 3. 🔒 Access the app

Visit:

* [http://localhost](http://localhost) → will redirect to
* [https://localhost](https://localhost) → served securely via Nginx

Expect a **browser warning** because the cert is self-signed.

---

## 🛠️ Features

* ✅ Flask backend (customizable)
* ✅ Nginx reverse proxy
* ✅ HTTPS with self-signed SSL
* ✅ HTTP → HTTPS redirection
* ✅ Runs in Docker

---

## 🧪 Local Testing

After running:

```bash
curl -k https://localhost
```

The `-k` flag tells curl to ignore certificate warnings.

---

## 📁 .env Support

If your app uses `.env` variables, they should be stored in `./app/.env`.

---
