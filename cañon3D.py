import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import random
import numpy as np

# Parámetros del lanzamiento
num_balas = 1000  # Número de balas a lanzar
intervalo_tiempo = 0.02  # Intervalo de tiempo para la simulación en segundos (ajustado para una animación más suave)

# Función para calcular la trayectoria de las bolas lanzadas por el cañón
def calcular_trayectoria(angulo, velocidad_inicial, tiempo):
    angulo_rad = math.radians(angulo)
    velocidad_x = velocidad_inicial * math.cos(angulo_rad)
    velocidad_y = velocidad_inicial * math.sin(angulo_rad)

    posicion_x = velocidad_x * tiempo
    posicion_y = velocidad_y * tiempo - 0.5 * 9.81 * tiempo ** 2  # Aceleración debido a la gravedad

    # Calcular la velocidad en cada instante de tiempo
    velocidad = math.sqrt(velocidad_x**2 + (velocidad_y - 9.81 * tiempo)**2)

    return posicion_x, posicion_y, velocidad

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(num_balas):
    # Generar valores aleatorios para el ángulo y la velocidad
    angulo_lanzamiento = random.uniform(30, 75)  # Limitamos el ángulo para que no apunte directamente hacia arriba o abajo
    velocidad_lanzamiento = random.uniform(1e-6, 5e-6)

    tiempo_actual = 0
    distancia_recorrida = 0
    velocidad_maxima = 0

    x_vals, y_vals, z_vals = [], [], []

    while tiempo_actual <= 2:  # Simulamos 2 segundos de trayectoria
        # Calcular la posición de la bola en el tiempo actual
        posicion_x, posicion_y, velocidad = calcular_trayectoria(angulo_lanzamiento, velocidad_lanzamiento, tiempo_actual)

        x_vals.append(posicion_y)
        y_vals.append(tiempo_actual)
        z_vals.append(posicion_x)

        tiempo_actual += intervalo_tiempo
        distancia_recorrida = tiempo_actual * velocidad  # La distancia en metros
        if velocidad > velocidad_maxima:
            velocidad_maxima = velocidad

    # Mostrar los resultados después de cada trayectoria completada
    print(f"Bala {i + 1}:")
    print(f"Ángulo de lanzamiento: {angulo_lanzamiento:.2f} grados")
    print(f"Velocidad de lanzamiento: {velocidad_lanzamiento:.2e} segundos")
    print(f"Distancia recorrida: {distancia_recorrida:.2f} metros")
    print(f"Velocidad máxima: {velocidad_maxima:.2f} m/s")
    print("")

    # Dibujar la trayectoria de la bala
    ax.plot(x_vals, y_vals, z_vals)

ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Distancia (m)')
ax.set_zlabel('Altura (m)')
ax.set_title('Trayectorias de las balas lanzadas por el cañón')

plt.show()