def linea(caracter, num_veces):
    for elemento in range(num_veces):
        print(caracter, end='')

def triangulo(caracter, lineas):
    for i in range(lineas):
        linea(caracter, i+1)
        print()

if __name__ == '__main__':
    triangulo('*', 5)