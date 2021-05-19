import json
from bottle import route, post, request
import checkers

@post('/home', method='post')
def add_question():
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

@post('/companies', method='post')
def add_partner():
    companies = []
    with open('companies.json') as f:
        companies = json.load(f)
    name = request.forms.get('COMPANY_NAME').strip()
    if (name == ""):
        return "Name field is empty!"
    descript = request.forms.get('COMPANY_DESCRIPTION').strip()
    if (descript == ""):
        return "Please describe your company and the reasons why you are interested in our university."
    address = request.forms.get('COMPANY_ADDRESS').strip()
    phone = request.forms.get('COMPANY_PHONE').strip()
    if (not checkers.check_phone(phone)):
        if (phone == ""):
            return "Phone field is empty!"
        return "Incorrect phone number!"
    companies.append({
        'name': name,
        'description': descript,
        'address': address,
        'phone': phone
        })
    file = open("companies.json", 'w')
    file.write(json.dumps(companies))
    file.close()
    return "Thank you for your future contribution to Ukhta education!"