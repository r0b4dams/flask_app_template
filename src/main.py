#!/usr/bin/env python

from server import RestServer
from config import config
from routes import blueprints


if __name__ == "__main__":
    server = RestServer(config, blueprints)
    server.listen()
