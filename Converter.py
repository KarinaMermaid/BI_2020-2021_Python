print ('This converter is foк converting Fahrenheit to Celsius and vice versa, Celsius to Fahrenheit')

while True:
    number = int(input())
    from_what_convert = str(input('Enter F or C:'))
    to_what_convert = str(input('Enter F or C:'))
    if from_what_convert == 'F' and to_what_convert == 'C':
        print(round( (number * (9/5) + 32), 2))
        break
    elif from_what_convert == 'C' and to_what_convert == 'F':
        print( round(((number - 32) * 5/9), 2))
        break
    elif from_what_convert == 'F' and to_what_convert == 'F' or from_what_convert == 'C' and to_what_convert == 'F':
        print ('There is nothing to convert. Try again')
        continue
    else :
        print ('You did something wrong. Try again')
        continue

