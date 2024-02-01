from flask import Blueprint, Flask
from gunicorn.app.base import BaseApplication


class Server(BaseApplication):
    """
    Top-level class managing the application. Extends the BaseApplication class provided by Gunicorn.
    """

    def __init__(self, config: dict[str, str] = {}, blueprints: list[Blueprint] = []):
        self.app = Flask(__name__)
        self.config = config
        self.register_blueprints(blueprints)
        super().__init__()

    def listen(self):
        """
        Start the server and run forever. 

        Runs the gunicorn WSGI server in production,
        else runs the Flask dev server
        """
        if self.config['mode'] == 'production':
            self.run()
        else:
            self.app.run(
                debug=True,
                host=self.config['host'],
                port=self.config['port']
            )

    def load(self):
        """
        Used by BaseApplication to access the Flask app
        """
        return self.app

    def load_config(self):
        """
        Pass config options to BaseApplication
        """
        # filter valid gunicorn properties
        gunicorn_config = {
            key: value for key, value in self.config.items()
            if key in self.cfg.settings and value is not None
        }

        # set config on BaseApplication
        for key, value in gunicorn_config.items():
            self.cfg.set(key.lower(), value)

    def register_blueprints(self, blueprints: list[Blueprint]):
        """
        Register Flask blueprints with the app
        """
        for blueprint in blueprints:
            self.app.register_blueprint(blueprint)
