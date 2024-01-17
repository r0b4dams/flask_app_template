from flask import Blueprint, Flask
from gunicorn.app.base import BaseApplication


class RestServer(BaseApplication):
    """
    RestServer is the top level class managing the application. For ease of deployment,
    it extends the BaseApplication class provided by Gunicorn.
    """

    def __init__(self, config: dict[str, str] = {}, blueprints: list[Blueprint] = []):
        self.app = Flask(__name__)
        self.config = config
        self.register_blueprints(blueprints)
        super().__init__()

    def listen(self):
        """
        Start the server and run forever.

        In production mode, runs the Gunicorn WSGI server.
        Otherwise, runs the Flask app dev server
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
        Returns the Flask application instance so BaseApplication can use it
        """
        return self.app

    def load_config(self):
        """
        Pass the config properties to the BaseApplication Config instance.
        """
        # filter valid gunicorn properties
        gunicorn_config = {
            key: value for key, value in self.config.items()
            if key in self.cfg.settings and value is not None
        }
        # set properties with the Config set method
        for key, value in gunicorn_config.items():
            self.cfg.set(key.lower(), value)

    def register_blueprints(self, blueprints):
        """
        Registers blueprints with the Flask application
        """
        for blueprint in blueprints:
            self.app.register_blueprint(blueprint)
