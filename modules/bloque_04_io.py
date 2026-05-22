"""
Bloque 04 — Entrada y Salida (input/print)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils.decoradores import input_int, input_float, input_str

class Bloque04:

    @staticmethod
    def ej1_ficha_personal():
        nombre = input_str("Ingrese su nombre")
        edad   = input_int("Ingrese su edad", minimo=0, maximo=120)
        altura = input_float("Ingrese su altura (ej 1.75)", minimo=0.0)
        return {"nombre":nombre,"edad":edad,"altura":altura}

    @staticmethod
    def ej2_calculadora():
        n1 = input_float("Ingrese primer número")
        n2 = input_float("Ingrese segundo número")
        return {"suma":n1+n2,"promedio":(n1+n2)/2}

    @staticmethod
    def ej3_error_str():
        numero = input_str("Ingrese un número")
        return {"concatenacion":numero+"10","repeticion":numero*2}
