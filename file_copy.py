# Kopiowanie dowolnego pliku

from os import strerror

nazwaZrodla = input("Wprowadz nazwe pliku zrodlowego: ")
try:
    zrodlo = open(nazwaZrodla, 'rb')
except IOError as e:
    print("Nie mozna otworzyc pliku zrodlowego: ", strerror(e.errno))
    exit(e.errno)	
	
nazwaDocelowa = input("Wprowadz nazwe pliku docelowego: ")
try:
    docelowy = open(nazwaDocelowa, 'wb')
except Exception as e:
    print("Nie mozna utworzyc pliku docelowego: ", strerror(e.errno))
    zrodlo.close()
    exit(e.errno)	

bufor = bytearray(65536)
suma  = 0
try:
    wczytany = zrodlo.readinto(bufor)
    while wczytany > 0:
        zapisany = docelowy.write(bufor[:wczytany])
        suma += zapisany
        wczytany = zrodlo.readinto(bufor)
except IOError as e:
    print("Nie mozna utworzyc pliku docelowego: ", strerror(e.errno))
    exit(e.errno)	
    
print(suma,'bajt(y) poprawie zapisany')
zrodlo.close()
docelowy.close()