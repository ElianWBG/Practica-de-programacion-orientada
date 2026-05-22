"""
Bloque 12 — Excepciones (try/except)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils.decoradores import input_str

class Bloque12:

    @staticmethod
    def ej1_value_error():
        entrada = input_str("Ingresa un número entero")
        try:    return {"ok":True,"valor":int(entrada)}
        except ValueError as e: return {"ok":False,"error":str(e)}

    @staticmethod
    def ej2_index_error():
        lista=[1,3,4]
        try:    return {"ok":True,"valor":lista[5]}
        except IndexError as e: return {"ok":False,"error":str(e)}

    @staticmethod
    def ej3_multiples():
        casos=[("10/0",lambda:10/0),("int('abc')",lambda:int("abc")),("10/2",lambda:10/2)]
        res=[]
        for nombre,fn in casos:
            try: res.append({"caso":nombre,"resultado":fn(),"error":None})
            except ZeroDivisionError as e: res.append({"caso":nombre,"resultado":None,"error":f"ZeroDivisionError: {e}"})
            except ValueError as e: res.append({"caso":nombre,"resultado":None,"error":f"ValueError: {e}"})
        return res
