import os
import random
import sys
import time

# Caracteres usados para la lluvia (letras, números y símbolos)
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*+-/<>~"


def get_terminal_size():
  try:
    return os.get_terminal_size().columns, os.get_terminal_size().lines
  except OSError:
    return 80, 24


def main():
  # Limpiar pantalla y ocultar cursor (simulado)
  os.system("cls" if os.name == "nt" else "clear")

  width, height = get_terminal_size()

  # Inicializar la posición de las gotas en cada columna
  drops = [random.randint(0, height) for _ in range(width)]

  print(
      "\033[32m"
  )  # Color verde brillante típico de Matrix (código ANSI de terminal)

  try:
    while True:
      output = []
      for i in range(width):
        if drops[i] < height:
          # Carácter aleatorio brillante
          char = random.choice(CHARS)
          output.append(char)
          drops[i] += 1
        else:
          output.append(" ")
          if random.random() > 0.95:  # Reiniciar la gota aleatoriamente
            drops[i] = 0

      print("".join(output))
      time.sleep(0.05)  # Velocidad de la lluvia

  except KeyboardInterrupt:
    # Restaurar color normal de la terminal al salir
    print("\033[0m")
    sys.exit()


if __name__ == "__main__":
  main()