"""
utils/decoradores.py — Decoradores de validación reutilizables

input_int / input_float / input_str usan builtins.input() para pasar
por el monkey-patch del marco, que controla la fila donde se muestra
cada prompt. La lógica de "reintento en la misma línea" vive en el
monkey-patch (patch_input_validado) y NO genera nuevas líneas.
"""
import functools, inspect, time, sys, builtins
from utils.consola import Color, c

# ── @validar(**reglas) ───────────────────────────────────────
def validar(**reglas):
    def decorador(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            sig   = inspect.signature(fn)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            for param, (tipo, condicion, msg) in reglas.items():
                if param in bound.arguments:
                    val = bound.arguments[param]
                    try:    val_conv = tipo(val)
                    except (ValueError, TypeError):
                        raise ValueError(f"{param}: se esperaba {tipo.__name__} — {msg}")
                    if not condicion(val_conv):
                        raise ValueError(f"{param}: {msg}")
            return fn(*args, **kwargs)
        return wrapper
    return decorador

def requiere_positivo(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        for a in args:
            if isinstance(a, (int, float)):
                if a <= 0:
                    raise ValueError(f"Se esperaba número positivo, recibido: {a}")
                break
        return fn(*args, **kwargs)
    return wrapper

def capturar_errores(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:    return fn(*args, **kwargs), None
        except Exception as e: return None, str(e)
    return wrapper

def log_llamada(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(str(a) for a in args)
        print(f"  {c('▶ Llamando:', Color.CIAN)} "
              f"{c(fn.__name__, Color.AMARILLO)}({args_str})")
        res = fn(*args, **kwargs)
        print(f"  {c('◀ Retorna: ', Color.CIAN)} {c(str(res), Color.VERDE)}")
        return res
    return wrapper

def medir_tiempo(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t0  = time.perf_counter()
        res = fn(*args, **kwargs)
        ms  = (time.perf_counter() - t0) * 1000
        print(f"  {c('⏱', Color.GRIS)} {c(fn.__name__, Color.AMARILLO)} "
              f"→ {c(f'{ms:.3f} ms', Color.VERDE)}")
        return res
    return wrapper

# ── Inputs validados ─────────────────────────────────────────
# Usan builtins.input() → interceptado por patch_input en el marco.
# El mensaje de error se pasa como parte del prompt cuando hay error,
# de modo que el marco lo puede dibujar en la MISMA fila (sin nueva línea).
# Protocolo: si el valor falla, llamamos builtins.input con un prompt
# especial que empieza con "\x01ERROR\x01" para que el marco sepa que
# debe sobreescribir la fila anterior.

_ERR_PREFIX = "\x01ERR\x01"  # señal interna para "reescribir misma fila"

def input_int(texto, minimo=None, maximo=None):
    rango = (f" ({minimo}–{maximo})" if minimo is not None and maximo is not None
             else f" (≥{minimo})" if minimo is not None
             else f" (≤{maximo})" if maximo is not None else "")
    prompt_ok  = f"▶  {texto}{rango}"
    prompt_err = f"{_ERR_PREFIX}▶  {texto}{rango}"
    prompt     = prompt_ok
    while True:
        val = builtins.input(prompt)
        try:
            n = int(val)
            if minimo is not None and n < minimo: raise ValueError
            if maximo is not None and n > maximo: raise ValueError
            return n
        except (ValueError, TypeError):
            err_msg = f"⚠ Ingresa un entero válido{rango}"
            prompt  = f"{_ERR_PREFIX}▶  {texto}{rango}  {c(err_msg, Color.ROJO)}"

def input_float(texto, minimo=None):
    suf        = f" (≥{minimo})" if minimo is not None else ""
    prompt_ok  = f"▶  {texto}{suf}"
    prompt     = prompt_ok
    while True:
        val = builtins.input(prompt)
        try:
            n = float(val)
            if minimo is not None and n < minimo: raise ValueError
            return n
        except (ValueError, TypeError):
            err_msg = f"⚠ Ingresa un decimal válido{suf}"
            prompt  = f"{_ERR_PREFIX}▶  {texto}{suf}  {c(err_msg, Color.ROJO)}"

def input_str(texto, opciones=None, solo_letras=False):
    """
    Valida entrada de texto.
    - Rechaza vacío siempre.
    - Si opciones: la entrada debe estar en la lista.
    - Si solo_letras=True o no hay opciones y el texto sugiere nombre/texto:
      rechaza entradas que sean puramente numéricas.
    """
    suf       = f" ({'/'.join(opciones)})" if opciones else ""
    prompt_ok = f"▶  {texto}{suf}"
    prompt    = prompt_ok
    # Detectar automáticamente si el campo espera texto (no número)
    _palabras_texto = ("nombre", "name", "apellido", "ciudad", "país", "pais",
                       "texto", "mensaje", "descripcion", "descripción", "título",
                       "titulo", "palabra", "cadena", "str")
    es_campo_texto = solo_letras or (
        not opciones and any(p in texto.lower() for p in _palabras_texto)
    )
    while True:
        val = builtins.input(prompt)
        try:
            v = val.strip()
            if not v:
                raise ValueError("vacio")
            if opciones and v.lower() not in opciones:
                raise ValueError("opcion")
            if es_campo_texto and v.replace('.','').replace(',','').replace('-','').isdigit():
                raise ValueError("numerico")
            return v
        except ValueError as e:
            if opciones:
                err_msg = f"⚠ Elige: {'/'.join(opciones)}"
            elif "numerico" in str(e):
                err_msg = "⚠ Ingresa texto, no solo números"
            else:
                err_msg = "⚠ No puede estar vacío"
            prompt = f"{_ERR_PREFIX}▶  {texto}{suf}  {c(err_msg, Color.ROJO)}"
