from app import db
from app.models.book import Book 
from app.models.author import Author
from flask import Blueprint, jsonify, abort, make_response, request

books_bp = Blueprint("books", __name__, url_prefix = "/books")
authors_bp = Blueprint("authors", __name__, url_prefix = "/authors")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
    
    return model

@books_bp.route("", methods = ["GET"])
def get_all_books():
    title_query = request.args.get("title")
    if title_query:
        books = Book.query.filter_by(title = title_query)
    else:
        books = Book.query.all()

    books_response = []
    for book in books:
        books_response.append(book.to_dict())
    return jsonify(books_response)

@books_bp.route("/<model_id>", methods = ["GET"])
def get_one_book(model_id):
    book = validate_model(Book, model_id)
    return book.to_dict()

@books_bp.route("", methods = ["POST"])
def create_book():
    request_body = request.get_json()
    # new_book = Book(title = request_body["title"], description = request_body["description"])
    new_book = Book.from_dict(request_body)
    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} successfully created"), 201)

@books_bp.route("/<model_id>", methods = ["PUT"])
def update_book(model_id):
    book = validate_model(Book, model_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(jsonify(f"Book #{model_id} successfully updated."), 200)

@books_bp.route("/<model_id>", methods = ["DELETE"])
def delete_book(model_id):
    book = validate_model(Book, model_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify(f"Book #{model_id} successfully deleted."), 200)

# Author routes

@authors_bp.route("", methods = ["GET"])
def get_all_authors():
    name_query = request.args.get("name")
    if name_query:
        authors = Author.query.filter_by(name = name_query)
    else:
        authors = Author.query.all()

    authors_response = []
    for author in authors:
        authors_response.append(author.name)
    return jsonify(authors_response)

@authors_bp.route("/<model_id>", methods = ["GET"])
def get_one_author(model_id):
    author = validate_model(Author, model_id)
    return jsonify({"name": author.name})

@authors_bp.route("", methods = ["POST"])
def create_author():
    request_body = request.get_json()
    new_author = Author(name = request_body["name"])
    
    db.session.add(new_author)
    db.session.commit()

    return make_response(jsonify(f"Author {new_author.name} successfully added"), 201)

@authors_bp.route("/<author_id>/books", methods = ["POST"])
def create_book(author_id):
    author = validate_model(Author, author_id)

    request_body = request.get_json()
    new_book = Book(
        title = request_body["title"],
        description = request_body["description"],
        author = author
    )

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} by {new_book.author.name} successfully created"), 201)
