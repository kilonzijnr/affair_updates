from app.models import Sources
from flask import render_template
from .import main
from ..request import get_sources, get_articles

@main.route("/")
def index():
    """
    view root page function"
    """

    Sources = get_sources()
    title = "NEWS BING"

    return render_template("index.html", title=title, Sources=Sources)

@main.route("/articles/<id>")
def articles(id):
    """
    returns the articles
    """

    articles = get_articles(id)
    title = f"{id}"

    return render_template("articles.html", title=title, articles=articles)