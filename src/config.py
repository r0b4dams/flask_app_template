import os

CONFIG = {
    "MODE": os.environ.get("MODE", "development"),
    "HOST": os.environ.get("HOST", "localhost"),
    "PORT": os.environ.get("PORT", 9000)
}
