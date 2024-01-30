from Szek import Szek

def peldanyookListaban():
    soraim=[]
    beolvasas=open(" szekAdatai.txt", "r", encoding="utf-8")
    beolvasas.readline()
    soraim=beolvasas.readlines()
    for index in range(0,len(soraim),1):
        sor=soraim[index].strip().split("-")
        peldaany=Szek(sor[0],sor[1],sor[2],sor[3])
        szekekLista.append(peldaany)
    beolvasas.close()
    peldany1 = Szek("kék", 13)
    peldany2 = Szek("piros", 4)
    peldany3 = Szek("zöld", 5)
    szekek = [peldany1, peldany2, peldany3]
    return szekek

def listaKiiras(lista):
    for index in range(0,len(szekekLista),1):
        print(lista[index])


#hosszu verzio
szekekLista=peldanyookListaban()
listaKiiras(szekekLista)



