# Ejercicio 2

import random

nota = int(random.random() * 10)

if nota <= 3: print(f"Desaprobado, la nota es: {nota}")
elif nota <= 5: print(f"Aprobado, la nota es {nota}")
else: print(f"Promocion directa, la nota es: {nota}")