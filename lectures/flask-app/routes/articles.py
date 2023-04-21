from app import app, db
from flask import render_template, request, redirect
from models import Article


@app.route("/article/create")
def article_create():
    return render_template("article-create.html")


@app.route("/article/save", methods=["POST"])
def article_save():
    data = request.form
    article = Article(title=data.get("title"), body=data.get("body"))
    db.session.add(article)
    db.session.commit()
    return redirect("/")


@app.route("/article/<int:id>/delete")
def article_delete(id):
    article = Article.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return redirect("/")