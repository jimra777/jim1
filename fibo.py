# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        #print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = [] # Crea una lista en blanco
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
#JCRL. ANTERIORMENTE SE CREARON DOS FIBONACCI FIB Y FIB2
print(fib(100)) # Hasta 100
print(fib2(7**70))  # Hasta 70 veces siete
print(fib2(1000)) # Hasta 1000