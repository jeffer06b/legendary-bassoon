def calcular_promedio_temperaturas(datos_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad a partir de datos de múltiples ciudades y semanas.

    Args:
        datos_temperaturas: Un diccionario donde las claves son los nombres de las ciudades
                            y los valores son listas de listas, representando las temperaturas
                            semanales de cada ciudad.  Ejemplo:
                            {'CiudadA': [[20, 22, 21, 23, 24, 25, 22], [21, 23, 20, 22, 25, 24, 23], ...],
                             'CiudadB': [[...], [...] ...], ...}

    Returns:
        Un diccionario donde las claves son los nombres de las ciudades y los valores son las
        temperaturas promedio de cada ciudad.  Devuelve None si los datos son inválidos.
    """

    if not isinstance(datos_temperaturas, dict):
        return None  # Manejo de datos inválidos

    promedios = {}
    for ciudad, temperaturas_semanales in datos_temperaturas.items():
        if not all(isinstance(semana, list) for semana in temperaturas_semanales):
            return None # Manejo de datos inválidos

        temperaturas_totales = []
        for semana in temperaturas_semanales:
            temperaturas_totales.extend(semana)

        if not all(isinstance(temp, (int, float)) for temp in temperaturas_totales):
            return None # Manejo de datos inválidos

        if not temperaturas_totales:
            promedios[ciudad] = 0 # Manejo de caso sin temperaturas
        else:
            promedio = sum(temperaturas_totales) / len(temperaturas_totales)
            promedios[ciudad] = promedio

    return promedios
print(calcular_promedio_temperaturas(datos_temperaturas=
                                     {'CiudadA': [[20, 22, 21, 23], [25, 24, 26, 27], [22, 20, 23, 21],
                                                  [24, 25, 26, 23]],
                                      'CiudadB': [[18, 19, 20, 17], [21, 20, 22, 23], [19, 18, 21, 20],
                                                  [20, 21, 22, 19]],
                                      'CiudadC': [[28, 29, 30, 27], [31, 32, 33, 30], [29, 28, 31, 30],
                                                  [30, 29, 32, 31]]}))