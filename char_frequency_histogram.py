# 6.9.1.16 Histogram posortowanej częstotliwości znaków

def histogram(file_name):
    
    histogram = {}
    try:
        for line in open(file_name, 'r'):
            for char in line:
                if char.isalpha():
                    char = char.lower()
                    if char in histogram:
                        histogram[char] += 1
                    else:
                        histogram[char] = 1
    except IOError as error:
        print('Nie udało się otworzyć pliku!', error)
        return

    # Sortowanie słownika po wartościach
    list = sorted(histogram.items(), key=lambda x:x[1], reverse=True)
    sortdict = dict(list)

    try:
        file = open(f"{file_name}.hist", 'w')
        for letter, value in sortdict.items():
            x = f"{letter} -> {value}"
            print(x)
            file.write(x)
            file.write('\n')
        file.close()
        print('Zapisano do pliku!')
    except Exception as error:
        print('Nie udało się zapisać pliku!', error)
        return


def main():

    file_name = input('Wprowadź nazwę pliku wejściowego: ')

    histogram(file_name)

if __name__ == '__main__':
    main()