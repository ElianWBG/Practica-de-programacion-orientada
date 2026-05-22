"""
Bloque 16 — Archivos y JSON
"""
import json, os, tempfile
_TMP=tempfile.gettempdir()

class Bloque16:

    @staticmethod
    def ej1_texto():
        r=os.path.join(_TMP,"demo.txt")
        with open(r,"w") as f: f.write("Python\nPOO\nBloque 16\n")
        with open(r,"r") as f: return f.read()

    @staticmethod
    def ej2_json_dict():
        r=os.path.join(_TMP,"demo.json")
        d={"x":10,"y":20}
        with open(r,"w") as f: json.dump(d,f,indent=2)
        with open(r,"r") as f: return json.load(f)

    @staticmethod
    def ej3_json_lista():
        r=os.path.join(_TMP,"usuarios.json")
        us=[{"nombre":"Ana","edad":20},{"nombre":"Luis","edad":30}]
        with open(r,"w") as f: json.dump(us,f,indent=2)
        with open(r,"r") as f: return [u["nombre"] for u in json.load(f)]
