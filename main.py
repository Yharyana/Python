import math
print("hi git")
#listy
krotka_lista=[1,"malina",21.37,"hamster",None]
print(krotka_lista)
print("pierwsze na liście jest",krotka_lista[0],"i to jest ",type(krotka_lista[0]))
print(f"drugie na liście jest {krotka_lista[1]}")
print(f" to jest długość listy  {len(krotka_lista)}")
print(f"a to jest ostatni element listy za pomocą wywołania -1 {krotka_lista[-1]}")
#slicing
print(f"dwa pierwsze z listy  {krotka_lista[:2]}")
print("pozostałem niż 2 pierwsze z listy ",krotka_lista[2:])
print(f"dwa ostatnie bez reszty {krotka_lista[-2:]}")
#dodawanie odmejmowanie iot

krotka_lista.append("ale checa pojawiłem sie")
krotka_lista.insert(0,"ale checa wephcnołem sie na 1 miejsce")
print(krotka_lista)
del krotka_lista[2]
print("nie lubiłem malin wiec je usunołem",krotka_lista)
nonetyp=krotka_lista.pop(4)
print(" to jest none typ",nonetyp)
print(krotka_lista)
krotka_lista.remove(1)
print(krotka_lista)
krotka_lista[-1]="teraz ja jestem ostatni"
name="muhhamed"
print("pierwsza litera imienia",name[0])
print("ostatnia litera imienia",name[-1])
name="n"+name[1:] #to jest w usmie utworzenie nowego napisu przypisanny do starej zmiennej ale to dygresja juz
print[name]
