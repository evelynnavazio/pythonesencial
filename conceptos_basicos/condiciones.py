from tkinter import E


a = 1
b = 1

if a > b:
    print("A es menor que B")
elif a == b:
    print("A es igual a B")
else:
    print("A es mayor que B")


c = True

if a:
    print("A es verdadero")
else:
    print("A es falso")

d = False

if type(d) is bool:
    print("D es booleano")


e = 10
f = 5
g = 1

if e > f and f > g:
    print("Las dos condiciones son verdaderas")

if e > f or f > g:
    print("Al menos uno de los dos es verdadero")
