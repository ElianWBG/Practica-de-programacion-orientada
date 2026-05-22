"""
Bloque 06 — Bucles (for/while)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils.decoradores import input_str

class Bloque06:

    @staticmethod
    def ej1_while_1_10():
        nums=[]; i=1
        while i<=10: nums.append(i); i+=1
        return nums

    @staticmethod
    def ej2_enumerate_frutas():
        return list(enumerate(["manzana","pera","uva","mango","kiwi"],1))

    @staticmethod
    def ej3_cuadrados_pares():
        return [x**2 for x in range(1,11) if x%2==0]

    @staticmethod
    def ej4_buscar_producto():
        productos = ["laptop","mouse","teclado","monitor","audífonos"]
        busq = input_str("Producto a buscar")
        for i,nombre in enumerate(productos):
            if nombre==busq.lower():
                return {"encontrado":True,"posicion":i,"producto":busq}
        return {"encontrado":False,"posicion":-1,"producto":busq}
