from Szek import Szek

peldany1 = Szek("kék", 13)
peldany2 = Szek("piros", 4)
peldany3 = Szek("zöld", 5)

print(peldany1.__str__())
print(peldany2.__str__())
print(peldany3.__str__())

szekek=[peldany1, peldany2, peldany3]

def osszegzes():
    print("Összesen hány székláb van a teremben: ", end="")
    ossz=0
    for index in range(0, len(szekek),1):
        ossz += szekek[index].labszam
    print(f"{ossz} db")
osszegzes()

def maximumKivalasztas(szekekLista):
    #maximum kivalasztas
    maxLabIndex = 0
    for index in range(1, len(szekek), 1):
        if szekek[maxLabIndex].labszam > szekek[index].labszam:
            maxLabIndex=index
    return szekek[maxLabIndex].szin
maximumKivalasztas()
print(f"A legtöbb lábú szék színe: {maximumKivalasztas()}")

def negynelTobbLabu(szekekLista):
    #megszamlalas
    db=0
    for index in range(0,len(szekek),1):
        if szekek[index].labszam > 4:
            db+=1
    print(f"Négynél több lábú szék: {db} db ")
    return szekek[index].labszam
negynelTobbLabu()

def pirosNegyLabu():
    #eldontes tetele
    van=False
    for index in range(0,len(szekek),1):
        if szekek[index].labszam==4 and szekek[index].szin=="piros":
            van=True
    if van==True:
        print("Van piros 4 lábú szék.")
    else:
        print("Nincsen piros 4 lábú szék.")
pirosNegyLabu()

