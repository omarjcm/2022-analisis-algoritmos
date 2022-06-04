def linea(caracter, num_veces):
    for elemento in range(num_veces):
        print(caracter, end='')

if __name__ == '__main__':
    linea('*', 10)