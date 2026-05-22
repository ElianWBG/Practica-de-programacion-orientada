"""
Bloque 03 — Operadores
"""

class Bloque03:

    @staticmethod
    def ej1_aritmeticos():
        a,b=20,4
        return {"suma":a+b,"resta":a-b,"mult":a*b,"division":a/b,
                "div_entera":a//b,"modulo":a%b,"potencia":a**b}

    @staticmethod
    def ej2_comparacion_is():
        li=[10,11,12,13]; li2=[10,11,12,13]; li3=li
        return {"li == li2":li==li2,"li is li2":li is li2,"li is li3":li is li3}

    @staticmethod
    def ej3_precedencia():
        x = 2 + 1 * 2 % 2 + (2**1) // 2
        return {
            "resultado": x,
            "pasos": ["2**1 = 2","1 * 2 = 2","2 % 2 = 0","2 // 2 = 1","2 + 0 + 1 = 3"],
        }
