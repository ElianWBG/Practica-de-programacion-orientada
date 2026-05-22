"""
Bloque 10 — Diccionarios
"""

class Bloque10:

    @staticmethod
    def ej1_acceso():
        p={"nombre":"Elian","edad":22,"ciudad":"Durán"}
        return {"corchetes":p["nombre"],"get_edad":p.get("edad","no existe"),
                "get_telefono":p.get("telefono","no existe")}

    @staticmethod
    def ej2_iterar():
        return list({"nombre":"Elian","edad":22,"ciudad":"Durán"}.items())

    @staticmethod
    def ej3_referencia_copia():
        d={"nombre":"Juan"}; c=d; c["nuevo"]=2
        return {"datos":d,"copia":c,"mismo_objeto":d is c}

    @staticmethod
    def ej4_comprehension():
        return {x:x**2 for x in range(11)}
