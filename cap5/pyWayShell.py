import cmd, subprocess, sys, logging
from sympy import *
from os.path import splitext as st

logging.basicConfig(filename=st(__file__)[0] + '.log', level=logging.DEBUG)

class PyWayShell(cmd.Cmd):
    intro = "Benvenuto :) Digita help o ? per vedere l'elenco dei comandi.\n"
    prompt = '>> '

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.namespace = {}

    def do_quit(self, line):
        """Esce dal programma."""
        print("\nGrazie per aver usato pyWayShell :)")
        sys.exit(1)

    def do_shell(self, line):
        """Esegue il comando nella shell di sistema."""
        try:
            subprocess.call(line, timeout=5, shell=True)
        except subprocess.TimeoutExpired:
            print('Il processo non è terminato nel timeout stabilito')

    def emptyline(self):    
        """Non fare nulla se la linea e' vuota"""
        pass

    def do_EOF(self, line):
        """Con CTR-D esce dal programma."""
        self.do_quit(line)

    do_q = do_quit

    def precmd(self, line):
        """Azioni prima di interpretare il comando"""
        self.raw_line = line
        try:
            return line.format_map(self.namespace) 
        except KeyError as ex:
            print("L'etichetta %s non e' definita" %ex)
        except ValueError:
            print("L'etichetta tra parentesi graffe non puo' essere un numero")

        return '' # Restituisce una linea vuota

    def default(self, line):
        """I comandi non previsti nell'help vengono semplificati con SymPy."""
        try:
            if '=' in line:
                try:
                    n, e = [item.strip() for item in line.split('=')] 
                except ValueError:
                    print("Non e' possibile fare piu' di un assegnamento nello stesso comando")
                else:
                    if n.isalnum():
                        self.namespace.update({n:e}) 
                    else:
                        print("Nome `%s` non valido!" %n)
            elif line == self.raw_line and line.isalnum():
                print("Prova con {%s} piuttosto che con %s." %(line, line))
            else:
                print(simplify(line) if line else '')
        except Exception as ex:
            logging.debug('Linea: ' + line)
            logging.debug('Messaggio: %s\n' %str(ex))
            print(ex)

    def help_default(self):
        print(self.default.__doc__)


if __name__ == '__main__':
    pws = PyWayShell()
    pws.cmdloop()

