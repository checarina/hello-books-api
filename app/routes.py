from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

@hello_world_bp.route("/hello/JSON", methods = ["GET"])
def say_hello_json():
    return {
        "name": "Carina",
        "message": "Hello!",
        "hobbies": ["Reading", "Crosswords", "Video games"]
    }