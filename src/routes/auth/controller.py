import flask


class AuthController:
    def __init__(self) -> None:
        pass

    def callback(self) -> flask.Response:
        status_code = 200
        response = {
            "GET": "callback"
        }
        return flask.make_response(response, status_code)

    def login(self) -> flask.Response:
        status_code = 200
        response = {
            "GET": "login"
        }
        return flask.make_response(response, status_code)

    def logout(self) -> flask.Response:
        status_code = 200
        response = {
            "GET": "logout"
        }
        return flask.make_response(response, status_code)

    def refresh(self) -> flask.Response:
        status_code = 200
        response = {
            "POST": "refresh"
        }
        return flask.make_response(response, status_code)

    def register(self) -> flask.Response:
        status_code = 200
        response = {
            "GET": "register"
        }
        return flask.make_response(response, status_code)

    def user(self) -> flask.Response:
        status_code = 200
        response = {
            "GET": "user"
        }
        return flask.make_response(response, status_code)
