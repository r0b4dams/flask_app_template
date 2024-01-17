from server import RestServer
from config import config

from routes.auth import auth_blueprint


if __name__ == "__main__":
    server = RestServer(config, blueprints=[auth_blueprint])
    server.listen()
