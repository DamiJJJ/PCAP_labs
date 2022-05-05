# 5.8.1.8 Anagrams

tekst1 = str(input("Wprowadź pierwszy tekst: "))
tekst2 = str(input("Wprowadź drugi tekst: "))

tekst1 = tekst1.replace(' ', '').upper()
tekst2 = tekst2.replace(' ', '').upper()
lst = []

if tekst1 == '' or tekst2 == '':
    print('Nie anagramy')
else:
    for ch in tekst1:
        lst.append(ch)
    licznik = 0
    for ch in tekst2:
        if ch in lst:
            licznik += 1
    if licznik == len(lst):
        print('Anagramy')
    else:
        print('Nie anagramy')