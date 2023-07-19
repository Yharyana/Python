import math
#print("hi git")
#listy
#krotka_lista=[1,"malina",21.37,"hamster",None]
#print(krotka_lista)
#print("pierwsze na liście jest",krotka_lista[0],"i to jest ",type(krotka_lista[0]))
#print(f"drugie na liście jest {krotka_lista[1]}")
#print(f" to jest długość listy  {len(krotka_lista)}")
#print(f"a to jest ostatni element listy za pomocą wywołania -1 {krotka_lista[-1]}")
#slicing
#print(f"dwa pierwsze z listy  {krotka_lista[:2]}")
#print("pozostałem niż 2 pierwsze z listy ",krotka_lista[2:])
#print(f"dwa ostatnie bez reszty {krotka_lista[-2:]}")
#dodawanie odmejmowanie iot

#krotka_lista.append("ale checa pojawiłem sie")
#krotka_lista.insert(0,"ale checa wephcnołem sie na 1 miejsce")
#print(krotka_lista)
#del krotka_lista[2]
#print("nie lubiłem malin wiec je usunołem",krotka_lista)
#nonetyp=krotka_lista.pop(4)
#print(" to jest none typ",nonetyp)
#print(krotka_lista)
#krotka_lista.remove(1)
#print(krotka_lista)
#krotka_lista[-1]="teraz ja jestem ostatni"
#name="muhhamed"
#print("pierwsza litera imienia",name[0])
#print("ostatnia litera imienia",name[-1])
#name="n"+name[1:] #to jest w usmie utworzenie nowego napisu przypisanny do starej zmiennej ale to dygresja juz
#print(name)
#words="to jest zdanie".split(" ")
#print(words)
#print(f"pierwsze słowo to {words[0]}")
#zadania
#favourite_sports=["triatlon","bridge","bobslej"]
#print(f"to jest ulubiony sport który napewno sanm {favourite_sports[0]} a to jest mój znienadziwony {favourite_sports[-1]}")
#favourite_sports[1]="football"
#print(favourite_sports)
#jedzenie1=input("jaka jest twa top 1 potrawa?")
#jedzenie2=input("jaka jest twa top 2 potrawa?")
#jedzenie3=input("jaka jest twa top 3 potrawa?")
#fav_potrawki=[jedzenie1,jedzenie2,jedzenie3]
#print(fav_potrawki)
#nr_celly=input("pojda swój numer celly")
#nr_celly=nr_celly[:3]+6*"-"
#print(nr_celly)



#dictonary
#słwonik={
#"klucz":"wartość",
#1:"adin"
#}
#print(f" Przykład: {słwonik['klucz']}")
#wydatki={
 #   "zakupy":[340,2.40],
  #  "prąd":[2137]
#}
#nauczyciel={
#    "first name":"Janusz",
 #   "sekend naejm":"korwin",
  #  "contrackt":{
   #     "sign date":"21.3.1997",
    #    "salaty":69
    #}
#}
#nauczyciel["first name"]="muhammed"
#nauczyciel["city"]="Istambuł"
#print(nauczyciel.keys())
#print(nauczyciel.values())
#values=list(nauczyciel.values())
#print(values)
#print(nauczyciel)
#print(wydatki)
#print(len(nauczyciel))
##zadania
#oceny={
#    "matma":[5,3,2,5,4],
##    "polski":[6,5,1,5,1,6],
 ###   "angielski":[6,6,5]
#}
#print(oceny)
#my_family ={
#    "ja":{
#        "data urodzenia":"26.04.2006",
#        "mama":{
#            "data urodzenia":"nie znam",
#        },
#        "tata":{
#            "data utodzneia":"nie znam"
#        }
#        }
#    }
#print(my_family)
#jedzenie=int(input("Ile wydajesz na jedzenie miesiecznie?"))
#rozrywka=int(input("ile wydajesz na rozyrwke miesiecznie?"))
###oplaty=int(input("ile wydajesz na oplaty miesieczne??"))
#wszytk_wydatka=jedzenie+rozrywka+oplaty
#jedzenie*=100/wszytk_wydatka
#rozrywka*=100/wszytk_wydatka
#oplaty*=100/wszytk_wydatka
#procenty={
#    "jedzomko":jedzenie,
#    "rozrywka":rozrywka,
#    "rachunki":oplaty
#}
#wbrana=input("wybierz bt zobaczyc procent jaki wydajesz na co (jedzomko/rozrywka/rachunki)")
#print(f"NA {wbrana} wyjdajesz  {procenty[wbrana]:.0f}%")

#None type
#None
#print(type(none))
# nie wiem komu to potrzebne ale sie da
#none_str=str(None)
#print("abc"+none_str)
