"""
Descripción del desafío

En esta oportunidad, se cuenta con 2 archivos (.xlsx), donde cada uno representa la generación de energía en una planta
solar de 1 día completo, dividida por inversor. La relación entre inversor y planta es de muchos a uno, es decir,
una planta está relacionada a 1 o más inversores.

El desafío es poder procesar los archivos tomando en cuenta que en la realidad pueden haber 1000 archivos a procesarse.

Para cada archivo, se solicita lo siguiente:

1) Generar un gráfico, un line chart donde el eje x sea la fecha y el eje y sea el active power para finalmente guardarlo.

2) Guardar en un (.txt) la suma por día del active power, el valor máximo y mínimo del active_power y por último,
la ruta donde se encuentra el grafico generado en 1).

3) Imprimir en consola la suma total del active power por día, de todas las plantas.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def buscar_valores(datos):

    # Crear una lista por dia

    valores_dias = []

    # Recorrer valores de energia lectura_1 y sumar sus valores

    total_energia = 0

    for valor in datos:
        valores_dias.append(int(valor))
        total_energia += int(valor)

    # Valores maximo y minimo

    mayor = max(valores_dias)
    menor = min(valores_dias)

    # Devolver los valores

    return total_energia, mayor, menor


def guardar_datos(datos_power, datos_fecha):

    lista_datos_puros = [int(i) for i in datos_power if not pd.isna(
        i) and type(i) != type("dato")]
    lista_datos = [i for i in datos_power]
    lista_fechas = [i for i in datos_fecha]

    diccionario_datos = dict(zip(lista_fechas, lista_datos))

    direccionario_limpio = {}

    for i in diccionario_datos:
        if not pd.isna(diccionario_datos[i]) and type(diccionario_datos[i]) != type("dato"):
            direccionario_limpio[i] = diccionario_datos[i]
        else:
            pass

    return lista_datos_puros, direccionario_limpio


def grabar(rut, max_1, min_1, tota_1, max_2, min_2, tota_2):
    archivo = open('datos.txt', 'a')
    archivo.write(
        f'''el "active power" de la planta 1 del dia es: {tota_1}, su maximo fue de: {max_1} y su minimo due de {min_1}' y el grafico de este dia esta en la direccion: {rut}\n''')
    archivo.write(
        f'''el "active power" de la planta 2 del dia es: {tota_2}, su maximo fue de: {max_2} y su minimo due de {min_2}' y el grafico de este dia esta en la direccion: {rut}\n''')
    archivo.close


def graficar(dccionario):
    myList = dccionario.items()
    myList = sorted(myList)
    x, y = zip(*myList)

    plt.plot(x, y)
    plt.xlabel('Date')
    plt.ylabel('Active_Power')
    plt.title('Desafio')
    plt.show()


ruta = Path("C:/Users/ircdc/Desktop/deafio")

# Rutas de lectura de archivos
ruta_lec_1 = 'data_plantas_python_1_1.xlsx'
ruta_lec_2 = 'data_plantas_python_2.xlsx'

# Leer archivos

lec_1 = pd.read_excel(ruta_lec_1)
lec_2 = pd.read_excel(ruta_lec_2)

# Filtrar valores numericos y devolver listas de dastos limpios y diccionario limpio

lista_power_1, dic_fech_power_1 = guardar_datos(
    lec_1['active_power_im'], lec_1['fecha_im'])
lista_power_2, dic_fech_power_2 = guardar_datos(
    lec_2['active_power_im'], lec_2['fecha_im'])

# Buscar valores con funcion

total_energia_1, valor_max_1, valor_min_1 = buscar_valores(lista_power_1)
total_energia_2, valor_max_2, valor_min_2 = buscar_valores(lista_power_2)

# Creamos txt y grabamos todas las variables

grabar(ruta, valor_max_1, valor_min_1, total_energia_1,
       valor_max_2, valor_min_2, total_energia_2)

# Reunimos datos para graficar

graficar(dic_fech_power_1)
graficar(dic_fech_power_2)

# Imprimit en pantalla la totalidad de la potencia activa de las plantas entregadas

total_potencia_activa = total_energia_1 + total_energia_2

print(
    f'Total potencia activa entre planta 1 y 2 es de: {total_potencia_activa}')
