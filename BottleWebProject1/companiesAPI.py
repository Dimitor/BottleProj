from bottle import route, post, request, template

@route('/companies')
def companies():
    return template("companies.tpl", title = title, year = year);

