"""
✦ PRÁCTICA POO EN PYTHON ✦
main.py — Punto de entrada
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))

from utils.consola import (
    Color, c, RESET, BOLD, limpiar, spinner,
    ocultar_cursor, mostrar_cursor, gotoxy, w,
    get_cols, get_filas, borde_h, paredes, limpiar_fila, fila_centrada,
    TL, TR, BL, BR, H, V, ML, MR,
)
from data.bloques_data         import BLOQUES
from controllers.menu_controller import mostrar_menu_principal


def bienvenida():
    limpiar()
    print("\n")
    spinner("Iniciando sistema", 1.5)
    limpiar()

    cols  = get_cols()
    filas = get_filas()
    ancho = max(52, min(64, cols - 2))
    inter = ancho - 2
    x_ini = max(1, (cols - ancho) // 2 + 1)
    x_fin = x_ini + ancho - 1
    cb    = Color.CIAN

    ocultar_cursor()
    y = max(2, (filas - 9) // 2)

    borde_h(x_ini, y, ancho, TL, TR, cb);           y += 1
    paredes(x_ini, x_fin, y, cb)
    fila_centrada(x_ini, inter, y, "");              y += 1
    paredes(x_ini, x_fin, y, cb)
    fila_centrada(x_ini, inter, y,
                  "✦  PRÁCTICA POO EN PYTHON  ✦",
                  BOLD + Color.AMARILLO);             y += 1
    paredes(x_ini, x_fin, y, cb)
    fila_centrada(x_ini, inter, y,
                  "Guía Práctica Experimental 1",
                  Color.GRIS);                        y += 1
    paredes(x_ini, x_fin, y, cb)
    fila_centrada(x_ini, inter, y, "");              y += 1
    borde_h(x_ini, y, ancho, ML, MR, cb);           y += 1
    paredes(x_ini, x_fin, y, cb)
    fila_centrada(x_ini, inter, y,
                  "Elian  ·  Sistemas",
                  Color.MAGENTA);                     y += 1
    paredes(x_ini, x_fin, y, cb)
    fila_centrada(x_ini, inter, y, "");              y += 1
    borde_h(x_ini, y, ancho, BL, BR, cb)

    mostrar_cursor()
    print("\n")
    time.sleep(0.8)


if __name__ == "__main__":
    bienvenida()
    mostrar_menu_principal(BLOQUES)
