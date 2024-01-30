import math

def oszthato(osztando):
    oszthatoLista = []
    for oszto in range(2,int(math.sqrt(osztando)+1)):
        if osztando%oszto==0:
            oszthatoLista.append(oszto)
    return oszthatoLista

def kiiras(oszthatoLista):
    print(oszthatoLista, end="")
kiiras(oszthato(10001))



