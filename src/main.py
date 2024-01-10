from server import Server
from config import CONFIG


if __name__ == "__main__":
    server = Server(CONFIG["PORT"])
    server.run()
