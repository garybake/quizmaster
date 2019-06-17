"""Holds Answer model."""

from .. import db


class Answer(db.Model):
    """Model to hold answers to questions."""

    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64))
    is_correct = db.Column(db.Boolean(), default=False)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))
    question = db.relationship("Question", backref="answers", lazy=True)

    def __repr__(self):
        """Return string readable version of model."""
        return "<answer {}>".format(self.text)
