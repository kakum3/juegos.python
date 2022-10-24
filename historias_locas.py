#Cocatenar cadenas de caracteres
#Supongamos que queremos crear una cadena que diga:
#aprende a programar con_________.

# organisacion ="freeCodeCamp"

# print("aprende a programar con" + organisacion)
# print("Aprende a programar con {}" .format(organisacion) )
# print(f"Aprende a programar con {organisacion}")

# Mad Libs (Historias locas)

adj=input("Adjetivo: ")
verbo = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural= input("Sustantivo (plural):  ")

madlib = f" ¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo} problemas. ¡aprende a {verbo2} con freeCodeCamp y alcana tus {sustantivo_plural}! "

print(madlib)