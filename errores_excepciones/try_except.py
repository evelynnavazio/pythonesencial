from ast import Assert


def calcular_promedio(lista):
    assert len(lista) > 0, "La lista esta vacia"
    return sum(lista) / len(lista)


try:
    promedio = calcular_promedio(lista=["te"])
    print(promedio)
except AssertionError as assert_error:
    print(assert_error)
except Exception as e:
    print("no se calc el promedio")
    print(e)
