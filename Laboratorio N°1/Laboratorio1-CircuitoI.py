from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead

from matplotlib import plo

LTR = LTSpiceRawRead("Draft1.ASC")

print(LTR.get_trace_names())
print(LTR.get_raw_property())


import pandas as pd
import matplotlib.pyplot as plt
#from PyLTSpice.LTSpiceBatch import SimCommander

# Nombre del archivo .asc generado por LTspice
archivo_asc = 'Laboratorio1-CircuitoII.asc'

# Lee el archivo .asc utilizando pandas
datos = pd.read_csv(archivo_asc)
print(datos)  # Muestra las primeras filas del dataframe

##datos = pd.read_csv(archivo_asc, comment=';', delim_whitespace=True, skiprows=1, names=['tiempo', 'voltaje'])

# Procesa y analiza los datos según tus necesidades
#print(datos.head())  # Muestra las primeras filas del dataframe

##{
# import re

#def modificar_resistencia(archivo_entrada, archivo_salida, nombre_resistencia, nuevo_valor):
    # Lee el archivo .asc
#    with open(archivo_entrada, 'r') as f:
#        lineas = f.readlines()

    # Busca la línea que contiene la resistencia
#    for i, linea in enumerate(lineas):
#        if nombre_resistencia in linea:
            # Encuentra y modifica el valor de la resistencia
#            nueva_linea = re.sub(r'value=(\d+\.?\d*)', f'value={nuevo_valor}', linea)
#            lineas[i] = nueva_linea

    # Escribe el nuevo archivo .asc
#    with open(archivo_salida, 'w') as f:
#        f.writelines(lineas)

# Modifica la resistencia R1 con un nuevo valor de 10k ohmios
# modificar_resistencia('circuito_original.asc', 'circuito_modificado.asc', 'R1', '10k')
}

##/