def validar_x(x):
    if x < 1:
        raise Exception("la variable x debe der mayor a uno")
    else:
        print("x es mayor a 1")


x = 2


validar_x(x)
