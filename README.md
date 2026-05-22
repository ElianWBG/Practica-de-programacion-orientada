# 📚 Práctica POO en Python

---

## 👤 Información del Estudiante

| Campo           | Detalle                                  |
|-----------------|------------------------------------------|
| **Nombre**      | Elian Wladimir Galeas Baren              |
| **Materia**     | Programación Orientada a Objetos         |
| **Semestre**    | Sistemas                                 |
| **Universidad** | —                                        |

---

Aplicación de consola interactiva que cubre los **18 bloques** (0–17) de la Guía Práctica 1 de POO en Python.
Cada bloque se ejecuta desde un menú con marco de caja Unicode, visor de código con scroll, contexto informativo y validación de inputs en tiempo real dentro del marco.

---

## 🗂 Estructura del proyecto

```
PracticaPoo/
├── main.py                              ← Punto de entrada. Pantalla de bienvenida y menú principal.
├── controllers/
│   ├── __init__.py
│   └── menu_controller.py               ← Visor de código, inputs pre-renderizados,
│                                           validación en la misma línea (sin saltar).
├── data/
│   ├── __init__.py
│   └── bloques_data.py                  ← Mapa de bloques, ejercicios, inputs y contexto.
├── modules/
│   ├── __init__.py
│   ├── bloque_00_intro.py               ✔ Introducción a la POO
│   ├── bloque_01_constructor.py         ✔ Constructor __init__
│   ├── bloque_02_variables.py           ✔ Variables y Tipos de Datos
│   ├── bloque_03_operadores.py          ✔ Operadores
│   ├── bloque_04_io.py                  ✔ Entrada y Salida
│   ├── bloque_05_condicionales.py       ✔ Condicionales
│   ├── bloque_06_bucles.py              ✔ Bucles
│   ├── bloque_07_funciones.py           ✔ Funciones
│   ├── bloque_08_listas.py              ✔ Listas
│   ├── bloque_09_tuplas.py              ✔ Tuplas
│   ├── bloque_10_diccionarios.py        ✔ Diccionarios
│   ├── bloque_11_conjuntos.py           ✔ Conjuntos (set)
│   ├── bloque_12_excepciones.py         ✔ Excepciones
│   ├── bloque_13_decoradores.py         ✔ Decoradores
│   ├── bloque_14_unpacking.py           ✔ Unpacking
│   ├── bloque_15_orden_superior.py      ✔ Funciones de Orden Superior
│   ├── bloque_16_archivos_json.py       ✔ Archivos y JSON
│   └── bloque_17_mixins.py              ✔ Mixins
└── utils/
    ├── __init__.py
    ├── consola.py                        ← gotoxy, Color, bordes Unicode, spinner,
    │                                       helpers de caja, limpiar, truncar.
    └── decoradores.py                    ← @validar, @requiere_positivo,
                                            @capturar_errores, @log_llamada,
                                            @medir_tiempo, input_int/float/str.
```

---

## 🚀 Cómo ejecutar

```bash
cd PracticaPoo
python main.py
```

> Requiere **Python 3.10+**.
> Se recomienda una terminal de al menos **80 columnas** para visualizar correctamente el marco y el visor de código.

---

## 🖥 Interfaz

| Elemento             | Descripción                                                                    |
|----------------------|--------------------------------------------------------------------------------|
| **Pantalla de bienvenida** | Marco centrado con nombre del proyecto, spinner de carga y datos del autor |
| **Menú principal**   | Caja doble `╔═╗` con todos los bloques numerados                               |
| **Visor de código**  | Muestra 10 líneas del archivo fuente con numeración; scroll con `W↑` / `S↓`   |
| **Contexto previo**  | Líneas informativas `ℹ` dibujadas antes de los inputs cuando el ejercicio lo requiere |
| **Inputs en marco**  | Todos los prompts se pre-renderizan de una sola vez; los errores reescriben la misma línea sin generar nueva |
| **Colores ANSI**     | Cyan = info, Verde = ok/retorno, Rojo = error, Amarillo = nombres, Magenta = autor |

---

## ⌨ Flujo de navegación

```
main.py  →  bienvenida()  →  mostrar_menu_principal(BLOQUES)
                                      │
                              menu_controller.py
                                      │
                              ┌───────┴────────┐
                         Elige bloque     Elige ejercicio
                              │                │
                         bloques_data.py   ejecuta fn()
                         (desc, ruta,      desde el módulo
                          inputs,          correspondiente
                          contexto)
```

---

## 🧩 Componentes principales

### `utils/consola.py`

| Función / Clase  | Responsabilidad                                                   |
|------------------|-------------------------------------------------------------------|
| `gotoxy(x, y)`   | Posiciona el cursor en coordenadas absolutas de la terminal       |
| `limpiar()`       | Limpia la pantalla (`cls` / `clear`)                              |
| `get_cols/filas()`| Detecta el tamaño actual de la terminal                          |
| `Color`          | Clase con constantes ANSI: ROJO, VERDE, AMARILLO, AZUL, CIAN…    |
| `c(texto, color)`| Envuelve texto con color ANSI y lo resetea automáticamente        |
| `borde_h()`      | Dibuja borde horizontal de caja con `gotoxy`                      |
| `paredes()`      | Dibuja columnas laterales `║` en la posición dada                 |
| `fila_centrada()`| Centra texto dentro del ancho interno del marco                   |
| `spinner()`      | Animación de carga con puntos en la línea actual                  |
| `TL TR BL BR H V ML MR` | Caracteres Unicode para caja doble                      |
| `tl tr bl br h v ml mr` | Caracteres Unicode para caja simple                     |

### `utils/decoradores.py`

| Decorador / Función      | Responsabilidad                                                        |
|--------------------------|------------------------------------------------------------------------|
| `@validar(**reglas)`     | Valida tipo y condición de cada argumento declarado                    |
| `@requiere_positivo`     | Lanza `ValueError` si el primer argumento numérico es ≤ 0             |
| `@capturar_errores`      | Retorna `(resultado, None)` o `(None, mensaje_error)` sin propagar     |
| `@log_llamada`           | Imprime nombre de la función, argumentos y valor de retorno            |
| `@medir_tiempo`          | Cronometra la ejecución e imprime el tiempo en milisegundos            |
| `input_int(texto, ...)`  | Input validado para enteros con rango opcional; error en la misma fila |
| `input_float(texto, ...)` | Input validado para flotantes con mínimo opcional                    |
| `input_str(texto, ...)`  | Input validado para texto: no vacío, opciones o solo letras            |

### `controllers/menu_controller.py`

| Función               | Responsabilidad                                                         |
|-----------------------|-------------------------------------------------------------------------|
| Visor de código       | Lee el archivo fuente del ejercicio y lo muestra con 10 líneas + scroll |
| Pre-render de inputs  | Dibuja todos los prompts de golpe antes de capturar el primero          |
| Validación en línea   | Detecta el prefijo `\x01ERR\x01` y sobreescribe la fila con el error   |
| `mostrar_menu_principal()` | Dibuja el menú de bloques y delega en el ejercicio elegido        |

### `data/bloques_data.py`

Registro central de todos los bloques y ejercicios. Cada entrada contiene:

```python
"1": {
    "desc":     "Descripción corta del ejercicio",
    "ruta":     "modules/bloque_XX.py",   # archivo fuente a mostrar en el visor
    "fn":       BloqueXX.ejN,             # función estática a ejecutar
    "inputs":   ["▶  Prompt 1", ...],     # prompts pre-renderizados (lista vacía si no hay)
    "contexto": ["ℹ  Línea informativa"], # contexto previo (lista vacía si no aplica)
}
```

---

## 📋 Patrón de un módulo

```python
# modules/bloque_XX_nombre.py

class BloqueXX:

    @staticmethod
    def ej1_nombre():
        # Lógica del ejercicio.
        # Los inputs se capturan con las funciones de utils/decoradores.py:
        #   input_int(), input_float(), input_str()
        pass

    @staticmethod
    def ej2_nombre(): ...
```

Los prompts correspondientes se declaran en `data/bloques_data.py` bajo la clave `"inputs"`, y el controlador los pre-renderiza en pantalla antes de llamar a la función.

---

## ✅ Estado de avance

| Bloque | Tema                          | Ejercicios                                                                         |
|--------|-------------------------------|------------------------------------------------------------------------------------|
| 00     | Introducción a la POO         | Clases sistema biblioteca · Clase Persona · Clase Auto con métodos                 |
| 01     | Constructor `__init__`        | Clase Producto con validación · Clase Estudiante + classmethods · Clase Libro (3 constructores) |
| 02     | Variables y Tipos             | Tipos simples · Tipos complejos · Slicing de lista · Clase Inventario              |
| 03     | Operadores                    | Aritméticos · == vs is · Precedencia `2+1*2%2+(2**1)//2`                          |
| 04     | Entrada y Salida              | Ficha personal · Calculadora suma/promedio · Error str vs int                      |
| 05     | Condicionales                 | Par o impar · Calificación letra A-D · Login usuario/contraseña · Clasificar vehículo |
| 06     | Bucles                        | While acumular 1-10 · enumerate frutas · Cuadrados pares · Buscar producto         |
| 07     | Funciones                     | doble(x) · *args sumar_varios · Factorial recursivo · Lambdas + map/filter · Recursividad |
| 08     | Listas                        | append/sort/reverse · Estadísticas suma/max/min · Referencia vs copia              |
| 09     | Tuplas                        | Inmutabilidad TypeError · Unpacking con * · Coordenadas (x,y) · Conversión tupla↔lista |
| 10     | Diccionarios                  | Acceso [] y get() · Iterar items() · Referencia vs copia · Dict comprehension x²  |
| 11     | Conjuntos                     | Unión/intersección/diferencia/simétrica · Eliminar duplicados · Diferencia simétrica explicada |
| 12     | Excepciones                   | ValueError con input · IndexError lista · Múltiples excepciones ZeroDivision+ValueError |
| 13     | Decoradores                   | Iniciando/Finalizando · @requiere_positivo · @log_llamada · @validar(**reglas) · @medir_tiempo |
| 14     | Unpacking                     | Unpacking básico *resto · *lista como args de función · Combinar dicts con **      |
| 15     | Funciones de Orden Superior   | map() incrementar · filter() mayores a 3 · reduce() multiplicar · Combinación map+filter+lambda |
| 16     | Archivos y JSON               | Leer/escribir .txt · json.dump/load diccionario · JSON lista usuarios              |
| 17     | Mixins                        | PromedioMixin · ValidacionMixin email y edad · ExportarMixin JSON y CSV            |

---

## 🤖 Registro de uso de IA

> **Herramienta utilizada:** Claude (Anthropic) — `claude.ai`

Se utilizó Claude como apoyo de estudio para comprender los conceptos teóricos de cada bloque, resolver dudas sobre el código, pedir ejemplos adicionales y practicar con ejercicios similares a los de la guía. El proceso seguido en cada bloque fue:

1. Pedir una explicación del tema con ejemplos en Python.
2. Solicitar un ejercicio similar al de la guía para practicar por cuenta propia.
3. Resolver el ejercicio de forma independiente y verificar el resultado con Claude.
4. Repetir el ciclo hasta comprender el concepto completamente.

---

### Bloque 00 — Introducción a la POO

**Prompt de comprensión:**
> "Explícame qué es la programación orientada a objetos y cuál es la diferencia entre una clase y un objeto. Dame un ejemplo sencillo en Python."

**Prompt de proceso similar:**
> "Genera un ejercicio donde identifique 5 clases para modelar un sistema de biblioteca, y luego cree una clase Persona con nombre y edad e instancie 3 objetos."

---

### Bloque 01 — Constructor `__init__`

**Prompt de comprensión:**
> "Explícame cómo funciona __init__ en Python, qué representa self, y cómo agregar validaciones dentro del constructor."

**Prompt de proceso similar:**
> "Dame un ejercicio donde cree una clase Producto con nombre y precio. El constructor debe lanzar ValueError si el precio es negativo. Agrega también un @classmethod desde_diccionario."

---

### Bloque 02 — Variables y Tipos de Datos

**Prompt de comprensión:**
> "Explícame los tipos de datos en Python: int, float, str, bool, None, list, tuple, dict y set. Muéstrame cómo usar slicing en listas con ejemplos paso a paso."

**Prompt de proceso similar:**
> "Crea un ejercicio donde declare al menos una variable de cada tipo, luego cree una lista con 5 elementos y use slicing para obtener sublistas."

---

### Bloque 03 — Operadores

**Prompt de comprensión:**
> "Explícame la diferencia entre == e is en Python con listas, y muéstrame la tabla de precedencia de operadores con un ejemplo numérico resuelto paso a paso."

**Prompt de proceso similar:**
> "Dame un ejercicio que calcule todos los operadores aritméticos con dos números y luego demuestre que == y is son diferentes en dos listas con el mismo contenido."

---

### Bloque 04 — Entrada y Salida

**Prompt de comprensión:**
> "Explícame cómo funciona input() en Python, por qué siempre devuelve str, cómo hacer casting a int y float, y qué error ocurre si intentas sumar el input sin convertirlo."

**Prompt de proceso similar:**
> "Genera un ejercicio donde el usuario ingrese su nombre, edad y altura, y el programa muestre los datos formateados con f-string."

---

### Bloque 05 — Condicionales

**Prompt de comprensión:**
> "Explícame if, elif y else en Python, el operador ternario y el match-case de Python 3.10 con ejemplos concretos de cada uno."

**Prompt de proceso similar:**
> "Crea un ejercicio donde el usuario ingrese un número y el programa determine si es par o impar, y otro donde ingrese una nota y obtenga su letra correspondiente."

---

### Bloque 06 — Bucles

**Prompt de comprensión:**
> "Explícame for y while en Python, la diferencia entre break y continue, cómo funciona enumerate(), y cómo crear listas con list comprehension."

**Prompt de proceso similar:**
> "Dame un ejercicio donde use while para acumular del 1 al 10, y luego use list comprehension para obtener los cuadrados de los números pares del 1 al 10."

---

### Bloque 07 — Funciones

**Prompt de comprensión:**
> "Explícame cómo usar *args en Python, qué son las funciones lambda, y cómo funciona la recursividad con un ejemplo de factorial."

**Prompt de proceso similar:**
> "Genera un ejercicio donde cree una función doble(x), otra con *args que sume varios números, y una función recursiva de factorial."

---

### Bloque 08 — Listas

**Prompt de comprensión:**
> "Explícame la diferencia entre copia = lista y copia = lista.copy() en Python, y muéstrame qué pasa con la lista original si modifico cada tipo de copia."

**Prompt de proceso similar:**
> "Crea un ejercicio donde haga una lista de números, use append, sort y reverse, calcule estadísticas y luego compare referencia vs copia."

---

### Bloque 09 — Tuplas

**Prompt de comprensión:**
> "Explícame por qué las tuplas son inmutables en Python, cómo funciona el unpacking con * para capturar el resto, y cuándo es mejor usar una tupla en vez de una lista."

**Prompt de proceso similar:**
> "Dame un ejercicio donde intente modificar una tupla y capture el TypeError, y luego desempaquete una tupla usando * para el resto de los elementos."

---

### Bloque 10 — Diccionarios

**Prompt de comprensión:**
> "Explícame cómo crear y recorrer diccionarios en Python, la diferencia entre acceder con [] y con get(), y cómo usar dict comprehension."

**Prompt de proceso similar:**
> "Crea un ejercicio donde haga un diccionario, lo recorra con items(), compare referencia vs copia y use dict comprehension para generar cuadrados."

---

### Bloque 11 — Conjuntos

**Prompt de comprensión:**
> "Explícame qué son los conjuntos (set) en Python, cómo funcionan las operaciones de unión, intersección y diferencia, y para qué sirve convertir una lista a set."

**Prompt de proceso similar:**
> "Dame un ejercicio donde cree dos sets, calcule la unión, intersección, diferencia y diferencia simétrica, y luego explique el resultado (A|B)-(A&B)."

---

### Bloque 12 — Excepciones

**Prompt de comprensión:**
> "Explícame cómo funciona try/except/else/finally en Python, cuáles son los tipos de error más comunes, y cómo manejar múltiples excepciones en un mismo bloque."

**Prompt de proceso similar:**
> "Genera un ejercicio donde capture un ValueError al convertir input a entero, un IndexError al acceder a una lista, y un bloque con ZeroDivisionError y ValueError juntos."

---

### Bloque 13 — Decoradores

**Prompt de comprensión:**
> "Explícame cómo funciona un decorador en Python paso a paso: qué es wrapper, cómo se aplica con @, y para qué se usa en proyectos reales."

**Prompt de proceso similar:**
> "Crea un ejercicio donde defina un decorador que imprima 'Iniciando' y 'Finalizando', otro que valide que el argumento sea positivo, y uno que registre el nombre de la función y su retorno."

---

### Bloque 14 — Unpacking

**Prompt de comprensión:**
> "Explícame cómo funciona el unpacking en Python con listas, tuplas y diccionarios, cómo pasar una lista como argumentos con * y cómo combinar dicts con **."

**Prompt de proceso similar:**
> "Dame un ejercicio donde desempaquete una secuencia con *resto, pase una lista como argumentos de función con * y combine dos diccionarios con **."

---

### Bloque 15 — Funciones de Orden Superior

**Prompt de comprensión:**
> "Explícame cómo funcionan map(), filter() y reduce() en Python con ejemplos claros, y cuándo conviene usarlos en lugar de un for."

**Prompt de proceso similar:**
> "Genera un ejercicio donde use map() para incrementar cada elemento, filter() para filtrar mayores a 3, reduce() para multiplicar todos, y los combine con lambda."

---

### Bloque 16 — Archivos y JSON

**Prompt de comprensión:**
> "Explícame cómo leer y escribir archivos de texto en Python con open(), cuáles son los modos 'r', 'w', 'a', y cómo guardar y cargar datos con json.dump y json.load."

**Prompt de proceso similar:**
> "Crea un ejercicio donde escriba y lea un archivo .txt, guarde un diccionario en JSON y lo cargue de vuelta, y trabaje con una lista de usuarios en JSON."

---

### Bloque 17 — Mixins

**Prompt de comprensión:**
> "Explícame qué es un Mixin en Python, para qué se usa, cómo se diferencia de una clase normal, y qué es el MRO (Method Resolution Order) en herencia múltiple."

**Prompt de proceso similar:**
> "Dame un ejercicio donde cree un PromedioMixin para calcular el promedio de notas, un ValidacionMixin para validar email y edad, y un ExportarMixin que genere JSON y CSV."

---

## 📝 Notas finales

- El uso de IA tiene como objetivo aprender a formular buenas preguntas y entender los procesos, no copiar respuestas.
- Cada prompt de "proceso similar" genera un ejercicio nuevo que el estudiante resuelve por su cuenta.
- Todos los ejercicios del proyecto incluyen validaciones de datos.
- Los inputs se validan en tiempo real dentro del marco, reescribiendo la misma línea sin generar nuevas líneas en la terminal.
- El menú principal y el visor de código están implementados en `controllers/menu_controller.py`; el mapa de bloques y ejercicios en `data/bloques_data.py`.
#   P r a c t i c a - d e - p r o g r a m a c i o n - o r i e n t a d a  
 