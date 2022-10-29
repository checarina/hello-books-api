from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Pride and Prejudice", "my favorite"),
    Book(2, "The Two Towers", "the beacons are lit, Gondor calls for aid"),
    Book(3, "The Life-Changing Magic of Tidying Up", "sparks joy")
] 

hello_world_bp = Blueprint("hello_world", __name__)
books_bp = Blueprint("books", __name__, url_prefix = "/books")

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

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby) #fixed
    return response_body

@books_bp.route("", methods = ["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)