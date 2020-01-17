from app import db
from datetime import datetime
import re


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body
    created

    def generate_slug(self):
        if self.title == self.slug:
            self.slug = slugify(self.title)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.slug = generate_slug()

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)

