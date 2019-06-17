"""Holds Question model."""

from .. import db


class Question(db.Model):
    """Model to hold Questions."""

    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64))
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizzes.id"))
    quiz = db.relationship("Quiz", backref="questions", lazy=True)

    def __repr__(self):
        """Return string readable version of model."""
        return "<question {}>".format(self.text)
