def linea(caracter, num_veces):
    if num_veces == 0:
        return
    else:
        print(caracter, end='')
        num_veces -= 1
        return linea(caracter, num_veces)

if __name__ == '__main__':
    linea('*', 10)