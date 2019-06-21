import os
from post import Post
import datetime
from app import create_app, db

app = create_app('production')

if __name__ == '__main__':
    app.app_context().push()
    db.session.query(Post).delete()
    posts = []
    for i in range(0, 100000):
        posts.append(Post({
            'id': i,
            'location': 'location',
            'latitude': 124.2,
            'description': 'text',
            'content_total_value': 10,
            'featured': 0,
            'longitude': 125.2,
            'parent_post_id': 0
        }))

    db.session.bulk_save_objects(posts)
    db.session.commit()
    print('END')
