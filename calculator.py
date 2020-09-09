number1= int(input('Enter a number: ' ))
operand = input('Enter an operand ')
number2= int(input('Enter a number '))

if number2 == 0 and (operand == "mod" or operand == "/" or operand == "div"):
    print("division by zero")
elif operand == '+':
    print(number1 + number2)
elif operand == '-':
    print(number1 - number2)
elif operand == '*':
    print(number1 * number2)
elif operand == '/':
    print(number1 / number2)
elif operand == 'mod':
    print(number1 % number2)
elif operand == 'pow':
    print(number1 ** number2)
elif operand == 'div':
    print(number1 // number2)
else: 
  print("Unknown operator")
