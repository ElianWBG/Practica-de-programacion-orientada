"""
Bloque 05 — Condicionales
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils.decoradores import input_int, input_str

class Bloque05:

    @staticmethod
    def ej1_par_impar():
        n = input_int("Ingrese un número")
        return "Par" if n%2==0 else "Impar"

    @staticmethod
    def ej2_calificacion():
        nota = input_int("Ingrese la nota (0-100)", minimo=0, maximo=100)
        letra = "A" if nota>=90 else "B" if nota>=80 else "C" if nota>=70 else "D"
        return {"nota":nota,"letra":letra}

    @staticmethod
    def ej3_login():
        usuario  = input_str("Usuario")
        password = input_str("Contraseña")
        if usuario=="admin" and password=="123":
            return True,"Bienvenido, admin!"
        return False,"Acceso denegado"

    @staticmethod
    def ej4_clasificar_vehiculo():
        tipo = input_str("Tipo de vehículo", opciones=["auto","moto","camion","bus"])
        velo = input_int("Velocidad actual (km/h)", minimo=0)
        anos = input_int("Años de antigüedad", minimo=0)
        match tipo:
            case "auto":   cat="Vehículo liviano"
            case "moto":   cat="Vehículo de dos ruedas"
            case "camion": cat="Vehículo pesado"
            case "bus":    cat="Transporte público"
            case _:        cat="Vehículo desconocido"
        vel = ("Velocidad baja" if velo<60 else
               "Velocidad normal" if velo<=120 else "Exceso de velocidad")
        est = "Vehículo riesgoso" if anos>10 and velo>100 else "Vehículo en condiciones"
        return {"tipo":tipo,"categoria":cat,"velocidad":vel,"estado":est}
