import re

reg = re.compile("^[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Za-z0-9]+)+$")

def check_mail(mail):
	return reg.fullmatch(mail) is not None
