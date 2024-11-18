import math
import random


#esto es para calcular el resultado despues de girar la ruleta, hay que probarlo
NUMEROS = list(range(37))  # Números de 0 a 36
ANGULO_POR_SECTOR = 360 / len(NUMEROS)  # Grados por sector

angulo_inicial = random.uniform(0, 360)  
angulo_giro = random.uniform(720, 1440)  # Girar entre 2 y 4 vueltas
angulo_final = (angulo_inicial + angulo_giro) % 360  

numero_salida = NUMEROS[int(angulo_final // ANGULO_POR_SECTOR)]
print(f"El ángulo final es {angulo_final:.2f}° y el número ganador es {numero_salida}")


