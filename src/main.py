#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Creador: Jakepy Perdomo <j4kyjak3@protonmail.com>
# Título: pytranslate
# FechaCreación: 6-may-22
#
# Código simple de un simple traductor.
# Copyright (c) 2022 Jakepy Perdomo <j4kyjak3@protonmail.com>. 
# Comentarios bienvenidos.
#
# Permiso otorgado para uso y distribución no comercial siempre que
# este aviso de derechos de autor permanece intacto.
#
# Hay ejemplos de cómo usar este código en el README.md.
#
# Cual quier duda escribeme, o talvez este dormido jsjs.



from googletrans import Translator
from color import Color as c
import platform, os

trans = Translator()

def clear():
    if platform.system() == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def banner():
    f = Figlet(font='epic')

    print(f'{c.azul}', f.renderText('Traductpy'), f'{c.off}')


def menu() -> None:
    ''' menu de elecion de tipo int
    ''' 

    print(option := f'''
{c.azul}[*] Ingresa una opcion [*]{c.off}

{c.amarillo}1) {c.azul}ES a EN
{c.amarillo}2) {c.azul}EN a ES
{c.amarillo}3) {c.azul}salir ''')

    return option


# Opcion 1
def traductor_ES_a_EN(p: str) -> str:
    ''' Traduce de español a ingles
    '''
    salida = trans.translate(p, dest='en')
    print('\n',salida.text,'\n')

    return salida

# opcion 2
def traductor_EN_a_ES(p: str) -> str:
    '''Traduce de ingles a español
    '''

    salida = trans.translate(p, dest='es')
    print('\n',salida.text,'\n')

    return salida


def main():
    clear()
    banner()
    menu()
    try:    
        option = int(input(f'\n{c.rojo}[*] {c.verde}Ingresa una opcion: {c.off}'))  

        while option != 3:

            if option == 1:
                clear()
                banner()
                palabra = str(input(f'{c.rojo}[*] {c.verde}Ingresa la palabra a traducir {c.azul}[ES]: {c.off}'))
                traductor_ES_a_EN(palabra)
                break
            
            elif option == 2:
                clear()
                banner()
                palabra = str(input(f'{c.rojo}[*] {c.verde}Ingresa la palabra a traducir {c.azul}[EN]: {c.off}'))
                traductor_EN_a_ES(palabra)
                break

            else:
                clear()
                banner()
                print(f'\n{c.rojo}[!] Bye...{c.off}\n')
                exit(0)
    
    except KeyboardInterrupt:
        clear()
        print(f'\n\n {c.rojo}[!] Saliendo... {c.off}\n')

    except ValueError:
        clear()
        print(f'\n\n {c.rojo}[!] Ingresa una palabra {c.off}\n')
        
        
if __name__ == '__main__':
    main()
