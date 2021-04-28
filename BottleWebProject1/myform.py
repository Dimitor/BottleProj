from bottle import post, request, re

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
    matchres = re.findall(r"^\S+@\S+(\.\S+)+$", mail)
    if (len(matchres) == 0 or matchres[0] == None):
        return "Your mail have invalid format"
    questions[mail] = question
    data['questions'].append({
        'question': question,
        'mail': mail
    })
    with open('questions.txt', 'a') as outfile:
        json.dump(data, outfile)
    return "Thanks! The answer will be sent to the mail %s" % mail

