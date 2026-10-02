from requests import Timeout
import requests

CATALOGO_PRODUCTOS_URL= "https://api.escuelajs.co/api/v1/products"

def obtener_recomendaciones(
    categoria: str | None = None, presupuesto: float | None = None
) -> list[dict]:
    """Obtiene recomendaciones de productos según la categoría/uso 
    y/o presupuesto especificado.

    Args:
        categoria: Categoría, tipo de producto o uso deseado (ej.
          'audífonos', 'gaming', 'trabajo').
        presupuesto: Presupuesto máximo disponible.

    Returns:
        Lista de productos recomendados que se ajustan a la búsqueda.
    """
    catalogo = requests.get(CATALOGO_PRODUCTOS_URL, timeout=10).json()

    recomendaciones = []

    for producto in catalogo:
        # Filtrar por presupuesto si se especifica
        if presupuesto is not None and producto["price"] > presupuesto:
            continue

        # Filtrar por categoría si se especifica
        if categoria:
            cat_lower = categoria.lower().strip()
            titulo_lower = producto["title"].lower()
            desc_lower = producto["description"].lower()
            categoria_lower = producto["category"]["name"].lower()

            coincide = (
                cat_lower in titulo_lower
                or cat_lower in desc_lower
                or cat_lower in categoria_lower
            )
            if not coincide:
                continue

        recomendaciones.append(producto)

    return recomendaciones        