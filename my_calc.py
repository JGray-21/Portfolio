#This is my calculator :)

def add(num1, num2):
	return int(num1) + int(num2)
def sub(num1, num2):
	return int(num1) - int(num2)
def mul(num1, num2):
	return int(num1) * int(num2)
def div(num1, num2):
	return int(num1) / int(num2)

while True:
	math = input('>  ')

	if math.find('+') >= 0:
		ans = add(math[:math.find('+')], math[math.find('+')+1:])
		print(ans)

	elif math.find('-') >= 0:
		ans = sub(math[:math.find('-')], math[math.find('-')+1:])
		print(ans)

	elif math.find('*') >= 0:
		ans = mul(math[:math.find('*')], math[math.find('*')+1:])
		print(ans)

	elif math.find('/') >= 0:
		ans = div(math[:math.find('/')], math[math.find('/')+1:])
		print(ans)

	elif math.find('exit') >= 0:
		break

	else: print('Please enter valid opperation.')
