"""
controllers/menu_controller.py
- Visor de código: 10 líneas + scroll W↑ / S↓
- Contexto informativo antes de los inputs
- Todos los inputs pre-renderizados de una sola vez
- Validación: reescribe la MISMA línea (sin generar nueva línea)
- Todo dentro de la caja centrada ╔═╗
"""
import sys, os, time, builtins, re

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.consola import (
    Color, c, RESET, BOLD,
    limpiar, ocultar_cursor, mostrar_cursor,
    gotoxy, w, truncar, get_cols, get_filas,
    borde_h, paredes, limpiar_fila, fila_centrada,
    TL, TR, BL, BR, H, V, ML, MR,
)
from utils.decoradores import _ERR_PREFIX   # señal de "reescribir misma fila"

LINEAS_COD = 10
_ANSI = re.compile(r'\033\[[0-9;]*m')

def _len_visual(s):
    """Longitud visible del string (sin secuencias ANSI)."""
    return len(_ANSI.sub('', s))

def _trunc_visual(s, max_len):
    """Trunca s a max_len caracteres visibles."""
    limpio = _ANSI.sub('', s)
    if len(limpio) <= max_len:
        return s
    # Necesitamos cortar el string con ANSI preservado
    count = 0
    result = []
    i = 0
    while i < len(s) and count < max_len - 1:
        if s[i] == '\033':
            j = i
            while j < len(s) and s[j] != 'm':
                j += 1
            result.append(s[i:j+1])
            i = j + 1
        else:
            result.append(s[i])
            count += 1
            i += 1
    return ''.join(result) + "…"


# ════════════════════════════════════════════════════════════
#  VISOR DE CÓDIGO
# ════════════════════════════════════════════════════════════
def _dibujar_bloque_codigo(x_ini, x_fin, inter, cb, y_inicio, lineas, offset):
    NUM_W = 4
    COD_W = inter - NUM_W - 4
    total = len(lineas)
    y     = y_inicio
    for rel in range(LINEAS_COD):
        idx = offset + rel
        paredes(x_ini, x_fin, y, cb)
        limpiar_fila(x_ini, inter, y)
        if idx < total:
            num_str = f"{idx+1:>{NUM_W}}"
            cod_str = truncar(lineas[idx].expandtabs(4), COD_W)
            gotoxy(x_ini + 1, y)
            w(f" {c(num_str, Color.GRIS)} {c('│', Color.GRIS)} "
              f"{c(cod_str, Color.VERDE)}")
        y += 1
    # Barra de estado
    paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
    pag_a  = offset // LINEAS_COD + 1
    pag_t  = max(1, (total + LINEAS_COD - 1) // LINEAS_COD)
    nav    = "  W↑ subir  S↓ bajar" if total > LINEAS_COD else ""
    status = _trunc_visual(
        f"  Líneas {offset+1}–{min(offset+LINEAS_COD,total)} de {total}"
        f"  [{pag_a}/{pag_t}]{nav}", inter - 2)
    gotoxy(x_ini + 1, y); w(f"{Color.GRIS}{status}{RESET}")
    return y + 1


# ════════════════════════════════════════════════════════════
#  MARCO DE EJECUCIÓN
# ════════════════════════════════════════════════════════════
def _ejecutar_en_marco(datos: dict):
    ruta     = datos["ruta"]
    desc     = datos["desc"]
    fn       = datos["fn"]
    inputs   = datos.get("inputs", [])    # prompts pre-declarados
    contexto = datos.get("contexto", [])  # líneas informativas

    # ── Leer archivo fuente ──────────────────────────────────
    ruta_abs = os.path.abspath(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), ruta))
    try:
        with open(ruta_abs, "r", encoding="utf-8", errors="replace") as f:
            lineas_codigo = f.read().splitlines()
    except Exception:
        lineas_codigo = ["(no se pudo leer el archivo)"]

    total_cod = len(lineas_codigo)
    offset    = [0]

    cols  = get_cols()
    ancho = max(56, min(84, cols - 2))
    inter = ancho - 2
    x_ini = max(1, (cols - ancho) // 2 + 1)
    x_fin = x_ini + ancho - 1
    cb    = Color.MAGENTA

    # ── FASE 1: scroll de código ─────────────────────────────
    while True:
        limpiar(); ocultar_cursor()
        y = 1
        borde_h(x_ini, y, ancho, TL, TR, cb); y += 1

        paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
        fila_centrada(x_ini, inter, y, "◈  EJECUTANDO EJERCICIO", BOLD + Color.BLANCO)
        y += 1; borde_h(x_ini, y, ancho, ML, MR, cb); y += 1

        paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
        gotoxy(x_ini + 1, y)
        w(f"{Color.CIAN}{_trunc_visual(f'  📄 {ruta_abs}', inter-2)}{RESET}"); y += 1

        paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
        gotoxy(x_ini + 1, y)
        w(f"{Color.GRIS}{_trunc_visual(f'  {desc}', inter-2)}{RESET}"); y += 1

        borde_h(x_ini, y, ancho, ML, MR, cb); y += 1
        y = _dibujar_bloque_codigo(x_ini, x_fin, inter, cb, y, lineas_codigo, offset[0])

        if total_cod > LINEAS_COD:
            borde_h(x_ini, y, ancho, ML, MR, cb); y += 1
            paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
            fila_centrada(x_ini, inter, y,
                          "W ↑ subir código     S ↓ bajar código     Enter → ejecutar",
                          Color.AMARILLO); y += 1

        borde_h(x_ini, y, ancho, ML, MR, cb); y += 1
        paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
        fila_centrada(x_ini, inter, y, "[Enter] Ejecutar    [0] Volver", Color.GRIS)
        y += 1; borde_h(x_ini, y, ancho, BL, BR, cb)

        gotoxy(x_ini + 1, y + 1); mostrar_cursor()
        sys.stdout.write(f"  {c('▶', Color.VERDE)}  {c('Opción: ', Color.BLANCO)}")
        sys.stdout.flush()
        tecla = sys.stdin.readline().rstrip("\n").strip().lower()

        if tecla == "0":
            return
        elif tecla in ("s", "j"):
            if offset[0] + LINEAS_COD < total_cod:
                offset[0] += LINEAS_COD
        elif tecla in ("w", "k"):
            offset[0] = max(0, offset[0] - LINEAS_COD)
        else:
            break  # Enter → ejecutar

    # ── FASE 2: pre-renderizar marco de ejecución ────────────
    limpiar(); ocultar_cursor()
    y = 1
    borde_h(x_ini, y, ancho, TL, TR, cb); y += 1

    paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
    fila_centrada(x_ini, inter, y, "◈  EJECUTANDO EJERCICIO", BOLD + Color.BLANCO)
    y += 1; borde_h(x_ini, y, ancho, ML, MR, cb); y += 1

    paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
    gotoxy(x_ini + 1, y)
    w(f"{Color.CIAN}{_trunc_visual(f'  📄 {ruta_abs}', inter-2)}{RESET}"); y += 1

    paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
    gotoxy(x_ini + 1, y)
    w(f"{Color.GRIS}{_trunc_visual(f'  {desc}', inter-2)}{RESET}"); y += 1

    borde_h(x_ini, y, ancho, ML, MR, cb); y += 1

    # ── Contexto informativo ─────────────────────────────────
    if contexto:
        for linea_ctx in contexto:
            paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
            gotoxy(x_ini + 2, y)
            w(f"{Color.CIAN}{_trunc_visual(linea_ctx, inter-4)}{RESET}")
            y += 1
        paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y); y += 1
        borde_h(x_ini, y, ancho, ML, MR, cb); y += 1

    # ── Pre-renderizar todos los inputs vacíos ───────────────
    filas_inputs = []
    for prompt_txt in inputs:
        paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
        max_p = inter - 4
        prompt_vis = _trunc_visual(f"  {prompt_txt}: ", max_p)
        gotoxy(x_ini + 2, y)
        w(f"{Color.VERDE}{prompt_vis}{RESET}")
        gotoxy(x_fin, y); w(f"{cb}{V}{RESET}")
        filas_inputs.append(y)
        y += 1

    # Separador antes de la zona de output
    if inputs:
        borde_h(x_ini, y, ancho, ML, MR, cb); y += 1

    # ── Estado del monkey-patch ──────────────────────────────
    mostrar_cursor()
    estado = {
        "fila":             y,
        "prompt_pendiente": "",
        "input_idx":        0,
        "filas_inputs":     filas_inputs,
    }

    def _color_txt(texto):
        t = texto.strip()
        if t.startswith(("✔","✓")): return Color.VERDE
        if t.startswith(("✘","✗")): return Color.ROJO
        if t.startswith("⚠"):       return Color.AMARILLO
        if t.startswith("ℹ"):       return Color.CIAN
        if t.startswith(("▸","►")): return Color.AMARILLO
        return Color.BLANCO

    def _dibujar_output(texto, color_txt=None):
        """Dibuja una nueva línea en la zona de output (avanza fila)."""
        yf  = estado["fila"]
        clr = color_txt or _color_txt(texto)
        paredes(x_ini, x_fin, yf, cb)
        limpiar_fila(x_ini, inter, yf)
        trunc = _trunc_visual(texto, inter - 4)
        gotoxy(x_ini + 2, yf); w(f"{clr}{trunc}{RESET}")
        gotoxy(x_fin, yf);     w(f"{cb}{V}{RESET}")
        estado["fila"] += 1

    def patch_print(*args, **kwargs):
        sep_  = kwargs.get("sep", " ")
        end_  = kwargs.get("end", "\n")
        file_ = kwargs.get("file", None)
        if file_ is sys.stderr:
            sys.stderr.write(sep_.join(str(a) for a in args) + (end_ or "")); return
        if file_ not in (None, sys.stdout): return
        texto  = sep_.join(str(a) for a in args)
        partes = texto.split("\n")
        if end_ == "" and len(partes) == 1:
            estado["prompt_pendiente"] += partes[0]; return
        if estado["prompt_pendiente"]:
            partes[0] = estado["prompt_pendiente"] + partes[0]
            estado["prompt_pendiente"] = ""
        for parte in partes:
            _dibujar_output(parte)

    def patch_input(prompt=""):
        """
        Pre-renderizado activo: cada input ya tiene su fila asignada.
        - Prompt normal  → posicionarse en la fila pre-renderizada y esperar input.
        - _ERR_PREFIX    → sobreescribir la MISMA fila: prompt verde + error rojo.
        Tras leer el valor, redibuja la fila limpia: prompt verde + valor en cian.
        Si el valor falla, la siguiente llamada con _ERR_PREFIX lo sobreescribirá.
        """
        prompt_str = estado["prompt_pendiente"] + str(prompt)
        estado["prompt_pendiente"] = ""
        es_error = prompt_str.startswith(_ERR_PREFIX)

        if es_error:
            prompt_str = prompt_str[len(_ERR_PREFIX):]

        idx = estado["input_idx"]
        if idx < len(estado["filas_inputs"]):
            yf = estado["filas_inputs"][idx]
        else:
            yf = estado["fila"]
            if not es_error:
                paredes(x_ini, x_fin, yf, cb); limpiar_fila(x_ini, inter, yf)
                estado["fila"] += 1

        # ── Separar prompt base del mensaje de error (si lo hay) ──────────
        # El prompt_str en caso de error tiene la forma:
        #   "▶  Texto (rango)  \x1b[...m⚠ Ingresa...\x1b[0m"
        # Separamos por el primer carácter ⚠ (visible)
        prompt_limpio_vis = _ANSI.sub('', prompt_str)
        corte_err = prompt_limpio_vis.find('⚠')
        if es_error and corte_err >= 0:
            prompt_base_vis = prompt_limpio_vis[:corte_err].rstrip()
            err_msg_vis     = prompt_limpio_vis[corte_err:]
        else:
            prompt_base_vis = prompt_limpio_vis
            err_msg_vis     = ""

        # ── Redibujar la fila ──────────────────────────────────────────────
        paredes(x_ini, x_fin, yf, cb); limpiar_fila(x_ini, inter, yf)
        max_p      = inter - 4
        base_part  = _trunc_visual(f"  {prompt_base_vis}: ", max_p)
        gotoxy(x_ini + 2, yf)
        w(f"{Color.VERDE}{base_part}{RESET}")
        col_cursor = x_ini + 2 + _len_visual(base_part)

        if es_error and err_msg_vis:
            espacio_err = (x_fin - 2) - col_cursor
            err_trunc   = err_msg_vis[:max(0, espacio_err)]
            w(f"{Color.ROJO}{err_trunc}{RESET}")
            col_cursor += len(err_trunc)

        # Rellenar hasta borde y posicionar cursor
        relleno = (x_fin - 1) - col_cursor
        if relleno > 0: w(" " * relleno)
        gotoxy(x_fin, yf); w(f"{cb}{V}{RESET}")
        # Cursor al final del prompt base (sobre el error si hay, o al final)
        gotoxy(x_ini + 2 + _len_visual(base_part), yf)

        val = sys.stdin.readline().rstrip("\n")

        # ── Redibujar limpio con el valor ingresado ────────────────────────
        paredes(x_ini, x_fin, yf, cb); limpiar_fila(x_ini, inter, yf)
        val_display  = val if val else ""
        prompt_show  = _trunc_visual(f"  {prompt_base_vis}: ", max_p - len(val_display) - 1)
        gotoxy(x_ini + 2, yf)
        w(f"{Color.VERDE}{prompt_show}{RESET}{Color.CIAN}{val_display}{RESET}")
        col_after = x_ini + 2 + _len_visual(prompt_show) + len(val_display)
        relleno2  = (x_fin - 1) - col_after
        if relleno2 > 0: w(" " * relleno2)
        gotoxy(x_fin, yf); w(f"{cb}{V}{RESET}")
        sys.stdout.flush()

        if not es_error:
            if idx < len(estado["filas_inputs"]):
                estado["input_idx"] += 1

        return val

    # ── Monkey-patch ─────────────────────────────────────────
    orig_print = builtins.print
    orig_input = builtins.input
    builtins.print = patch_print
    builtins.input = patch_input

    try:
        resultado = fn()
        # Separador entre inputs y resultado
        if resultado is not None:
            _dibujar_output("")
            _renderizar_resultado(resultado, _dibujar_output)
    except SystemExit:
        pass
    except Exception as e:
        _dibujar_output(f"  ⚠  Error: {e}", Color.ROJO)
    finally:
        builtins.print = orig_print
        builtins.input = orig_input

    # ── Pie ──────────────────────────────────────────────────
    yp = estado["fila"]
    paredes(x_ini, x_fin, yp, cb); limpiar_fila(x_ini, inter, yp); yp += 1
    borde_h(x_ini, yp, ancho, ML, MR, cb); yp += 1
    paredes(x_ini, x_fin, yp, cb); limpiar_fila(x_ini, inter, yp)
    fila_centrada(x_ini, inter, yp, "✔  Ejercicio finalizado", BOLD + Color.VERDE)
    yp += 1; borde_h(x_ini, yp, ancho, ML, MR, cb); yp += 1
    ocultar_cursor()
    paredes(x_ini, x_fin, yp, cb); limpiar_fila(x_ini, inter, yp)
    fila_centrada(x_ini, inter, yp, "Presiona Enter para volver...", Color.GRIS)
    yp += 1; borde_h(x_ini, yp, ancho, BL, BR, cb)
    gotoxy(x_ini + 1, yp + 1); mostrar_cursor()
    sys.stdin.readline()


def _renderizar_resultado(resultado, dibujar):
    """Renderiza el valor devuelto por fn() en la zona de output."""
    if isinstance(resultado, dict):
        for k, v in resultado.items():
            dibujar(f"  ▸ {k}: {v}", Color.AMARILLO)
    elif isinstance(resultado, list):
        for item in resultado:
            if isinstance(item, dict):
                ok_  = item.get("ok", True)
                clr  = Color.VERDE if ok_ else Color.ROJO
                sym  = "✔" if ok_ else "✘"
                if "usuario" in item:
                    dibujar(f"  {sym}  {item['usuario']}: {item.get('msg','')}", clr)
                elif "caso" in item:
                    if item.get('error') is None:
                        dibujar(f"  ▸ {item['caso']} → {item['resultado']}", Color.VERDE)
                    else:
                        dibujar(f"  ✘ {item['caso']} → {item['error']}", Color.ROJO)
                else:
                    dibujar(f"  ▸ {item}", Color.AMARILLO)
            elif hasattr(item, '__dict__'):
                for k2, v2 in vars(item).items():
                    dibujar(f"  ▸ {k2}: {v2}", Color.AMARILLO)
            elif isinstance(item, tuple) and len(item) == 2:
                dibujar(f"  ▸ {item[0]}  →  {item[1]}", Color.AMARILLO)
            else:
                dibujar(f"  ▸ {item}", Color.AMARILLO)
    elif isinstance(resultado, tuple) and len(resultado)==2 and isinstance(resultado[0], bool):
        clr = Color.VERDE if resultado[0] else Color.ROJO
        dibujar(f"  {'✔' if resultado[0] else '✘'}  {resultado[1]}", clr)
    else:
        dibujar(f"  ▸ {resultado}", Color.AMARILLO)


# ════════════════════════════════════════════════════════════
#  SUBMENÚ
# ════════════════════════════════════════════════════════════
def mostrar_submenu(bloque: dict):
    nombre     = bloque["nombre"]
    tema       = bloque["tema"]
    ejercicios = bloque["ejercicios"]
    claves     = sorted(ejercicios.keys(), key=int)

    while True:
        limpiar(); ocultar_cursor()
        cols  = get_cols(); filas = get_filas()
        ancho = max(56, min(80, cols - 2))
        inter = ancho - 2
        x_ini = max(1, (cols - ancho) // 2 + 1)
        x_fin = x_ini + ancho - 1
        alto  = len(ejercicios) + 8
        y_ini = max(2, (filas - alto) // 2)
        cb    = Color.MAGENTA

        gotoxy(x_ini, y_ini - 1)
        partes = [c("[Inicio]", Color.CIAN), c(f"[{nombre}]", Color.CIAN)]
        w(f"  {c('❯',Color.GRIS)} " + f"  {c('❯',Color.GRIS)}  ".join(partes))

        y = y_ini
        borde_h(x_ini, y, ancho, TL, TR, cb); y += 1
        paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
        fila_centrada(x_ini, inter, y,
                      _trunc_visual(f"✦  {nombre.upper()}  —  {tema.upper()}  ✦", inter-4),
                      BOLD + Color.AMARILLO)
        y += 1; borde_h(x_ini, y, ancho, ML, MR, cb)

        et = inter - 28
        for k in claves:
            desc = _trunc_visual(ejercicios[k]["desc"], max(10, et))
            y += 1
            paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
            linea = (f"  {c('[',Color.AMARILLO+BOLD)}{c(k,Color.BLANCO)}"
                     f"{c(']',Color.AMARILLO+BOLD)}  "
                     f"{c(f'Ejercicio {k:<3}',Color.BLANCO)}  "
                     f"{c('│',Color.GRIS)}  {c(desc,Color.GRIS)}")
            gotoxy(x_ini+1, y); w(linea)

        y += 1; borde_h(x_ini, y, ancho, ML, MR, cb); y += 1
        paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
        gotoxy(x_ini+1, y)
        w(f"  {c('[',Color.AMARILLO+BOLD)}{c('0',Color.ROJO)}"
          f"{c(']',Color.AMARILLO+BOLD)}  {c('Regresar al Menú Principal',Color.ROJO)}")
        y += 1; borde_h(x_ini, y, ancho, BL, BR, cb)

        y_prompt = y + 2; mostrar_cursor()
        while True:
            gotoxy(x_ini, y_prompt); w(" "*(ancho+4))
            gotoxy(x_ini, y_prompt)
            w(f"  {c('▶',Color.VERDE)}  {c('Elige ejercicio: ',Color.BLANCO)}")
            op = sys.stdin.readline().rstrip("\n").strip()
            if op == "0": return
            elif op in ejercicios:
                _ejecutar_en_marco(ejercicios[op]); break
            else:
                gotoxy(x_ini, y_prompt); w(" "*(ancho+4))
                gotoxy(x_ini, y_prompt)
                w(f"  {c('✘',Color.ROJO)}  "
                  f"{c(f'Opción inválida — elige 1-{max(claves,key=int)} o 0',Color.ROJO)}")
                sys.stdout.flush(); time.sleep(0.9)


# ════════════════════════════════════════════════════════════
#  MENÚ PRINCIPAL
# ════════════════════════════════════════════════════════════
def mostrar_menu_principal(bloques: dict):
    while True:
        limpiar(); ocultar_cursor()
        cols  = get_cols(); filas = get_filas()
        ancho = max(58, min(80, cols - 2))
        inter = ancho - 2
        x_ini = max(1, (cols - ancho) // 2 + 1)
        x_fin = x_ini + ancho - 1
        alto  = len(bloques) + 8
        y_ini = max(2, (filas - alto) // 2)
        cb    = Color.CIAN
        et    = inter - 28

        y = y_ini
        borde_h(x_ini, y, ancho, TL, TR, cb); y += 1
        paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
        fila_centrada(x_ini, inter, y, "✦  MENÚ PRINCIPAL  ✦", BOLD+Color.AMARILLO)
        y += 1; borde_h(x_ini, y, ancho, ML, MR, cb)

        max_key_w = max(len(k) for k in bloques.keys())
        for key, bloque in bloques.items():
            nombre = _trunc_visual(bloque["nombre"], 10)
            tema   = _trunc_visual(bloque["tema"], max(8, et))
            y += 1
            paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
            key_pad = f"{key:>{max_key_w}}"
            linea = (f"  {c('[',Color.AMARILLO+BOLD)}{c(key_pad,Color.BLANCO)}"
                     f"{c(']',Color.AMARILLO+BOLD)}  "
                     f"{c(f'{nombre:<10}',Color.BLANCO)}  "
                     f"{c('│',Color.GRIS)}  {c(tema,Color.GRIS)}")
            gotoxy(x_ini+1, y); w(linea)

        y += 1; borde_h(x_ini, y, ancho, ML, MR, cb); y += 1
        paredes(x_ini, x_fin, y, cb); limpiar_fila(x_ini, inter, y)
        gotoxy(x_ini+1, y)
        w(f"  {c('[',Color.AMARILLO+BOLD)}{c('S',Color.ROJO)}"
          f"{c(']',Color.AMARILLO+BOLD)}  {c('Salir del programa',Color.ROJO)}")
        y += 1; borde_h(x_ini, y, ancho, BL, BR, cb)

        y_prompt = y + 2; mostrar_cursor()
        while True:
            gotoxy(x_ini, y_prompt); w(" "*(ancho+4))
            gotoxy(x_ini, y_prompt)
            w(f"  {c('▶',Color.VERDE)}  {c('Elige un bloque: ',Color.BLANCO)}")
            op = sys.stdin.readline().rstrip("\n").strip().upper()
            if op == "S":
                limpiar()
                print(f"\n  {c('¡Hasta pronto! Sigue practicando 💪', Color.VERDE+BOLD)}\n")
                return
            elif op in bloques:
                mostrar_submenu(bloques[op]); break
            else:
                gotoxy(x_ini, y_prompt); w(" "*(ancho+4))
                gotoxy(x_ini, y_prompt)
                w(f"  {c('✘',Color.ROJO)}  "
                  f"{c('Opción inválida — ingresa 0-17 o S para salir',Color.ROJO)}")
                sys.stdout.flush(); time.sleep(0.9)
