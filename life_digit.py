# 5.8.1.9 Cyfra Życia

def cyfra_zycia(data):
    liczba = 0
    for ch in str(data):
        liczba += int(ch)
    if liczba > 9:
        liczba = cyfra_zycia(liczba)
    return liczba

data = input("Wprowadź datę w formacie RRRRMMDD, RRRRDDMM, MMDDRRRR: ")  

if len(data) != 8 or not data.isdigit():
    print("Wprowadzono błędny format daty!")
else:
    print(f"Twoja Cyfra Życia to: {cyfra_zycia(data)}")
