import re

def check_mail(mail):
	reg = re.compile("^\w+@(\w+\.)+\w{2,3}$")
	return reg.fullmatch(mail) is not None

def check_phone(phoone):
	reg = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
	return re.search(reg, phone)
