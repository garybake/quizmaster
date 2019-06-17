"""Main package for views."""
from flask import Blueprint

main = Blueprint("main", __name__)

from . import views, errors  # noqa F401, E402
