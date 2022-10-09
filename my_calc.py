#This is my calculator :)


g = open("history.txt", "r")

def add(num1, num2):
    if num1.rstrip() == 'ans':
        num1 = g.read()
    if num2.rstrip() == 'ans':
        num2 = g.read()

    f = open("history.txt", "w")
    f.write(str(float(num1) + float(num2)))
    f.close()
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

g.close()
