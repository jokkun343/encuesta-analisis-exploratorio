def borrar_valores_atipicos(base_de_datos, columna):
    Q1 = base_de_datos[columna].quantile(0.25)
    Q3 = base_de_datos[columna].quantile(0.75)
    rango = Q3 - Q1

    limite_inferior = Q1 - 1.5 * rango
    limite_superior = Q3 + 1.5 * rango

    valores_sin_atipicos = (base_de_datos[columna] >= limite_inferior) & (base_de_datos[columna] <= limite_superior)
    base_de_datos_filtrada = base_de_datos[valores_sin_atipicos]
    
    return base_de_datos_filtrada