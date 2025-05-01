def flatten(lista):
    resultado = []
    for i in lista:
        if isinstance(i, list):
            resultado.extend(flatten(i))
        elif isinstance(i, tuple):
            resultado.extend(flatten(list(i)))
        elif isinstance(i, dict):
            for key, value in i.items():
                resultado.append(key)
                resultado.extend(flatten([value]))

        else:
            resultado.append(i)
    return resultado


print (flatten([1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]))

"""funcion recursiva para aplanar una lista de listas"""