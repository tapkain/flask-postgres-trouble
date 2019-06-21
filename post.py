import datetime
from app import db
from sqlalchemy.dialects import postgresql
import enum


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self, data):
        self.id = data.get('id')
