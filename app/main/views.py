from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from . import main
from ..models import Blog, User, Comment
from .forms import BlogForm, CommentForm
from .. import db
from ..requests import get_quotes

# Views
@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    title = "Home - Blog"

    quote = get_quotes()
    return render_template("index.html", quote=quote)

@main.route("/blogs")
@main.route("/blogs/<category>")
def blogs(category=None):


    """
    View root page function that returns the index page and its data
    """
    if not category:
        blogs = Blog.query.all()
    else:
        blogs = Blog.query.filter_by(category=category)

    return render_template("blogs.html", category=category, blogs=blogs)




