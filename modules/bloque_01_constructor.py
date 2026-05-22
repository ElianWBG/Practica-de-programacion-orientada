"""
Bloque 01 — Constructor __init__
"""

class Bloque01:

    @staticmethod
    def ej1_producto():
        class Producto:
            def __init__(self, codigo, nombre, precio):
                if precio < 0: raise ValueError("Precio no puede ser negativo")
                self.codigo = codigo; self.nombre = nombre; self.precio = precio
        return [Producto("P001","Laptop",900), Producto("P002","Mouse",25)]

    @staticmethod
    def ej2_estudiante():
        class Estudiante:
            def __init__(self, nombre, notas=None):
                self.nombre = nombre; self.notas = notas or []
            @classmethod
            def desde_diccionario(cls, d):
                return cls(d["nombre"], d["notas"])
            @classmethod
            def desde_texto(cls, txt):
                p = txt.split(",")
                return cls(p[0], [int(n) for n in p[1:]])
        return [
            Estudiante("Elian",[8,9,10]),
            Estudiante.desde_diccionario({"nombre":"Luis","notas":[8,9,7]}),
            Estudiante.desde_texto("Carlos,7,8,9"),
            Estudiante("Ana"),
        ]

    @staticmethod
    def ej3_libro():
        class Libro:
            def __init__(self, titulo, autor, paginas, generos=None):
                if paginas < 0: raise ValueError("Páginas no puede ser negativa")
                self.titulo = titulo; self.autor = autor
                self.paginas = paginas; self.generos = generos or []
            @classmethod
            def desde_diccionario(cls, d):
                return cls(d["titulo"],d["autor"],d["paginas"],d["generos"])
            @classmethod
            def desde_texto(cls, txt):
                p = txt.split(",")
                return cls(p[0],p[1],int(p[2]),p[3:])
        return [
            Libro("El Principito","Saint-Exupéry",96,["infantil","filosofía"]),
            Libro.desde_diccionario({"titulo":"Dune","autor":"Herbert","paginas":412,"generos":["ciencia ficción"]}),
            Libro.desde_texto("Python 101,Smith,250,tecnología,programación"),
        ]
