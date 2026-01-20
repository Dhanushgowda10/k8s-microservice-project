from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Kubernetes Microservice Running",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "dev")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
