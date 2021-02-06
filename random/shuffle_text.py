# Сделайте программу, получающую на вход текст, и выдающую этот же текст со следующими изменениями - буквы во всех словах
# кроме первой и последней перемешаны. Для простоты пока будем считать, что пунктуации нет

import random

inp = input().split()
for s in inp:
    result = s
    space = ' '
    if s == inp[-1]:
        space = ''

    if len(s) > 3:
        l = list(s[1:-1])
        random.shuffle(list(s[1:-1]))
        result = s[0] + ''.join(l) + s[-1]

    print(result, end=space)