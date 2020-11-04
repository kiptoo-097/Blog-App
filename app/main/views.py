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


