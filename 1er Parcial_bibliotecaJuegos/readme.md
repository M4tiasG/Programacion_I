# 1er Parcial de progamación - Sistema de Biblioteca de Videojuegos 🎮

Este proyecto es un programa de consola desarrollada en Python que permite administrar una biblioteca temática de videojuegos de manera eficiente, robusta y con una interfaz de usuario en consola limpia y cómoda.

El sistema cumple con todos los requisitos técnicos de integración de fundamentos de Python (estructuras de control, colecciones nativas, modularización, manejo de errores y pruebas).

## Características Principales 🔧
- **Interfaz de Consola Cómoda:** Menú interactivo intuitivo y completamente validado para evitar cierres inesperados.
- **Datos Precargados:** Inicia con videojuegos ya registrados para probar las funcionalidades de inmediato.
- **IDs Autoincrementales:** Generación automática y única de identificadores para cada videojuego.
- **Orden Automático:** Todas las listas y filtros muestran los videojuegos organizados de mayor a menor puntaje de forma obligatoria.

---

## Funcionalidades del Menú
1. **Agregar videojuego:** Validación estricta de campos vacíos, año numérico, puntaje (1 al 10) y géneros válidos.
2. **Listar todos los elementos:** Muestra el catálogo completo ordenado por puntaje descendente.
3. **Buscar por título:** Búsqueda flexible por coincidencia parcial (ignora mayúsculas/minúsculas).
4. **Filtrar por género:** Encuentra títulos asociados a géneros válidos (`rpg`, `aventura`, `sandbox`, `retro`...).
5. **Filtrar por año:** Filtra lanzamientos de un año específico.
6. **Mostrar recomendación aleatoria:** Elige un juego al azar de la biblioteca.
7. **Eliminar elemento:** Borrado seguro mediante el ID numérico, manejando IDs inexistentes.
8. **Salir:** Cierre controlado del programa.