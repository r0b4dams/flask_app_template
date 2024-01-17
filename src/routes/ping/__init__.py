import flask

ping_blueprint = flask.Blueprint("ping", __name__, url_prefix="/ping")


@ping_blueprint.route("/", methods=["GET"])
def ping():
    status_code = 200
    response = "pong"
    return flask.make_response(response, status_code)
