import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Read values from environment variables
    greeting_message = os.getenv("GREETING_MESSAGE", "Hello, World!")
    secret_key = os.getenv("SECRET_KEY", "No Secret Key Found")

    return f"{greeting_message} - Secret Key: {secret_key}"

@app.route('/healthz', methods=['GET'])
def health_check():
    # You can add checks here to verify if the app is fully functional, like database connectivity, etc.
    return 'OK', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
