def factorial_iterativo(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
"""
# Factorial de un número iterativamente
# El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.
# Se define una función iterativa que calcula el factorial de un número n."""


def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
    
"""
# Factorial de un número recursivamente
# El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.
# Se define una función recursiva que calcula el factorial de un número n."""
    

    

    

