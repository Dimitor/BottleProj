import re

def check_mail(mail):
	reg = re.compile("^\w+@(\w+\.)+\w{2,3}$")
	return reg.fullmatch(mail) is not None

def check_phone(phone):
	reg = re.compile("^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$")
	return reg.fullmatch(phone) is not None
