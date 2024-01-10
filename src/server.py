from flask import Flask
from routes.auth import auth_blueprint


class Server:
    def __init__(self, port) -> None:
        self.app = Flask(__name__)
        self.port = port
        self.load_blueprints()

    def load_blueprints(self):
        self.app.register_blueprint(auth_blueprint)

    def run(self):
        self.app.run(debug=True, port=self.port)
