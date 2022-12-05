from math import *
from random import *
#Töö "Vigade otsing -2"
print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a=(abs(int(input("Введите целое число => "))))
        break
    except ValueError:
         print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c=b=a
    paaris=0
    paaritu=0
    while b>0:
        if b%2==0:
            paaris+=1
        else:
            paaritu+=1
        b//=10
    print("Чётных цифр:",paaris)
    print("Нечётных цифр:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a>0:
        number=a%10
        a=a//10
        b=b*10
        b+=number
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз")
    print()
    if c%2==0:
        print(c, "- чётное число. Делим на 2.")
    else:
        print(c, "- нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c!=1:
            if c%2==0:
                c=c/2
            else:
                c=(3*c+1)/2
            print(int(c), end=" ")
    print()
    print("Гипотеза верна")

#taabel while
r=0
c=0
while r<10:
    r+=1
    while c<10:
        c+=1
        print(str(r*c).center(4), end="")
    c=0
    print()#/n
#taabel for
for r in range(1,11):
    for c in range(1,11):
        print(str(r*c).center(4), end="")
    print()
print()
#Ввести с клавиатуры 10 пар чисел.  Сравнить числа в каждой паре и напечатать большие из них.
text=""
for i in range(1,11):
    arv1=randint(-100,100)
    arv2=randint(-100,100)
    if arv1>arv2:
        print(f"{arv1} on suurem kui {arv2}")
        text+=""+str(arv1)
    elif arv2>arv1:
        print(f"{arv2} on suurem kui {arv1}")
        text+=""+str(arv2)
    else:
        print(f"{arv1},{arv2} on võrdsed")
print(text)
#12
N=int(input("Sisesta kogus: "))
m=int(input("Sisesta aeg(min): "))
m*=60
summa=0
for i in range(1,N):
    summa+=m
    m+=10
print("Kokku nad töötavad: ",summa/60, "min")
#Напишите программу, печатающую столбик строк такого вида:
for j in range(9):
    for i in range(9):
        if j==i:
            print(j+1, end=" ")
        else:
            print(0, end=" ")
    print()
print()
#Напишите программу, печатающую столбик таблицу умножения такого вида:
print("Таблица умножения")
n = int(input('Введите n: '))
for i in range(1, 11):
    print(f'{n} * {i} = {n*i}')
#Даны натуральные числа от 1 до 50. Найти сумму тех из них, которые делятся на 5 или на 7.
a=0
for i in range (1,51):
    if i %7==0 or i %5==0:
        a+=i
print(a)
#Найти сумму чисел от 100 до 200, кратных 17
summ=0
a=100
while a<=200:
    if a%17==0:
        summ+=a
    a+=1
print(summ)
#Вводят 8 чисел. Найти их произведение (только положительных).
i=0
j=0
while i<8:
    i+=1
    a=float(input(f"{i} Sisesta A: "))
    if int(a)>0: 
        j=i*i*i*i*i*i*i*i
print(j)
#Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.
n=int(input("Sisesta arv: "))
j=0
for i in range(1,n+1):
    j+=i
print(j)
#В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?
S=float(input("Panusesumma: "))
N=float(input("Aeg:  ", ))
a=S+S*0.03*N
print("Panusesumma kokku", a)
#Вводят 15 чисел. Определить, сколько среди них целых.
j=0
i=0
while i<15:
    i+=1
    a=float(input(f"{i} Sisesta A: "))
    if int(a)==a: j+=1 
print(j)
