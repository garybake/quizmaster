from .. import db


class User(db.Model):
    """Model for storing users."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<user {}>'.format(self.name)

    @property
    def by_id(cls, user_id):
        return cls.query.filter_by(user_id).first()
