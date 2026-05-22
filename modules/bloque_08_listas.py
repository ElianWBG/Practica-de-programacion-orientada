"""
Bloque 08 — Listas
"""

class Bloque08:

    @staticmethod
    def ej1_metodos_lista():
        lista=[]
        for v in [3,1,4]: lista.append(v)
        original=list(lista); lista.sort(); ordenada=list(lista)
        lista.reverse(); invertida=list(lista)
        return {"original":original,"ordenada":ordenada,"invertida":invertida}

    @staticmethod
    def ej2_estadisticas():
        nums=[5,3,8,1,9,3]
        return {"suma":sum(nums),"max":max(nums),"min":min(nums)}

    @staticmethod
    def ej3_referencia_vs_copia():
        lista=[1,2,3]; ref=lista; copia=lista.copy(); ref.append(4)
        return {"lista":lista,"copia_ref":ref,"copia_real":copia,
                "lista is copia_ref":lista is ref,"lista is copia_real":lista is copia}
