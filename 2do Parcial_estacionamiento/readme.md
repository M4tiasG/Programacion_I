# AutoPark — Sistema de Gestión de Estacionamiento

Aplicación modular en Python desarrollada para el **2.º Examen Parcial** de Programación I — Tecnicatura Superior en Desarrollo de Software (Instituto Roque González).

Permite liquidar el cobro de vehículos tanto **en tiempo real mediante una interfaz gráfica** (ventanilla) como **por lote** a partir de un archivo JSON con los movimientos del día, exportando los resultados a CSV y generando tickets fiscales individuales.

---

## Estructura del proyecto

```
2do Parcial_estacionamiento/
│
├── main.py                 # Único punto de entrada. Inicializa la ventana y las vistas.
├── data/                   # Archivos de entrada estáticos.
│   ├── tarifas.json
│   └── movimientos.json
├── exports/                # Archivos generados por el sistema (se crean automáticamente).
│   ├── Movimientos Procesados/
│   │   ├── liquidacion.csv
│   │   └── rechazados.csv
│   └── Tickets/
│       └── TKT-0000.txt
├── core/                   # Lógica de negocio (Backend).
│   ├── __init__.py
│   ├── calculations.py     # Motor de tarifas (función recursiva de cálculo).
│   ├── validations.py      # Expresiones regulares y limpieza de datos.
│   ├── importation.py      # Lectura y aplanado de los JSON de configuración/movimientos.
│   ├── exportation.py      # Generación de CSV y tickets (TKT-0000.txt).
│   └── process_movements.py # Orquesta el procesamiento por lote.
└── gui/                    # Interfaz de usuario (Frontend — CustomTkinter).
    ├── __init__.py
    ├── app.py               # Ventana principal y referencias globales a los widgets.
    ├── views.py             # Construcción visual de cada sección (labels, botones, entries).
    └── controllers.py       # Funciones conectadas a los eventos de los widgets.
```

---

## Requisitos e instalación
Es necesario instalar **customtkinter** y **CTkMessagebox** para el funcionamiento del programa.

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

---

## Funcionalidad implementada

### 1. Menú principal (GUI)

Al iniciar, se muestra una ventana con tres acciones:
m
- **Cobro en Ventanilla** → abre el formulario de liquidación manual.
- **Procesar lote de movimientos** → lee `data/movimientos.json`, valida y exporta los CSV.
- **Cerrar** → finaliza la aplicación.

### 2. Cobro Manual en Ventanilla

Formulario gráfico con:
- Campo de **patente**, validado contra los formatos tradicional (`AAA000`) y Mercosur (`AA000AA`).
- Menú desplegable de **tipo de vehículo** (`auto`, `moto`, `camioneta`).
- Checkbox **"Estadía de varios días"**: al activarla, habilita el campo de días y deshabilita (y limpia) los campos de horario; al desactivarla, ocurre lo inverso. Si no se completa, el sistema la trata como `0` sin generar errores.
- Campos de **hora de entrada/salida** (`HH:MM`), usados solo cuando la estadía es del mismo día.
- Checkbox de **servicio de lavado**.
- Botón **Liquidar**, que calcula el total, lo muestra en un cartel flotante (`CTkMessagebox`) y permite **imprimir un comprobante** en formato de ticket fiscal (`TKT-0000.txt`), con desglose de estacionamiento base, bonificación por lavado, costo de lavado, IVA discriminado (21%) y subtotal.

### 3. Procesamiento por Lote

Desde el menú principal, procesa `data/movimientos.json` contra `data/tarifas.json`:
- Valida patente, tipo de vehículo, formato de horarios y consistencia (salida posterior a entrada).
- Los movimientos válidos se liquidan y exportan a `liquidacion.csv`.
- Los movimientos inválidos se descartan con su motivo (`"Patente invalida"`, `"Tipo de vehiculo invalido"`, `"Hora de entrada invalida"`, `"Hora de salida invalida"`, `"Hora inconsistente"`) y se exportan a `rechazados.csv`.

---

## Desafíos de Valor Agregado cumplidos

### 🔵 Nivel 2

- **GUI con interfaz gráfica (`CustomTkinter`)** — Se implementó la totalidad del módulo de Cobro Manual en Ventanilla como ventana gráfica: campos de texto para patente y horarios, menú desplegable para tipo de vehículo, checkboxes para lavado y estadía prolongada, y botón de liquidación con cartel flotante y cálculo en tiempo real.
- **Generador de Tickets Fiscales Digitales (`TKT-0000.txt`)** — Cada liquidación manual puede emitir un comprobante individual con numeración correlativa (ceros a la izquierda), encabezado de fantasía (razón social, CUIT, dirección), desglose discriminado de estacionamiento base, bonificación por lavado, servicio de lavado, subtotal e IVA (21%).

---

## Alumno

Georgieff Matías — 2.º Año, Tecnicatura Superior en Desarrollo de Software.
