"""
Bloque 00 — Introducción a la POO
"""

@staticmethod
def noop(): pass  # placeholder para import

class Bloque00:

    @staticmethod
    def ej1_clases_biblioteca():
        return ["Libro", "Usuario", "Prestamo", "Autor", "Categoria"]

    @staticmethod
    def ej2_clase_persona():
        class Persona:
            def __init__(self, nombre, edad):
                self.nombre = nombre; self.edad = edad
        return [Persona("Elian",22), Persona("José",20), Persona("Jonathan",21)]

    @staticmethod
    def ej3_clase_auto():
        class Auto:
            def __init__(self, marca, color):
                self.marca = marca; self.color = color
            def presentarse(self):
                return f"Marca: {self.marca} | Color: {self.color}"
            def arrancar(self, estado):
                self.estado = estado
                return f"{self.marca} está {self.estado}"
        return [Auto("Suzuki","Negro"), Auto("Chevrolet","Blanco"), Auto("Hyundai","Rojo")]
