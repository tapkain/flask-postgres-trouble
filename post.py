import datetime
from app import db
from sqlalchemy.dialects import postgresql
import enum


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_post_id = db.Column(db.Integer, db.ForeignKey(
        id), nullable=True)

    description = db.Column(db.Text)
    location = db.Column(db.String(255), nullable=True)
    latitude = db.Column(postgresql.DOUBLE_PRECISION, nullable=True)
    longitude = db.Column(postgresql.DOUBLE_PRECISION, nullable=True)
    featured = db.Column(db.SmallInteger, nullable=True)
    content_total_value = db.Column(postgresql.DOUBLE_PRECISION, nullable=False, default=0.0)
    scheduled_date = db.Column(db.TIMESTAMP, nullable=True)

    def __init__(self, data):
        self.id = data.get('id')
        self.user_id = data.get('user_id')
        self.parent_post_id = data.get('parent_post_id')
        self.description = data.get('description')
        self.location = data.get('location')
        self.latitude = data.get('latitude')
        self.longitude = data.get('longitude')
        self.featured = data.get('featured', None)
        self.content_total_value = data.get('content_total_value', 0)
        self.created_at = data.get('created_at', datetime.datetime.utcnow())
        self.scheduled_date = data.get('scheduled_date', None)
