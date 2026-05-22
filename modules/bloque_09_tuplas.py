"""
Bloque 09 — Tuplas
"""

class Bloque09:

    @staticmethod
    def ej1_inmutabilidad():
        t=(10,20,30,40)
        try: t[0]=99; return "Sin error (inesperado)"
        except TypeError as e: return f"TypeError: {e}"

    @staticmethod
    def ej2_unpacking():
        a,b,*resto=(100,200,300,400)
        return {"a":a,"b":b,"resto":resto}

    @staticmethod
    def ej3_coordenadas():
        return [(x,y) for x,y in [(1,2),(3,4),(5,6),(7,8)]]

    @staticmethod
    def ej4_conversion():
        t=(1,2,3); lst=list(t); lst.append(4); nueva=tuple(lst)
        return {"original":t,"nueva":nueva}
