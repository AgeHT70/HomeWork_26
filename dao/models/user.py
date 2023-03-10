from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(512), nullable=False, unique=True)
    password = db.Column(db.LargeBinary, nullable=False)
    name = db.Column(db.String(512))
    surname = db.Column(db.String(512))
    is_locked = db.Column(db.Boolean, default=False)
    favorite_genre = db.Column(db.Integer(), db.ForeignKey('genre.id'))
    genre = db.relationship('Genre')
    # movies = db.relationship('UserMovie', secondary='user_movie')


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    password = fields.Str(load_only=True)
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()

