import math
from random import randint

def zad1():
    a = [1-x for x in range(1,10)]
    b = [4**x for x in range(8)]
    c = [x for x in b if x%2 == 0]
    print(a)
    print(b)
    print(c)

def zad2():
    a = []
    for i in range(0,10):
        x = randint(1,100)
        a.append(x)


    b = [x for x in a if x%2 == 0]
    print(b)
zad2()

def zad3():
    slownik_zakupow = \
    {
        "jabłka": "kg",
        "mleko": "litry",
        "chleb": "sztuki",
        "kurczak": "sztuki",
    }
    sztuki = [x for x, y in slownik_zakupow.items() if y == "sztuki"]
    print(sztuki)

zad3()

def zad4(a,b,c):
    if(a**2+b**2==c**2):
        return "trojkat jest prostokatny"
    else:
        return "trojkat nie jest prostokatny"

print(zad4(3,6,5))

def zad5(a,b,h):
    poletrapezu = ((a+b)*h)/2
    return poletrapezu
print(zad5(3,6,5))

def zad6(a=1,b=4,ile=10):
    wartosc = a*b**ile
    return wartosc

print(zad6(2,5,2))

def zad7(a):
    try:
        wynik = math.sqrt(a)
        return wynik
    except:
        return "error"


print(zad7(2))





















