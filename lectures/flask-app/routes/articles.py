from app import app, db
from flask import render_template, request, redirect, session
from models import Article, Category


@app.route("/article/create")
def article_create():
    if session.get("user", {}).get("id", False):
        categories = Category.query.all()
        return render_template("article-create.html", categories=categories)
    else:
        return redirect("/")


@app.route("/article/save", methods=["POST"])
def article_save():
    if session.get("user", {}).get("id", False):
        data = request.form
        article = Article(title=data.get("title"), body=data.get("body"), user_id=int(session.get("user", {}).get("id")))
        db.session.add(article)
        for category_id in data.getlist("categories"):
            category = Category.query.get(int(category_id))
            category.articles.append(article)
            db.session.add(category)
        db.session.commit()
    return redirect("/")


@app.route("/article/<int:id>/delete")
def article_delete(id):
    if session.get("user", {}).get("id", False):
        article = Article.query.get(id)
        if article.user_id == int(session.get("user", {}).get("id")):
            db.session.delete(article)
            db.session.commit()
    return redirect("/")



@app.route("/category/create")
def category_create():
    return render_template("category-create.html")


@app.route("/category/save", methods=["POST"])
def category_save():
    data = request.form
    category = Category(name=data.get("name"), slug=data.get("slug"))
    db.session.add(category)
    db.session.commit()
    return redirect("/")


@app.route("/category/<string:slug>")
def category_details(slug):
    category = Category.query.filter(Category.slug == slug).first()
    return render_template("index.html", articles=category.articles)