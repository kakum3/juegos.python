import random
def jugar ():
    usuario = input("Escoge una opción: 'pi' para piedra 'ti' para tijera 'pa' para papel. \n").lower()
    computadora = random.choice(['pi','pa','ti'])

    if usuario == computadora:
        return 'Empate!'
    
    if ganó_el_jugador(usuario,computadora):
        return 'Ganaste!'
    
    return 'Perdiste!'


def ganó_el_jugador(jugador,oponente):
    if ((jugador == 'pi'and oponente == 'ti')
        or(jugador =='pa'and oponente == 'pi')
        or(jugador == 'ti'and oponente == 'pa')):
        return True
    else:
        return False
    

print (jugar())   

         
      