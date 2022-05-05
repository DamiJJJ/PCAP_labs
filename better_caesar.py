# 5.8.1.6 Ulepszenie Szyfru Cezara

tekst = input("Tekst do zaszyfrowania: ")

przesuniecie = 0
while not (0 < przesuniecie < 26):
    try:
        przesuniecie = int(input("Przesunięcie (1-25): "))
    except:
        print('Wpisz poprawną wartość!')

szyfr = ''

for char in tekst:
    if not char.isalpha():
        szyfr += char
    else:
        kod = ord(char) + przesuniecie
        if char.isupper() and kod > ord('Z'):
            kod = ord('A') + (przesuniecie - (ord('Z') - ord(char) + 1))
        elif kod > ord('z'):
            kod = ord('a') + (przesuniecie - (ord('z') - ord(char) + 1))
        szyfr += chr(kod)

print(szyfr)