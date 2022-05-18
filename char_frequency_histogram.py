# 6.9.1.15 Histogram częstotliwości znaków

def histogram(file_name):
    
    dict = {}
    try:
        for line in open(file_name, 'r'):
            for char in line:
                if char.isalpha():
                    char = char.lower()
                    if char in dict:
                        dict[char] += 1
                    else:
                        dict[char] = 1
    except IOError as error:
        print('Nie udało się otworzyć pliku!', error)

    for letter, value in sorted(dict.items()):
        print(letter, ' -> ', value)

def main():

    file_name = input('Wprowadź nazwę pliku wejściowego: ')

    histogram(file_name)

if __name__ == '__main__':
    main()