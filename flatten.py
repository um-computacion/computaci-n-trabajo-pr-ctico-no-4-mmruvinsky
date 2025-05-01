def flatten(lista):
    resultado = []
    for i in lista:
        if isinstance(i, list):
            resultado.extend(flatten(i))
        else:
            resultado.append(i)
    return resultado


print (flatten([1, 2, [3, 4], [5, [6, 7]]]))

"""funcion recursiva para aplanar una lista de listas"""