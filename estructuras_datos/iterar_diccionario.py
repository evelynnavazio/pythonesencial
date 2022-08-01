lenguaje = {
    "nombre": "Python",
    "creador": "Guido"
}

for llave in lenguaje:
    print("llave:", llave)
    print("valor:", lenguaje[llave])

for elemento in lenguaje.keys():
    print(elemento)

for elemento in lenguaje.values():
    print(elemento)

for llave, valor in lenguaje.items():
    print(llave, valor)

for elemento in lenguaje.items():
    print(elemento)  # lo imprime como tupla llave valor completo
