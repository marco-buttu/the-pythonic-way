import subprocess
from sympy import *

namespace = {}
while True:
    raw_line = input(">> ").strip()
    fline = raw_line.format_map(namespace) 
    if fline == 'quit':
        break
    elif not fline: 
        continue
    elif fline.startswith('!'):
        try:
            subprocess.call(fline[1:].split())
        except FileNotFoundError:
            print('Nome del programma non valido!')
    elif '=' in fline:
        n, e = [item.strip() for item in fline.split('=')] # n -> name, e -> expression
        namespace.update({n:e}) if n.isalnum() else print("Nome `%s` non valido!" %n)
    elif fline == raw_line and fline.isalnum():
        print("Prova con {%s} piuttosto che con %s." %(fline, fline))
    else:
        print(simplify(fline) if fline else '')
