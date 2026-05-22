"""
data/bloques_data.py — Mapa de bloques y ejercicios
Campos por ejercicio:
  desc     : descripción corta
  ruta     : ruta al archivo fuente
  fn       : función estática a ejecutar
  inputs   : lista de strings con los prompts (para pre-renderizar todos juntos)
             Cada item: "▶  Texto del prompt"
  contexto : (opcional) lista de líneas informativas mostradas antes de los inputs
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from modules.bloque_00_intro         import Bloque00
from modules.bloque_01_constructor   import Bloque01
from modules.bloque_02_variables     import Bloque02
from modules.bloque_03_operadores    import Bloque03
from modules.bloque_04_io            import Bloque04
from modules.bloque_05_condicionales import Bloque05
from modules.bloque_06_bucles        import Bloque06
from modules.bloque_07_funciones     import Bloque07
from modules.bloque_08_listas        import Bloque08
from modules.bloque_09_tuplas        import Bloque09
from modules.bloque_10_diccionarios  import Bloque10
from modules.bloque_11_conjuntos     import Bloque11
from modules.bloque_12_excepciones   import Bloque12
from modules.bloque_13_decoradores   import Bloque13
from modules.bloque_14_unpacking     import Bloque14
from modules.bloque_15_orden_superior import Bloque15
from modules.bloque_16_archivos_json  import Bloque16
from modules.bloque_17_mixins         import Bloque17

_M = "modules"

BLOQUES = {
    "0": {
        "nombre": "Bloque 00", "tema": "Introducción a la POO",
        "ejercicios": {
            "1": {"desc": "Identificar 5 clases para sistema de biblioteca",
                  "ruta": f"{_M}/bloque_00_intro.py", "fn": Bloque00.ej1_clases_biblioteca,
                  "inputs": [], "contexto": []},
            "2": {"desc": "Clase Persona — instanciar 3 objetos",
                  "ruta": f"{_M}/bloque_00_intro.py", "fn": Bloque00.ej2_clase_persona,
                  "inputs": [], "contexto": []},
            "3": {"desc": "Clase Auto con métodos presentarse/arrancar",
                  "ruta": f"{_M}/bloque_00_intro.py", "fn": Bloque00.ej3_clase_auto,
                  "inputs": [], "contexto": []},
        }
    },
    "1": {
        "nombre": "Bloque 01", "tema": "Constructor __init__",
        "ejercicios": {
            "1": {"desc": "Clase Producto con validación de precio",
                  "ruta": f"{_M}/bloque_01_constructor.py", "fn": Bloque01.ej1_producto,
                  "inputs": [], "contexto": []},
            "2": {"desc": "Clase Estudiante + classmethods",
                  "ruta": f"{_M}/bloque_01_constructor.py", "fn": Bloque01.ej2_estudiante,
                  "inputs": [], "contexto": []},
            "3": {"desc": "Clase Libro — 3 constructores alternativos",
                  "ruta": f"{_M}/bloque_01_constructor.py", "fn": Bloque01.ej3_libro,
                  "inputs": [], "contexto": []},
        }
    },
    "2": {
        "nombre": "Bloque 02", "tema": "Variables y Tipos de Datos",
        "ejercicios": {
            "1": {"desc": "Tipos simples (int, float, str, bool, None)",
                  "ruta": f"{_M}/bloque_02_variables.py", "fn": Bloque02.ej1_tipos_simples,
                  "inputs": [], "contexto": []},
            "2": {"desc": "Tipos complejos (list, tuple, dict, set)",
                  "ruta": f"{_M}/bloque_02_variables.py", "fn": Bloque02.ej2_tipos_complejos,
                  "inputs": [], "contexto": []},
            "3": {"desc": "Slicing de lista",
                  "ruta": f"{_M}/bloque_02_variables.py", "fn": Bloque02.ej3_slicing,
                  "inputs": [], "contexto": []},
            "4": {"desc": "Clase Inventario con str, list y dict",
                  "ruta": f"{_M}/bloque_02_variables.py", "fn": Bloque02.ej4_inventario,
                  "inputs": [], "contexto": []},
        }
    },
    "3": {
        "nombre": "Bloque 03", "tema": "Operadores",
        "ejercicios": {
            "1": {"desc": "Operadores aritméticos",
                  "ruta": f"{_M}/bloque_03_operadores.py", "fn": Bloque03.ej1_aritmeticos,
                  "inputs": [], "contexto": []},
            "2": {"desc": "== vs is — comparación vs identidad",
                  "ruta": f"{_M}/bloque_03_operadores.py", "fn": Bloque03.ej2_comparacion_is,
                  "inputs": [], "contexto": []},
            "3": {"desc": "Precedencia: 2+1*2%2+(2**1)//2",
                  "ruta": f"{_M}/bloque_03_operadores.py", "fn": Bloque03.ej3_precedencia,
                  "inputs": [], "contexto": []},
        }
    },
    "4": {
        "nombre": "Bloque 04", "tema": "Entrada y Salida (input/print)",
        "ejercicios": {
            "1": {"desc": "Ficha personal — nombre, edad, altura",
                  "ruta": f"{_M}/bloque_04_io.py", "fn": Bloque04.ej1_ficha_personal,
                  "inputs": ["▶  Ingrese su nombre",
                              "▶  Ingrese su edad (0–120)",
                              "▶  Ingrese su altura (ej 1.75)"],
                  "contexto": []},
            "2": {"desc": "Calculadora — suma y promedio de dos números",
                  "ruta": f"{_M}/bloque_04_io.py", "fn": Bloque04.ej2_calculadora,
                  "inputs": ["▶  Ingrese primer número",
                              "▶  Ingrese segundo número"],
                  "contexto": []},
            "3": {"desc": "Error str vs int — concatenación sin castear",
                  "ruta": f"{_M}/bloque_04_io.py", "fn": Bloque04.ej3_error_str,
                  "inputs": ["▶  Ingrese un número"],
                  "contexto": ["ℹ  Escribe cualquier número. Verás la diferencia",
                                "   entre concatenar strings y sumar enteros."]},
        }
    },
    "5": {
        "nombre": "Bloque 05", "tema": "Condicionales",
        "ejercicios": {
            "1": {"desc": "Par o impar",
                  "ruta": f"{_M}/bloque_05_condicionales.py", "fn": Bloque05.ej1_par_impar,
                  "inputs": ["▶  Ingrese un número"],
                  "contexto": []},
            "2": {"desc": "Calificación letra A-D",
                  "ruta": f"{_M}/bloque_05_condicionales.py", "fn": Bloque05.ej2_calificacion,
                  "inputs": ["▶  Ingrese la nota (0-100)"],
                  "contexto": ["ℹ  Escala:  90-100 → A  |  80-89 → B  |  70-79 → C  |  0-69 → D"]},
            "3": {"desc": "Sistema de login usuario/contraseña",
                  "ruta": f"{_M}/bloque_05_condicionales.py", "fn": Bloque05.ej3_login,
                  "inputs": ["▶  Usuario",
                              "▶  Contraseña"],
                  "contexto": ["ℹ  Credenciales válidas:  usuario=admin  |  contraseña=123"]},
            "4": {"desc": "Clasificar vehículo por tipo y velocidad",
                  "ruta": f"{_M}/bloque_05_condicionales.py", "fn": Bloque05.ej4_clasificar_vehiculo,
                  "inputs": ["▶  Tipo de vehículo (auto/moto/camion/bus)",
                              "▶  Velocidad actual (km/h)",
                              "▶  Años de antigüedad"],
                  "contexto": ["ℹ  Tipos válidos:  auto  |  moto  |  camion  |  bus",
                                "ℹ  Velocidad:  <60 baja  |  60-120 normal  |  >120 exceso"]},
        }
    },
    "6": {
        "nombre": "Bloque 06", "tema": "Bucles (for/while)",
        "ejercicios": {
            "1": {"desc": "While — acumular 1 al 10",
                  "ruta": f"{_M}/bloque_06_bucles.py", "fn": Bloque06.ej1_while_1_10,
                  "inputs": [], "contexto": []},
            "2": {"desc": "Enumerate de lista de frutas",
                  "ruta": f"{_M}/bloque_06_bucles.py", "fn": Bloque06.ej2_enumerate_frutas,
                  "inputs": [], "contexto": []},
            "3": {"desc": "Cuadrados de números pares (1-10)",
                  "ruta": f"{_M}/bloque_06_bucles.py", "fn": Bloque06.ej3_cuadrados_pares,
                  "inputs": [], "contexto": []},
            "4": {"desc": "Buscar producto en lista con for",
                  "ruta": f"{_M}/bloque_06_bucles.py", "fn": Bloque06.ej4_buscar_producto,
                  "inputs": ["▶  Producto a buscar"],
                  "contexto": ["ℹ  Productos disponibles:",
                                "   laptop  |  mouse  |  teclado  |  monitor  |  audífonos"]},
        }
    },
    "7": {
        "nombre": "Bloque 07", "tema": "Funciones",
        "ejercicios": {
            "1": {"desc": "Función doble(x)",
                  "ruta": f"{_M}/bloque_07_funciones.py", "fn": Bloque07.ej1_doble,
                  "inputs": [], "contexto": []},
            "2": {"desc": "*args — sumar_varios()",
                  "ruta": f"{_M}/bloque_07_funciones.py", "fn": Bloque07.ej2_sumar_varios,
                  "inputs": [], "contexto": []},
            "3": {"desc": "Factorial recursivo",
                  "ruta": f"{_M}/bloque_07_funciones.py", "fn": Bloque07.ej3_factorial,
                  "inputs": [], "contexto": []},
            "4": {"desc": "Lambdas + map/filter",
                  "ruta": f"{_M}/bloque_07_funciones.py", "fn": Bloque07.ej4_lambdas,
                  "inputs": [], "contexto": []},
            "5": {"desc": "Recursividad: factorial y sumar_hasta",
                  "ruta": f"{_M}/bloque_07_funciones.py", "fn": Bloque07.ej5_recursividad,
                  "inputs": [], "contexto": []},
        }
    },
    "8": {
        "nombre": "Bloque 08", "tema": "Listas",
        "ejercicios": {
            "1": {"desc": "Métodos de lista: append, sort, reverse",
                  "ruta": f"{_M}/bloque_08_listas.py", "fn": Bloque08.ej1_metodos_lista,
                  "inputs": [], "contexto": []},
            "2": {"desc": "Estadísticas: suma, max, min",
                  "ruta": f"{_M}/bloque_08_listas.py", "fn": Bloque08.ej2_estadisticas,
                  "inputs": [], "contexto": []},
            "3": {"desc": "Referencia vs copia de lista",
                  "ruta": f"{_M}/bloque_08_listas.py", "fn": Bloque08.ej3_referencia_vs_copia,
                  "inputs": [], "contexto": []},
        }
    },
    "9": {
        "nombre": "Bloque 09", "tema": "Tuplas",
        "ejercicios": {
            "1": {"desc": "Inmutabilidad — TypeError al modificar",
                  "ruta": f"{_M}/bloque_09_tuplas.py", "fn": Bloque09.ej1_inmutabilidad,
                  "inputs": [], "contexto": []},
            "2": {"desc": "Unpacking con * (resto)",
                  "ruta": f"{_M}/bloque_09_tuplas.py", "fn": Bloque09.ej2_unpacking,
                  "inputs": [], "contexto": []},
            "3": {"desc": "Recorrer coordenadas (x,y)",
                  "ruta": f"{_M}/bloque_09_tuplas.py", "fn": Bloque09.ej3_coordenadas,
                  "inputs": [], "contexto": []},
            "4": {"desc": "Conversión tupla ↔ lista",
                  "ruta": f"{_M}/bloque_09_tuplas.py", "fn": Bloque09.ej4_conversion,
                  "inputs": [], "contexto": []},
        }
    },
    "10": {
        "nombre": "Bloque 10", "tema": "Diccionarios",
        "ejercicios": {
            "1": {"desc": "Acceso con [] y get()",
                  "ruta": f"{_M}/bloque_10_diccionarios.py", "fn": Bloque10.ej1_acceso,
                  "inputs": [], "contexto": []},
            "2": {"desc": "Iterar con items()",
                  "ruta": f"{_M}/bloque_10_diccionarios.py", "fn": Bloque10.ej2_iterar,
                  "inputs": [], "contexto": []},
            "3": {"desc": "Referencia vs copia de dict",
                  "ruta": f"{_M}/bloque_10_diccionarios.py", "fn": Bloque10.ej3_referencia_copia,
                  "inputs": [], "contexto": []},
            "4": {"desc": "Dict comprehension x²",
                  "ruta": f"{_M}/bloque_10_diccionarios.py", "fn": Bloque10.ej4_comprehension,
                  "inputs": [], "contexto": []},
        }
    },
    "11": {
        "nombre": "Bloque 11", "tema": "Conjuntos (set)",
        "ejercicios": {
            "1": {"desc": "Unión, intersección, diferencia, simétrica",
                  "ruta": f"{_M}/bloque_11_conjuntos.py", "fn": Bloque11.ej1_operaciones,
                  "inputs": [], "contexto": []},
            "2": {"desc": "Eliminar duplicados de lista",
                  "ruta": f"{_M}/bloque_11_conjuntos.py", "fn": Bloque11.ej2_eliminar_duplicados,
                  "inputs": [], "contexto": []},
            "3": {"desc": "(A|B)-(A&B) diferencia simétrica explicada",
                  "ruta": f"{_M}/bloque_11_conjuntos.py", "fn": Bloque11.ej3_diferencia_simetrica,
                  "inputs": [], "contexto": []},
        }
    },
    "12": {
        "nombre": "Bloque 12", "tema": "Excepciones (try/except)",
        "ejercicios": {
            "1": {"desc": "ValueError con input()",
                  "ruta": f"{_M}/bloque_12_excepciones.py", "fn": Bloque12.ej1_value_error,
                  "inputs": ["▶  Ingresa un número entero"],
                  "contexto": ["ℹ  Escribe texto (ej: 'abc') para provocar el ValueError,",
                                "   o un número para ver el caso exitoso."]},
            "2": {"desc": "IndexError — índice fuera de rango",
                  "ruta": f"{_M}/bloque_12_excepciones.py", "fn": Bloque12.ej2_index_error,
                  "inputs": [], "contexto": []},
            "3": {"desc": "Múltiples excepciones: ZeroDivision, ValueError",
                  "ruta": f"{_M}/bloque_12_excepciones.py", "fn": Bloque12.ej3_multiples,
                  "inputs": [], "contexto": []},
        }
    },
    "13": {
        "nombre": "Bloque 13", "tema": "Decoradores",
        "ejercicios": {
            "1": {"desc": "Decorador 'Iniciando / Finalizando'",
                  "ruta": f"{_M}/bloque_13_decoradores.py", "fn": Bloque13.ej1_decorador_inicio,
                  "inputs": [], "contexto": []},
            "2": {"desc": "@requiere_positivo — validar argumento",
                  "ruta": f"{_M}/bloque_13_decoradores.py", "fn": Bloque13.ej2_validar_positivo,
                  "inputs": [], "contexto": []},
            "3": {"desc": "@log_llamada — registrar nombre y retorno",
                  "ruta": f"{_M}/bloque_13_decoradores.py", "fn": Bloque13.ej3_log,
                  "inputs": [], "contexto": []},
            "4": {"desc": "@validar(**reglas) — tipo + condición por arg",
                  "ruta": f"{_M}/bloque_13_decoradores.py", "fn": Bloque13.ej4_validar_kwargs,
                  "inputs": [], "contexto": []},
            "5": {"desc": "@medir_tiempo — cronometrar ejecución",
                  "ruta": f"{_M}/bloque_13_decoradores.py", "fn": Bloque13.ej5_medir_tiempo,
                  "inputs": [], "contexto": []},
        }
    },
    "14": {
        "nombre": "Bloque 14", "tema": "Unpacking",
        "ejercicios": {
            "1": {"desc": "Unpacking básico con *resto",
                  "ruta": f"{_M}/bloque_14_unpacking.py", "fn": Bloque14.ej1_unpacking_basico,
                  "inputs": [], "contexto": []},
            "2": {"desc": "*lista como argumentos de función",
                  "ruta": f"{_M}/bloque_14_unpacking.py", "fn": Bloque14.ej2_args_lista,
                  "inputs": [], "contexto": []},
            "3": {"desc": "Combinar dos dicts con **",
                  "ruta": f"{_M}/bloque_14_unpacking.py", "fn": Bloque14.ej3_combinar_dicts,
                  "inputs": [], "contexto": []},
        }
    },
    "15": {
        "nombre": "Bloque 15", "tema": "Funciones de Orden Superior",
        "ejercicios": {
            "1": {"desc": "map() — incrementar cada elemento",
                  "ruta": f"{_M}/bloque_15_orden_superior.py", "fn": Bloque15.ej1_map,
                  "inputs": [], "contexto": []},
            "2": {"desc": "filter() — filtrar mayores a 3",
                  "ruta": f"{_M}/bloque_15_orden_superior.py", "fn": Bloque15.ej2_filter,
                  "inputs": [], "contexto": []},
            "3": {"desc": "reduce() — multiplicar todos",
                  "ruta": f"{_M}/bloque_15_orden_superior.py", "fn": Bloque15.ej3_reduce,
                  "inputs": [], "contexto": []},
            "4": {"desc": "Combinación map + filter + lambda",
                  "ruta": f"{_M}/bloque_15_orden_superior.py", "fn": Bloque15.ej4_combinacion,
                  "inputs": [], "contexto": []},
        }
    },
    "16": {
        "nombre": "Bloque 16", "tema": "Archivos y JSON",
        "ejercicios": {
            "1": {"desc": "Leer y escribir archivo .txt",
                  "ruta": f"{_M}/bloque_16_archivos_json.py", "fn": Bloque16.ej1_texto,
                  "inputs": [], "contexto": []},
            "2": {"desc": "Guardar y cargar diccionario JSON",
                  "ruta": f"{_M}/bloque_16_archivos_json.py", "fn": Bloque16.ej2_json_dict,
                  "inputs": [], "contexto": []},
            "3": {"desc": "JSON lista de usuarios — filtrar nombres",
                  "ruta": f"{_M}/bloque_16_archivos_json.py", "fn": Bloque16.ej3_json_lista,
                  "inputs": [], "contexto": []},
        }
    },
    "17": {
        "nombre": "Bloque 17", "tema": "Mixins",
        "ejercicios": {
            "1": {"desc": "PromedioMixin — calcular promedio de notas",
                  "ruta": f"{_M}/bloque_17_mixins.py", "fn": Bloque17.ej1_promedio_mixin,
                  "inputs": [], "contexto": []},
            "2": {"desc": "ValidacionMixin — email y edad",
                  "ruta": f"{_M}/bloque_17_mixins.py", "fn": Bloque17.ej2_validacion_mixin,
                  "inputs": [], "contexto": []},
            "3": {"desc": "ExportarMixin — JSON y CSV",
                  "ruta": f"{_M}/bloque_17_mixins.py", "fn": Bloque17.ej3_exportar_mixin,
                  "inputs": [], "contexto": []},
        }
    },
}
