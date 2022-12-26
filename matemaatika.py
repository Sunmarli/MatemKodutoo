from math import *
from random import *
#В программе случайным образом "задаются" примеры, с учетом сложности провряемых знаний.
#После введенного пользователем ответа, проверяется его правильностью.

answers = 5
print("Проверка знаний\n")
Tase=int(input("Choose tase, 1,2 or 3?"))
if Tase==1:
        for i in range (5):
            first=randint(0,10)
            second=randint(0,10)
            tehed=["+","-"]
            tehe_arv=1
            tehe=randint(0,tehe_arv)
            mark=tehed[tehe]
            res=eval(str(first)+mark+str(second))
            print(f"{first}{mark}{second} =", end=" ")
            answer = int(input(""))
            if answer !=res:
                print("Ошибка!")
                answers -= 1
elif Tase==2:
        for i in range (5):
            first=randint(0,100)
            second=randint(0,100)
            res=first-second
            tehed=["+","-","*"]
            tehe_arv=2
            tehe=randint(0,tehe_arv)
            mark=tehed[tehe] 
            print(f"{first}{mark}{second} =", end=" ")
            answer = int(input(""))
            if answer !=res:
                print("Ошибка!")
                answers -= 1
elif Tase==3:
        for i in range (5):
            first=randint(0,100)
            second=randint(0,100)
            res=first*second
            tehed=["+","-","*","/"]
            tehe_arv=3
            tehe=randint(0,tehe_arv)
            mark=tehed[tehe] 
            print(f"{first} {mark} {second} =", end=" ")
            answer = int(input(""))
            if answer !=res:
                print("Ошибка!")
                answers -= 1

print(f"Правильных ответов: {answers}")
 
if 0 <= answers <= 2:
    print("Оценка: плохо")
if 2 <= answers <= 3:
    print("Оценка: хорошо")
if 3 <= answers <= 4:
    print("Оценка: удовлетворительно")
if 4 <= answers <= 5:
    print("Оценка: отлично")
exit = input()