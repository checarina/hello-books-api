from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", back_populates = "books")

    def to_dict(self):
        book_dict = {}

        book_dict["id"] = self.id
        book_dict["title"] = self.title
        book_dict["description"] = self.description

        return book_dict
    
    @classmethod
    def from_dict(cls, book_data):
        #Initialize an instance of Book with the title and description from book_data
        #and with an id generated as usual for the Book class
        #return the Book instance
        return Book(title = book_data["title"], description = book_data["description"])