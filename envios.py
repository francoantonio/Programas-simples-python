#!/usr/bin/env python3
#  Programa para calcular el cargo de un envio de dinero
#  Iva %21
# cargos %5
from funciones import tabla_random, monto_exacto
from colorama import init, Fore
from os import system
init(autoreset=True)


def menu():
    print(Fore.YELLOW+'Programa para calcular el valor total de un envio de dinero sumando Los cargos y el iva'.center(
        100, '*'))
    while True:
        print(Fore.YELLOW + """
Eliga una opcion
1) calcular un monto exacto
2) ver tabla de valores randon
3) salir
        """)
        opc = input("> ")
        system("clear")
        if int(opc) == 1:
            monto_exacto()
        elif int(opc) == 2:
            tabla_random()
        elif int(opc) == 3:
            print('Saliendo del programa')
            print('Muchas gracias ')
            break
        else:
            print('************ERROR****************')
            print('opcion incorrecta\nIntente nuevamente')


def run():
    system("clear")
    menu()


if __name__ == "__main__":
    run()
