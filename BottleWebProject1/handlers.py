import json
from bottle import route, post, request
import checkers

@post('/home', method='post')
def my_form():
    questions = {}
    data = {}
    data['questions'] = []
    question = request.forms.get('QUEST').strip()
    mail = request.forms.get('ADRESS').strip()
    if (question == ""):
        return "Question field is not filled"
    if (mail == ""):
        return "Mail field is not filled"
    if (not test_mail.check_mail(mail)):
        return "Your mail have invalid format"
    questions[mail] = question
    data['questions'].append({
        'question': question,
        'mail': mail
    })
    with open('questions.txt', 'a') as outfile:
        json.dump(data, outfile)
    return "Thanks! The answer will be sent to the mail %s" % mail
