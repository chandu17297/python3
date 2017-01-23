import string
import random

def pwdgen(size=8,chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pwdgen(int(input('password size?'))))