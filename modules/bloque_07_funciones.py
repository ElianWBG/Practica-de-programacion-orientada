"""
Bloque 07 — Funciones
"""
from functools import reduce

class Bloque07:

    @staticmethod
    def ej1_doble(x): return x*2

    @staticmethod
    def ej2_sumar_varios(*nums): return sum(nums)

    @staticmethod
    def ej3_factorial(n): return 1 if n==0 else n*Bloque07.ej3_factorial(n-1)

    @staticmethod
    def ej4_lambdas():
        nums=[1,2,3,4,5,6,7,8,9,10]
        return {
            "cuadrado(5)":    (lambda x:x**2)(5),
            "es_par(4)":      (lambda x:x%2==0)(4),
            "saludar(Elian)": (lambda x:f"Hola, {x}!")("Elian"),
            "triples":        list(map(lambda x:x*3,nums)),
            "mayores_5":      list(filter(lambda x:x>5,nums)),
            "pares_cuadrados":list(map(lambda x:x**2,filter(lambda x:x%2==0,nums))),
        }

    @staticmethod
    def ej5_recursividad():
        def sumar_hasta(n): return 0 if n==0 else n+sumar_hasta(n-1)
        return {
            "factorial(5)":    Bloque07.ej3_factorial(5),
            "sumar_hasta(5)":  sumar_hasta(5),
            "sumar_hasta(10)": sumar_hasta(10),
        }
