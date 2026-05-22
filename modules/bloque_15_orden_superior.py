"""
Bloque 15 — Funciones de Orden Superior
"""
from functools import reduce

class Bloque15:

    @staticmethod
    def ej1_map(): return list(map(lambda x:x+1,[2,4,6]))

    @staticmethod
    def ej2_filter(): return list(filter(lambda x:x>3,[1,2,3,4,5]))

    @staticmethod
    def ej3_reduce(): return reduce(lambda x,y:x*y,[1,2,3,4])

    @staticmethod
    def ej4_combinacion():
        nums=[1,2,3,4,5,6,7,8,9,10]
        return {
            "triples":         list(map(lambda x:x*3,nums)),
            "mayores_5":       list(filter(lambda x:x>5,nums)),
            "pares_cuadrados": list(map(lambda x:x**2,filter(lambda x:x%2==0,nums))),
        }
