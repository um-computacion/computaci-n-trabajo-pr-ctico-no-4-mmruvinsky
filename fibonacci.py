
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise ValueError("El número debe ser mayor o igual a 0")
    else:
        return fibonacci(n-1) + fibonacci(n-2)  
    
    """funcion recursiva para calcular el n-ésimo numero de Fibonacci"""
