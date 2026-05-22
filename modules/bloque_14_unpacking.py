"""
Bloque 14 — Unpacking
"""

class Bloque14:

    @staticmethod
    def ej1_unpacking_basico():
        primera,*mitad,ultima=(10,20,30,40)
        return {"primera":primera,"mitad":mitad,"ultima":ultima}

    @staticmethod
    def ej2_args_lista():
        def multiplicar(a,b,c): return a*b*c
        return multiplicar(*[2,3,4])

    @staticmethod
    def ej3_combinar_dicts():
        d1={"nombre":"Elian","edad":22}; d2={"ciudad":"Guayaquil","carrera":"Sistemas"}
        return {**d1,**d2}
