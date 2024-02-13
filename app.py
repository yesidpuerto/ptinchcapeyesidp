from flask import Flask, render_template, request
import requests
from config import Config  # Importa la clase Config desde el archivo config.py

app = Flask(__name__)

@app.route("/")
def index():
    try:
        response = requests.get(Config.API_URL)  # Utiliza la variable de configuración API_URL
        posts = response.json()
        return render_template("posts.html", posts=posts)
    except requests.exceptions.RequestException as e:
        return render_template("error.html", error_message=f"Error fetching posts: {e}")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
