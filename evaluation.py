# 6.9.1.17 LAB Evaluating students' results
# Wyświetlanie z pliku tekstowego zsumowanych punktów każdego ucznia
# Dane w pliku miodek.txt

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


class EmptyFile(StudentsDataException):
    def __init__(self):
        super().__init__(self)

import os

def raport(file_name):

    dct = {}

    try:
        if os.stat(file_name).st_size == 0:
                raise EmptyFile
        else:
            line_number = 0
            for line in open(file_name, 'r'):
                columns = line.split()
                line_number += 1
                if len(columns) != 3:
                    raise BadLine(line_number, line)
                student = columns[0] + ' ' + columns[1]
                try:
                    points = float(columns[2])
                except ValueError:
                    raise BadLine(line_number, line)
                if student not in dct:
                    dct[student] = points
                else:
                    dct[student] += points

            for name, points in sorted(dct.items()):
                print(name, points, sep='\t')
                
    except IOError as e:
        print('Błąd I/O: ', os.strerror(e.errno))
    except BadLine as e:
        print('Błąd w linii #' + str(e.line_number) + ': ' + e.line_string)
    except EmptyFile:
        print("Plik źródłowy jest pusty!")

def main():

    file_name = input('Wprowadź nazwę pliku wejściowego: ')

    raport(file_name)

if __name__ == '__main__':
    main()