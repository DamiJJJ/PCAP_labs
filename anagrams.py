# 5.8.1.8 Anagrams

# Rozwiązanie 1
# tekst1 = str(input("Wprowadź pierwszy tekst: ")).replace(' ', '').upper()
# tekst2 = str(input("Wprowadź drugi tekst: ")).replace(' ', '').upper()
# lst = []

# if tekst1 == '' or tekst2 == '':
#     print('Nie anagramy')
# else:
#     for ch in tekst1:
#         lst.append(ch)
#     licznik = 0
#     for ch in tekst2:
#         if ch in lst:
#             licznik += 1
#     if licznik == len(lst):
#         print('Anagramy')
#     else:
#         print('Nie anagramy')

# Rozwiązanie 2
tekst1 = str(input("Wprowadź pierwszy tekst: "))
tekst2 = str(input("Wprowadź drugi tekst: "))

lst1 = ''.join(sorted(list(tekst1.upper().replace(' ',''))))
lst2 = ''.join(sorted(list(tekst2.upper().replace(' ',''))))

if len(lst1) > 0 and lst1 == lst2:
    	print("Anagramy")
else:
	print("Nie anagramy")	