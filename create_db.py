"""Create the database for quizzes.

Create an admin users
Creates 10x quizzes with 5x questions and 4x answers each
(Answer 3 will be the correct answer
TODO: is it easier to jumble the answers during render)
"""
from app import create_app, db, models

app = create_app()

QUIZ_COUNT = 10
QUESTIONS_PER_QUIZ = 5
ANSWERS_PER_QUESTION = 4

with app.app_context():
    db.init_app(app)
    db.drop_all()
    db.create_all()

    admin_user = models.User(name="admin@example.com", is_admin=True)
    db.session.add(admin_user)
    db.session.commit()

    for qz in range(QUIZ_COUNT):
        commit_list = []
        quiz = models.Quiz(name="Sample Quiz {}".format(qz))
        commit_list.append(quiz)

        questions = []
        for qs in range(QUESTIONS_PER_QUIZ):
            question = models.Question(
                text="What is the {} of {}?".format(qz, qs), quiz=quiz)
            commit_list.append(question)
            for ans in range(ANSWERS_PER_QUESTION):
                correct = (ans == 2)
                answer = models.Answer(
                    text="ans {}_{}_{}".format(qz, qs, ans), question=question,
                    is_correct=correct)
                commit_list.append(answer)

        db.session.add_all(commit_list)
        db.session.commit()
