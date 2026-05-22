"""
Bloque 17 — Mixins
"""
import json

class PromedioMixin:
    def calcular_promedio(self,notas): return sum(notas)/len(notas)

class ValidacionMixin:
    def validar_email(self,correo):
        if "@" not in correo or ".com" not in correo: raise ValueError("Email inválido")
    def validar_edad(self,edad):
        if edad<18: raise ValueError("Debe ser mayor de edad")

class ExportarMixin:
    def exportar_json(self,datos): return json.dumps(datos,indent=2)
    def exportar_csv(self,datos): return ",".join(str(v) for v in datos.values())

class Estudiante17(PromedioMixin):
    def __init__(self,nombre,notas): self.nombre=nombre; self.notas=notas
    def mostrar_promedio(self): return f"{self.nombre} — promedio: {self.calcular_promedio(self.notas):.1f}"

class Usuario17(ValidacionMixin):
    def __init__(self,nombre,email,edad):
        self.validar_email(email); self.validar_edad(edad)
        self.nombre=nombre; self.email=email; self.edad=edad

class Reporte17(ExportarMixin):
    def __init__(self,datos): self.datos=datos
    def mostrar(self): return {"json":self.exportar_json(self.datos),"csv":self.exportar_csv(self.datos)}

class Bloque17:

    @staticmethod
    def ej1_promedio_mixin(): return Estudiante17("Elian",[8,9,10]).mostrar_promedio()

    @staticmethod
    def ej2_validacion_mixin():
        res=[]
        for nombre,email,edad in [("Elian","elian@gmail.com",22),("Ana","anacorreo",20),("Luis","luis@gmail.com",15)]:
            try: u=Usuario17(nombre,email,edad); res.append({"usuario":u.nombre,"ok":True,"msg":"Registrado ✔"})
            except ValueError as e: res.append({"usuario":nombre,"ok":False,"msg":str(e)})
        return res

    @staticmethod
    def ej3_exportar_mixin():
        return Reporte17({"nombre":"Elian","edad":22,"carrera":"Sistemas"}).mostrar()
