from app import create_app, db, models

app = create_app()

with app.app_context():
    db.init_app(app)
    db.drop_all()
    db.create_all()

    admin_user = models.User(name='admin', is_admin=True)
    db.session.add(admin_user)

    quiz1 = models.Quiz(name='Sample Quiz 001')

    question1 = models.Question(text="What is the a of b?", quiz=quiz1)
    answer11 = models.Answer(text="aa", question=question1, is_correct=True)
    answer12 = models.Answer(text="bb", question=question1)
    answer13 = models.Answer(text="cc", question=question1)
    answer14 = models.Answer(text="dd", question=question1)
    db.session.add_all([quiz1, question1, answer11, answer12, answer13, answer14])

    question2 = models.Question(text="What is the c of d?", quiz=quiz1)
    answer21 = models.Answer(text="2aa", question=question2)
    answer22 = models.Answer(text="2bb", question=question2, is_correct=True)
    answer23 = models.Answer(text="2cc", question=question2)
    answer24 = models.Answer(text="2dd", question=question2)
    db.session.add_all([quiz1, question2, answer21, answer22, answer23, answer24])

    quiz2 = models.Quiz(name='Sample Quiz 002')
    db.session.add_all([quiz2])

    # selection1 = models.AnswerSelect(user=admin_user, answer=answer11)
    # selection2 = models.AnswerSelect(user=admin_user, answer=answer23)
    # db.session.add_all([selection1, selection2])

    db.session.commit()

    quiz = models.Quiz.query.first()
    print(quiz.questions)

    # questions = models.Question.query.filter_by(quiz=quiz).all()
    
    # answered = models.Question.query.filter_by(quiz=quiz).all()