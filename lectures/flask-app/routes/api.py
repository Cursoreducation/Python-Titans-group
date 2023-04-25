from app import api, db
from models import Article, MenuItem
from flask import request, Response
from flask_restful import Resource


class ArticleResource(Resource):
    def get(self):
        articles = Article.query.all()
        articles_list = []
        for article in articles:
            articles_list.append(article.serialize)
        return articles_list

    def post(self):
        data = request.json
        article = Article(title=data.get("title"), body=data.get("body"))
        db.session.add(article)
        db.session.commit()
        return article.serialize


class ArticleSingleResource(Resource):
    def get(self, id):
        article = Article.query.get(id)
        return article.serialize

    def put(self, id):
        data = request.json
        article = Article.query.get(id)
        article.title = data.get("title")
        article.body = data.get("body")
        db.session.add(article)
        db.session.commit()
        return article.serialize

    def delete(self, id):
        article = Article.query.get(id)
        db.session.delete(article)
        db.session.commit()
        return Response("", status=204)


class MenuItemResource(Resource):
    def get(self):
        menu_items = MenuItem.query.all()
        menu_items_list = []
        for menu_item in menu_items:
            menu_items_list.append(menu_item.serialize)
        return menu_items_list

    def post(self):
        data = request.json
        menu_item = MenuItem(name=data.get("name"), link=data.get("link"))
        db.session.add(menu_item)
        db.session.commit()
        return menu_item.serialize


api.add_resource(ArticleResource, "/api/articles")
api.add_resource(ArticleSingleResource, "/api/articles/<int:id>")
api.add_resource(MenuItemResource, "/api/menu-items")