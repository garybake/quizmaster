import datetime

from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<user {}>'.format(self.name)

    @classmethod
    def by_id(cls, user_id):
        return cls.query.filter_by(user_id).first()

    # def quizzes_not_attempted(self, id):
    #     return self.model


class Quiz(db.Model):
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<quiz {}>'.format(self.name)


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    quiz = db.relationship('Quiz', backref='questions', lazy=True)

    def __repr__(self):
        return '<question {}>'.format(self.text)


class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64))
    is_correct = db.Column(db.Boolean(), default=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    question = db.relationship('Question', backref='answers', lazy=True)

    def __repr__(self):
        return '<answer {}>'.format(self.text)


class AnswerSelect(db.Model):
    __tablename__ = 'answerselects'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answers.id'))
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user = db.relationship('User', backref='answerselects', lazy=True)
    answer = db.relationship('Answer', backref='answerselects', lazy=True)

    def __repr__(self):
        return '<AnswerSelect {}:{}>'.format(
            self.user.name,
            self.answer.text)
