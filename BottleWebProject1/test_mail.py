import re

reg = re.compile(r'^\S+@\S+(\.\S+)+$')

def check_mail(mail):
	return reg.fullmatch(mail) is not None
