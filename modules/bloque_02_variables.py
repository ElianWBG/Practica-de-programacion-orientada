"""
Bloque 02 — Variables y Tipos de Datos
"""

class Bloque02:

    @staticmethod
    def ej1_tipos_simples():
        return {"int":40,"float":3.1415,"str":"Hola Python","bool":True,"None":None}

    @staticmethod
    def ej2_tipos_complejos():
        return {"list":[1,2,3,"Elian"],"tuple":(1,"Hola",3.14),
                "dict":{"nombre":"Elian","edad":22},"set":{1,2,3}}

    @staticmethod
    def ej3_slicing():
        lista = [10,20,30,40,50]
        return {"primero":lista[0],"ultimo":lista[-1],"lista[1:4]":lista[1:4]}

    @staticmethod
    def ej4_inventario():
        class Inventario:
            def mostrar_info(self):
                producto = "Laptop Gaming"
                precios  = [450.99,899.50,1200.00,75.25,320.00]
                stock    = {"laptops":15,"mouses":42,"teclados":8}
                return {
                    "primeros_6":    producto[0:6],
                    "primer_precio": precios[0],
                    "ultimo_precio": precios[-1],
                    "rango":         precios[1:3],
                    "mouses":        stock["mouses"],
                }
        return Inventario().mostrar_info()
