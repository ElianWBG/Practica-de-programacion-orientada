"""
utils/consola.py — Colores, gotoxy, helpers de caja y componentes UX
"""
import os, sys, time, shutil

# ── Cursor & pantalla ────────────────────────────────────────
def gotoxy(x, y):
    sys.stdout.write(f"\033[{y};{x}H"); sys.stdout.flush()

def ocultar_cursor():
    sys.stdout.write("\033[?25l"); sys.stdout.flush()

def mostrar_cursor():
    sys.stdout.write("\033[?25h"); sys.stdout.flush()

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def get_cols():
    return shutil.get_terminal_size((80, 24)).columns

def get_filas():
    return shutil.get_terminal_size((80, 24)).lines

def w(texto):
    sys.stdout.write(texto); sys.stdout.flush()

def truncar(texto, max_len):
    return texto if len(texto) <= max_len else texto[:max_len - 1] + "…"

# ── Códigos ANSI ─────────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"

class Color:
    RESET   = RESET
    BOLD    = BOLD
    ROJO    = "\033[91m"
    VERDE   = "\033[92m"
    AMARILLO= "\033[93m"
    AZUL    = "\033[94m"
    MAGENTA = "\033[95m"
    CIAN    = "\033[96m"
    BLANCO  = "\033[97m"
    GRIS    = "\033[90m"

def c(texto, color):
    return f"{color}{texto}{RESET}"

# Bordes de caja doble
TL="╔"; TR="╗"; BL="╚"; BR="╝"
H ="═"; V ="║"; ML="╠"; MR="╣"
# Bordes de caja simple
tl="┌"; tr="┐"; bl="└"; br="┘"
h ="─"; v ="│"; ml="├"; mr="┤"

# ── Helpers de caja ──────────────────────────────────────────
def borde_h(x, y, ancho, izq, der, color, char=H):
    gotoxy(x, y); w(f"{color}{izq}{char*(ancho-2)}{der}{RESET}")

def paredes(x_ini, x_fin, y, color, char=V):
    gotoxy(x_ini, y); w(f"{color}{char}{RESET}")
    gotoxy(x_fin,  y); w(f"{color}{char}{RESET}")

def limpiar_fila(x_ini, inter, y):
    gotoxy(x_ini+1, y); w(" "*inter)

def fila_centrada(x_ini, inter, y, texto, color=""):
    pad = max(0, (inter - len(texto)) // 2)
    limpiar_fila(x_ini, inter, y)
    gotoxy(x_ini + 1 + pad, y); w(f"{color}{texto}{RESET}")

def fila_texto(x_ini, inter, y, texto, color="", indent=2):
    limpiar_fila(x_ini, inter, y)
    trunc = truncar(texto, inter - indent - 1)
    gotoxy(x_ini + indent, y); w(f"{color}{trunc}{RESET}")

# ── Dimensiones centradas ────────────────────────────────────
def dims(ancho_deseado=72):
    cols  = get_cols()
    ancho = max(52, min(ancho_deseado, cols - 2))
    inter = ancho - 2
    x_ini = max(1, (cols - ancho) // 2 + 1)
    x_fin = x_ini + ancho - 1
    return ancho, inter, x_ini, x_fin

# ── Componentes UX ───────────────────────────────────────────
def spinner(texto, segundos=1.2):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    fin = time.time() + segundos; i = 0
    while time.time() < fin:
        sys.stdout.write(f"\r  {c(frames[i%len(frames)], Color.AMARILLO)}  {c(texto, Color.GRIS)}")
        sys.stdout.flush(); time.sleep(0.1); i += 1
    sys.stdout.write(f"\r  {c('✔', Color.VERDE)}  {c(texto+' listo!', Color.VERDE)}\n")
    sys.stdout.flush()

def breadcrumb(ruta: list, x=None, y=None):
    partes = [c(f"[{p}]", Color.CIAN) for p in ruta]
    linea  = f"  {c('❯', Color.GRIS)} " + f"  {c('❯', Color.GRIS)}  ".join(partes)
    if x and y:
        gotoxy(x, y); w(linea)
    else:
        print(linea)

def ok(texto):      print(f"  {c('✔', Color.VERDE)}  {c(texto, Color.VERDE)}")
def erro(texto):    print(f"  {c('✘', Color.ROJO)}  {c(texto, Color.ROJO)}")
def info(texto):    print(f"  {c('ℹ', Color.CIAN)}  {c(texto, Color.CIAN)}")
def advert(texto):  print(f"  {c('⚠', Color.AMARILLO)}  {c(texto, Color.AMARILLO)}")
def sep():
    ancho, inter, _, _ = dims()
    print(c("  " + "·"*(inter-2), Color.GRIS))
def subtitulo(texto):
    print(f"\n{c('  ◈ '+texto, Color.MAGENTA+BOLD)}\n")
def pausa():
    input(f"\n  {c('[ Presiona ENTER para continuar ]', Color.GRIS)}")
