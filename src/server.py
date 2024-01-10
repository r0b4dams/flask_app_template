from flask import Flask
from routes.auth import auth_blueprint


class Server:
    def __init__(self, port) -> None:
        self._port = port
        self._app = Flask(__name__)
        self._load_blueprints()

    def _load_blueprints(self):
        self._app.register_blueprint(auth_blueprint)

    def run(self):
        self._app.run(debug=True, port=self._port)
