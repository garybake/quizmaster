"""Holds Quiz model."""

from .. import db


class Quiz(db.Model):
    """Model to hold quizzes."""

    __tablename__ = "quizzes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        """Return string readable version of model."""
        return "<quiz {}>".format(self.name)

    @property
    def question_count(self):
        """Return number of questions quiz has."""
        return len(self.questions)
