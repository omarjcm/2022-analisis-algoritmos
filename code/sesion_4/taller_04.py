def linea(caracter, num_veces):
    for elemento in range(num_veces):
        print(caracter, end='')

def cuadrado(caracter, num_veces):
    dimension = int(num_veces/2)
    for elemento in range(dimension):
        linea(caracter, num_veces)
        print()

if __name__ == '__main__':
    cuadrado('*', 10)