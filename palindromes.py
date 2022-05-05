# 5.8.1.7 Palindromy

# Rozwiązanie 1
# tekst = str(input("Wprowadź tekst: "))

# tekst = tekst.replace(' ', '')
# lst1 = []

# if tekst == '':
#     print('To nie jest palindrom')
# else:
#     for ch in tekst:
#         lst1.append(ch.upper())
#     lst2 = list(reversed(lst1))
#     if lst1 == lst2:
#         print('To jest palindrom')
#     else:
#         print('To nie jest palindrom')

# Rozwiązanie 2
tekst = str(input("Wprowadź tekst: ")).replace(' ', '').upper()

if tekst == '':
    print('To nie jest palindrom')
else:
    if tekst == tekst[::-1]:
        print("To jest palindrom")
    else:
        print("To nie jest palindrom")