from time import sleep

def contador(a, b, c):
    cont = a
    if a < b:
        while cont <= b:
            print(f'{cont}', end=' ', flush=True)
            cont += c
            sleep(0.5)
    else:
        while cont >= b:
            print(f'{cont}', end=' ', flush=True)
            cont -= c
            sleep(0.5)



ini = (int(input('digite aqui o numero de inicio: ')))
fim = (int(input('digite aqui o numero final: ')))
pas = (int(input('digie aqui o passo: ')))
contador(ini, fim, pas)
