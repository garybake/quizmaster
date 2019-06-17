"""Error handlers for flask."""
from flask import render_template

from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    """Return the 404 page on page not found."""
    return render_template("404.html"), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    """Return the 500 page on a server error."""
    return render_template("500.html"), 500
