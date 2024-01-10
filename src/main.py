from server import Server
from config import CONFIG


if __name__ == "__main__":
    server = Server(CONFIG["MODE"], CONFIG["HOST"], CONFIG["PORT"])
    server.run()
