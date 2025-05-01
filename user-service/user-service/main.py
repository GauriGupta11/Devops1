# user-service/main.py

from flask import Flask

def main():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello from User Service!"

    app.run(debug=True)
