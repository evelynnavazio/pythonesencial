for letra in "Texto":
    print(letra)

lenguajes = ['python', 'java', 'golang']
for elemento in lenguajes:
    if elemento == 'java':  # cuando llega a java se rompe el ciclo. imprime python/java
        continue  # break
    print(elemento)


for element in range(5):  # no incluye el ultimo numero
    print(element)


for element in range(1, 3):  # con punto de partida y de finalizacion
    print(element)
