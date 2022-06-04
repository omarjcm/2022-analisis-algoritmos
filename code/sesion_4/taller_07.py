def espacios(num_veces):
    for i in range(num_veces):
        print(' ', end='')

def linea(caracter, num_veces):
    for i in range(num_veces):
        print(caracter, end='')

def triangulo(caracter, lineas):
    for i in range(lineas, 0, -1):
        espacios(i-1)
        linea(caracter, ((lineas-i)+1)*2 )
        print()

if __name__ == '__main__':
    triangulo('*', 20)