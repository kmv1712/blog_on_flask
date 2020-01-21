from app import db
from datetime import datetime
import re


def slugify(s):
    """Генерация sluga.

    Args:
        s(str): Строка.

    Returns:
        str
    """
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


# Добавляем табличку для реализации связи многие ко многим для таблиц Post и Tag
post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    # Выстроим отношение с Tag
    # relationship(название т. с которой выстраиваем связь, название т. через которую выстр-ем связь,
    # назание поля возникающее в связаной таблице)
    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Tag id: {}, name: {}'.format(self.id, self.name)

