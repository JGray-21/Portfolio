#This is my calculator :)


f = open("history.py", "w")
g = open("history.py", "r")
def add(num1, num2):
	if num1 == 'ans': 
		num1 = g.read()
		print("num1 = " + num1)
	if num2 == 'ans': num2 = g.read()
	#f.write(str(float(num1) + float(num2)))
	return float(num1) + float(num2)

def sub(num1, num2):
	f.write(str(float(num1) - float(num2)))
	return float(num1) - float(num2)

def mul(num1, num2):
	f.write(str(float(num1) * float(num2)))
	return float(num1) * float(num2)

def div(num1, num2):
	f.write(str(float(num1) / float(num2)))
	return float(num1) / float(num2)

while True:
	math = input('>')

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

f.close()
g.cloes()
