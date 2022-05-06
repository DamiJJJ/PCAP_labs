def readint(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = min <= value <= max
            if not ok:
                print(f'Błąd: podana liczba jest spoza dozwolonego zakresu ({min}..{max})')
        except ValueError:
            print('Błąd: wprowadzono nieprawidłową liczbę')
    return value

v = readint("Podaj liczbe od -10 do 10: ", -10, 10)

print("Liczba to:", v)
