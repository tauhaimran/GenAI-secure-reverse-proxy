# 🔒 GenAI Secure Reverse Proxy

A containerized Flask web application that integrates with an external **API**, secured using **Nginx** reverse proxy and **SSL**, and orchestrated with **Docker Compose**.

> 🧰 A practical DevOps project featuring API consumption, containerization, secure traffic routing, and deployment automation.

---

## 🚀 Live Demo & Blog

- 🌐 **Live App**: [https://genai-proxy.up.railway.app](https://genai-proxy.up.railway.app) *(Hosted on Railway)*
- 📝 **Blog Post**: [How I Built a Secure Reverse Proxy with Nginx, Docker & SSL](#) *(Coming soon)*

---

## 📸 Screenshot

<p align="center">
  <img src="docs/app-demo.jpg" alt="App Screenshot" width="700"/>
</p>

---

## 📦 Project Structure

.
├── app/ # Flask or backend application
│ └── ...
├── nginx/
│ └── nginx.conf # Nginx reverse proxy config
├── docs/
│ └── app-demo.jpg # Screenshot/demo image
├── certs/
│ ├── selfsigned.crt # SSL certificate
│ └── selfsigned.key # SSL private key
├── docker-compose.yaml # Compose config for web + nginx
├── .env # Not included — provide your own API keys
└── README.md

yaml
Copy
Edit

---

## 🔧 Tech Stack

- 🐍 **Flask** – Lightweight Python web app
- 🐳 **Docker** – Containerized setup for portability
- 🌐 **Nginx** – Acts as secure reverse proxy
- 🔐 **SSL** – Self-signed certs for HTTPS
- ⚙️ **Docker Compose** – Multi-service orchestration
- ☁️ **Railway** – Cloud hosting & deployment

---

## 🛠️ Features

- ✅ Flask app fetches data from an external API
- ✅ Reverse proxy via Nginx
- ✅ HTTPS support with self-signed certs
- ✅ Auto-redirect HTTP → HTTPS
- ✅ Fully containerized with Docker
- ✅ Ready for production deployment

---

## 🧪 Running Locally

### 1. Generate a self-signed SSL certificate

```bash
mkdir -p certs
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout certs/selfsigned.key \
  -out certs/selfsigned.crt \
  -subj "/CN=localhost"
2. Start the app with Docker Compose
bash
Copy
Edit
docker compose up --build
3. Access locally
Visit: http://localhost → redirects to

Secure: https://localhost

Expect a browser warning for the self-signed cert — it's safe to continue.

🧪 Testing via Curl
bash
Copy
Edit
curl -k https://localhost
The -k option skips SSL verification (needed for self-signed certs).

🗂️ .env Support
Add your API keys or configs inside a .env file in the root (not committed).
Example:

ini
Copy
Edit
API_KEY=your_api_key_here
FLASK_ENV=development
📄 License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Built by Tauha Imran
Connect on LinkedIn