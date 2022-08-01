class Persona:
    pass  # para que no se genere un error se pone


pedro = Persona()
print(type(pedro))


paco = Persona()
print(type(paco))


# da False porque cada uno ocupa un espacio diferente en la memoria de la compu. Si son el mismo tipo no el mismo objeto
print(pedro == paco)
