from flask import Flask
from flask_cors import CORS

from routes.auth import auth_blueprint


class Server:
    def __init__(self, mode: str, host: str, port: int):
        self.app = Flask(__name__)
        self.mode = mode
        self.host = host
        self.port = port
        self.load_blueprints()
        CORS(self.app)

    def load_blueprints(self):
        self.app.register_blueprint(auth_blueprint)

    def run(self):
        if self.mode == 'production':
            print('TODO - implement production server')
        else:
            self.app.run(debug=True, port=self.port, host=self.host)
