vege=0
db=0
min=2147483648
szam=int
while (szam:=int(input("N=")))!=vege:
    if szam < min:
        min=szam
    db+=1
print(f"{db} számból a legkisebb: {min}")