import random


def adivina_numero_pc(x):

      print("=====================")
      print("¡Bienvenido al juego!")
      print("=====================")
      print(
          f"Selecciona un número entre 1 y {x} para que el pc intente adivinar....")

      limite_inferior = 1
      limite_superior = x

      respuesta = ""
      while respuesta != "c":
          if limite_inferior != limite_superior:

              predicción = random.randint(limite_inferior, limite_superior)
          else:
              predicción = limite_inferior  # también podría ser limite_inferior.

          # obtener respuesta del usuario
          respuesta = input(f" prediccion es {predicción}.Si es muy alta,ingresa (A). Si es muy baja,ingresa (B).Si es correcto ingresa (C) ").lower()
              

          if respuesta == "a":
              limite_superior = predicción - 1
          elif respuesta == "b":
              limite_inferior = predicción + 1

      print(f"¡Siiii! la computadora adivinó tú número correctamente :  {predicción}")

  
adivina_numero_pc(10)

          