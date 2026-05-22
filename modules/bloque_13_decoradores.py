"""
Bloque 13 — Decoradores
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils.decoradores import validar, requiere_positivo, capturar_errores, log_llamada, medir_tiempo

class Bloque13:

    @staticmethod
    def ej1_decorador_inicio():
        def iniciando(fn):
            def wrapper(*a,**k):
                print("  Iniciando...")
                r=fn(*a,**k)
                print("  Finalizando...")
                return r
            return wrapper
        @iniciando
        def saludar(): print("  Hola Mundo!")
        saludar()

    @staticmethod
    def ej2_validar_positivo():
        @requiere_positivo
        def cuadrado(a): return a**2
        @capturar_errores
        def cuadrado_seguro(a): return cuadrado(a)
        return {"cuadrado(4)":cuadrado_seguro(4),"cuadrado(-3)":cuadrado_seguro(-3)}

    @staticmethod
    def ej3_log():
        @log_llamada
        def suma(a,b): return a+b
        return suma(2,3)

    @staticmethod
    def ej4_validar_kwargs():
        @validar(
            precio=(float, lambda v:v>=0, "Debe ser >= 0"),
            cantidad=(int,  lambda v:v>0,  "Debe ser > 0"),
        )
        def registrar_venta(nombre, precio, cantidad):
            return f"{nombre}: ${precio:.2f} × {cantidad} uds"
        res=[]
        for nombre,precio,cantidad in [("Laptop",900.0,2),("Mouse",-5.0,1),("Teclado",35.0,0)]:
            try: res.append({"caso":nombre,"resultado":registrar_venta(nombre,precio,cantidad),"error":None})
            except ValueError as e: res.append({"caso":nombre,"resultado":None,"error":str(e)})
        return res

    @staticmethod
    def ej5_medir_tiempo():
        @medir_tiempo
        def sumar_lista(n): return sum(range(n))
        return sumar_lista(100_000)
