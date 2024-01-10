from flask import Flask
from routes.auth import auth_blueprint


class Server:
    def __init__(self) -> None:
        self.app = Flask(__name__)

    def load_blueprints(self):
        self.app.register_blueprint(auth_blueprint)

    def run(self):
        self.load_blueprints()
        self.app.run(debug=True)
