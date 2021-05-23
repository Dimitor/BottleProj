from bottle import route, post, request, template
import json
import checkers

@route('/companies')
def companies():
    return template("companies.tpl", title = title, year = year); # отображение страницы company

@post('/companies', method='post')
def add_partner(): # метод добавления партнёра
    companies = []
    with open('companies.json') as f: # чтение данных
        companies = json.load(f)
        # проверка введённых данных
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
    # добавление новой записи
    companies.append({
        'name': name,
        'description': descript,
        'address': address,
        'phone': phone
        })
    # запись записей в файл
    file = open("companies.json", 'w')
    file.write(json.dumps(companies))
    file.close()
    return "Thank you for your future contribution to Ukhta education!"

