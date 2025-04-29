import sympy as sp

# Definimos las variables simbólicas
V2, Vo, Vi, C1, C2, R1, R2, R3, s, k = sp.symbols('V2 Vo Vi C1 C2 R1 R2 R3 s k')

# Definimos las ecuaciones
eq1 = V2 * (C1 * s + C2 * s + 1/R2 + 1/R1) - Vo/R2 - Vi/R1 - (C2 * Vo * s)/k
eq2 = (Vo * (C2 * s + 1/R3)) / k - C2 * V2 * s

# Resolver el sistema de ecuaciones para V2 y Vo
solucion = sp.solve([eq1, eq2], (V2, Vo))

# Extraer la solución para Vo
Vo_sol = solucion[Vo]

# Simplificar la expresión de Vo/Vi
funcion_transferencia = sp.simplify(Vo_sol / Vi)

# Manipular la función de transferencia para que tenga la forma deseada
# Dividimos numerador y denominador por el coeficiente de s^2 en el denominador
coeficiente_s2 = C1 * C2 * R1 * R2 * R3

# Simplificar nuevamente
funcion_transferencia = sp.simplify(funcion_transferencia/coeficiente_s2)

print(funcion_transferencia)
# Mostrar la función de transferencia
print("Función de transferencia Vo/Vi:")
sp.pretty_print(funcion_transferencia)

print("Según FT de requerimiento: ")
k1 = k/(C1*R1)
a1 = 1/(C2*R3) + 1/(C2*R3)

'''
# Crear un rango de frecuencias para la gráfica
frequencies = np.logspace(1, 5, 1000)  # De 10 Hz a 100 kHz

# Calcular la respuesta en frecuencia
w, h = signal.freqs(num, den, frequencies)

# Graficar la respuesta en frecuencia
plt.figure()
plt.semilogx(w, 20 * np.log10(abs(h)))  # Eje x en escala logarítmica, y en dB
plt.title("Respuesta en frecuencia del filtro Chebyshev")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Ganancia (dB)")
plt.grid(which='both', axis='both')
plt.axvline(Wp_norm, color='red', linestyle='--', label=f'Frecuencia de corte ({Wp_norm} Hz)')
plt.legend()
plt.show()

''' 