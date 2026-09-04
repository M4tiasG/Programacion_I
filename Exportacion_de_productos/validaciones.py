def normalizar_y_validar(productos, usuarios_validos):
    """Revisa los datos, los corrige o los rechaza si son inválidos."""
    productos_validos = []
    productos_rechazados = []
    ids_vistos = set()

    for p in productos:
        motivos_rechazo = []
        prod_id = p.get('id')
        nombre = p.get('nombre')

        # Validación de ID y duplicados
        if prod_id is None:
            motivos_rechazo.append("ID faltante")
        elif prod_id in ids_vistos:
            motivos_rechazo.append(f"ID duplicado ({prod_id})")
        else:
            ids_vistos.add(prod_id)

        # Validación de usuario
        if p.get('id_usuario') not in usuarios_validos:
            motivos_rechazo.append(f"Usuario inválido o inexistente ({p.get('id_usuario')})")

        # Normalización de Nombre
        if not nombre or not isinstance(nombre, str) or not nombre.strip():
            motivos_rechazo.append("Nombre vacío o inválido")
        else:
            p['nombre'] = nombre.strip()

        # Normalización de Categoría
        categoria = p.get('categoria')
        if not categoria or str(categoria).strip() == "" or categoria == "null":
            p['categoria'] = "Sin categoría"
        else:
            p['categoria'] = str(categoria).strip()

        # Normalización y validación de Precio
        try:
            if p.get('precio') is None or str(p.get('precio')).strip() == "":
                raise ValueError
            p['precio'] = float(p.get('precio'))
        except ValueError:
            motivos_rechazo.append("Precio inválido o faltante")

        # Normalización y validación de Stock
        try:
            if p.get('stock') is None or str(p.get('stock')).strip() == "":
                raise ValueError
            p['stock'] = int(p.get('stock'))
        except ValueError:
            motivos_rechazo.append("Stock inválido o faltante")

        # Separar válidos de rechazados
        if motivos_rechazo:
            nombre_mostrar = nombre.strip() if isinstance(nombre, str) and nombre.strip() else f"ID {prod_id}"
            productos_rechazados.append({
                "producto": nombre_mostrar,
                "motivos": ", ".join(motivos_rechazo)
            })
        else:
            productos_validos.append(p)
    return productos_validos, productos_rechazados