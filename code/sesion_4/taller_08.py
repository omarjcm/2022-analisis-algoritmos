def espacios_escaleras(num_veces):
    for i in range(num_veces):
        for j in range(4):
            print(' ', end='')

def escalon_arriba():
    for i in range(5):
        print('*', end='')

def escaleras(num_escaleras):
    for escalon in range(num_escaleras, 0, -1):
        espacios_escaleras(escalon)
        escalon_arriba()
        print()
        espacios_escaleras(escalon)
        print('*')
        espacios_escaleras(escalon)
        print('*')

if __name__ == '__main__':
    escaleras(5)

