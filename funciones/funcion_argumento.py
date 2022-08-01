def perimetro_cuadrado(lado, unidades):  # argumento o parametro
    perimetro = lado * 4
    print(f"El perimetro es {perimetro} {unidades}")


perimetro_cuadrado(25, "metros")  # en orden
perimetro_cuadrado(lado=25, unidades="metros")  # con nombre propio
