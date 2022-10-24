import random 


def adivina_numero (x):
    
    print("=====================")
    print("¡Bienvenido al juego!")
    print("=====================")

    print("Tu meta es adivinar el número genrado por la computadora.")

    numero_aleatorio = random.randint(1,x) #numero entre 1 y x inclusive.

    prediccion = 0
      # El usuario ingresa un número:
    while prediccion != numero_aleatorio:
        prediccion = int(input(f"adivina un número entre 1 y {x}:  "))

        if prediccion < numero_aleatorio :
            print("Intentalo otra vez. Este número es muy pequeño ")
        elif prediccion > numero_aleatorio :
            print("Intentalo otra vez.Este número es demasiado grande.")  


    print(f" ¡Felicidades el número {numero_aleatorio} es correcto! ")  

    
adivina_numero(10)
  