from random import randint
from os import system
from colorama import Fore, init
init(autoreset=True)


def visualizador_datos(dato, camino=1):
    """Visualizador de datos
    Argumentos:
        dato ([list]): [lista para representar los datos]
        camino (int, optional): [Redirecciona si es una lista con sub lista, o lista sola]. Defaults to 1.
    """
    print(Fore.YELLOW + """
Valor Inicial\tCargos\tIva\ttotal""")

    if camino == 1:
        total = sum(dato)
        print(f"${dato[0]}\t\t${dato[1]}\t${dato[2]}\t${round(total,2)}")
    elif camino == 2:
        for a in dato:
            total = sum(a)
            print(f"${a[0]}\t\t${a[1]}\t${a[2]}\t${round(total,2)}")


def calculo(monto):
    """Calculo
    Argumentos
        monto (int): [monto principal a manipula]
    Returns:
        [list]: [retorna una lista con los valores Monto, Cargos, Iva]
    """
    cargos = monto * 0.05
    iva = cargos * 0.21
    return round(monto, 2), round(cargos, 2), round(iva, 2)


def tabla_random():
    while True:
        print('Cuantos valores quieres que muestre\n[1-50]')
        valores = int(input('> '))
        system("clear")
        if (1 <= int(valores) <= 50):
            print(f'Mostrando {valores} valores alazar')
            contenedor = []
            for i in range(valores):
                valor_rando = randint(1, 10001)
                contenedor.append(calculo(valor_rando))
            contenedor = sorted(contenedor)
            visualizador_datos(contenedor, 2)
            print(Fore.YELLOW + 'quieres probar denuevo?\n[Y/N]')
            continuar = input('> ')
            if continuar.capitalize() == 'N':
                break
        else:
            print('Por favor ingrese un numero dentro de esos valores')


def monto_exacto():
    print('Ingrese el monto deseado a enviar')
    monto_enviar = int(input('> $'))
    visualizador_datos(calculo(monto_enviar))

