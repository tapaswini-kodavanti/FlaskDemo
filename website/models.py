# From __init__.py, import database
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Max length for note is 10,000 characters
    data = db.Column(db.String(10000))

    # Store date; default is current time
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # This is the foreign key; it references the corresponding user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Email is a string with a max length of 150. One user cannot have the same email as another
    email = db.Column(db.String(150), unique=True)
    
    # Max lengths of 150 characters
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    # A list of all of the notes that the user has
    notes = db.relationship('Note')
