import subprocess
from sympy import *

namespace = {}
while True:
    raw_line = input(">> ").strip()
    try:
        fline = raw_line.format_map(namespace) 
    except KeyError as ex:
        print("L'etichetta %s non e' definita" %ex)
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
            print('Il processo non è terminato il timout stabilito')
        except KeyboardInterrupt:
            print()
    elif '=' in fline:
        try:
            n, e = [item.strip() for item in fline.split('=')] # n -> name, e -> expression
        except ValueError:
            print("Non e' possibile fare piu' di un assegnamento nello stesso comando")
        else:
            namespace.update({n:e}) if n.isalnum() else print("Nome `%s` non valido!" %n)
    elif fline == raw_line and fline.isalnum():
        print("Prova con {%s} piuttosto che con %s." %(fline, fline))
    else:
        print(simplify(fline) if fline else '')
