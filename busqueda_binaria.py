import random
import time


def busqueda_inocente(lista,objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista,objetivo,limite_inferior=None,limite_superior=None):
    if limite_inferior is None:
        limite_inferior= 0
    if limite_superior is None:
        limite_superior=len(lista)-1

    if limite_superior < limite_inferior:
        return -1
    
    punto_medio = (limite_superior + limite_inferior) // 2

    if lista[punto_medio]== objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista,objetivo, limite_inferior,punto_medio-1)
    else:
        return busqueda_binaria(lista,objetivo,punto_medio+1,limite_superior)
    
if __name__== '__main__':
    
  tamaño = 10000
  conjunto_inicial = set()

  while len(conjunto_inicial) < tamaño:
      conjunto_inicial.add(random.randint(-3*tamaño,3*tamaño))

  lista_ordenada = sorted(list(conjunto_inicial))
  #Medir el tiempo de búsqueda ingenua.
  inicio = time.time()
  for objetivo in lista_ordenada:
      busqueda_inocente(lista_ordenada,objetivo)
  fin = time.time()
  print(f"Tiempo de busqueda inocente: {fin-inicio} segundos. ")
    #Medir el tiempo de busqueda binaria.
  inicio = time.time()
  for objetivo in lista_ordenada:
      busqueda_binaria (lista_ordenada,objetivo)
  fin =time.time()
  print(f" Tiempo de búqueda binaria: {fin -inicio} segundos.")



      
    