import subprocess
import sys
from sympy import *

namespace = {}
while True:
    try:
        raw_line = input(">> ").strip()
        try:
            fline = raw_line.format_map(namespace) 
        except KeyError as ex:
            print("L'etichetta %s non e' definita" %ex)
        except ValueError:
            print("L'etichetta tra parentesi graffe non puo' essere un numero")
            continue
        if fline == 'quit':
            break
        elif not fline: 
            continue
        elif fline.startswith('!'):
            try:
                subprocess.call(fline[1:].split(), timeout=5)
            except FileNotFoundError:
                print('Nome del programma non valido!')
            except subprocess.TimeoutExpired:
                print('Il processo non è terminato nel timeout stabilito')
        elif '=' in fline:
            try:
                n, e = [item.strip() for item in fline.split('=')] # n -> name, e -> expression
            except ValueError:
                print("Non e' possibile fare piu' di un assegnamento nello stesso comando")
            else:
                namespace.update({n:e}) if n.isalnum() else \
                        print("Nome `%s` non valido!" %n)
        elif fline == raw_line and fline.isalnum():
            print("Prova con {%s} piuttosto che con %s." %(fline, fline))
        else:
            print(simplify(fline) if fline else '')
    except Exception as ex:
        print(ex)

