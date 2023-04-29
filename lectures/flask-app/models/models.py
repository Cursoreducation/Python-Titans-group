from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        }


articles_categories = db.Table("articles_categories", db.Column("article_id", db.Integer, db.ForeignKey("articles.id")),
                               db.Column("category_id", db.Integer, db.ForeignKey("categories.id")))


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%m:%s")
        }


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    articles = db.relationship("Article", secondary=articles_categories, backref="articles")

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
        }


class MenuItem(db.Model):
    __tablename__ = "menu_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "link": self.link
        }
