"""
Bloque 11 — Conjuntos (set)
"""

class Bloque11:

    @staticmethod
    def ej1_operaciones():
        A={1,2,3,4}; B={3,4,5,6}
        return {"union":sorted(A|B),"interseccion":sorted(A&B),
                "diferencia":sorted(A-B),"simetrica":sorted(A^B)}

    @staticmethod
    def ej2_eliminar_duplicados():
        return list(set([1,2,2,3,3,3,4]))

    @staticmethod
    def ej3_diferencia_simetrica():
        A={1,2,3,4,6}; B={6,7,8,9,10}
        r=(A|B)-(A&B)
        return {"resultado":sorted(r),"explicacion":"Todos los elementos excepto los compartidos (=A^B)"}
