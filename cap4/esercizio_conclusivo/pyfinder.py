#!/usr/bin/env python
"""
Questo modulo definisce delle funzioni generatore che consentono di cercare 
dei file nel file-system, ed anche del testo all'interno di un file. 
Il modulo definisce le seguenti funzioni:

  - file_finder(): cerca dei file il cui nome verifica un dato pattern. 
    Nel seguente esempio viene cercato un file di nome `os.py` all'interno 
    della directory contenente il modulo `os` della libreria standard, per 
    cui viene trovato il file `os.py`:

        >>> for file in file_finder('os.py', os.path.dirname(os.__file__)):
        ...     print(os.path.basename(file)) # Stampa solo il nome, non il percorso completo
        ...     
        ... 
        os.py

  - file_inspector(): cerca un dato pattern all'interno di un file di testo. Ad esempio:
      
        >>> for match in file_inspector(doctest.__file__, 'Tim Peters'):
        ...     print(match, end='')
        ...     
        ... 
        # Released to the public domain 16-Jan-2001, by Tim Peters (tim@python.org).

"""

import fnmatch
import os
import re

def file_finder(pattern: str, top_dir: str=os.curdir, recursive: bool=False):
    """Cerca dei file il cui nome verifica un dato pattern e restituisce un generatore.

    La ricerca avviene per default all'interno della directory corrente:
    
        >>> for file in file_finder('finder.py'):
        ...     print(os.path.basename(file)) # Stampa solo il nome, non il percorso completo
        ...     
        ... 
        finder.py
    
    Un secondo argomento opzionale viene utilizzato per indicare la directory di partenza:

        >>> for file in file_finder('message.py', os.path.dirname(email.__file__)):
        ...     print(os.path.basename(file))
        ...     
        ... 
        message.py

    Il pattern puo' contenere anche i caratteri jolly delle shell Unix-like: 

        >>> for file in file_finder('me*age.py', os.path.dirname(email.__file__)):
        ...     print(os.path.basename(file))
        ...     
        ... 
        message.py

    La ricerca puo' essere fatta anche in modo ricorsivo, passando come terzo argomento `True`.
    Nel seguente esempio il file `message.py` viene trovato nella directory `email` (primo risultato)
    ed in una sua sotto-directory (secondo risultato):

        >>> for file in file_finder('me*age.py',  os.path.dirname(email.__file__), True):
        ...     print(os.path.basename(file))
        ...     
        ... 
        message.py
        message.py

    """
    for path, dirs, files in os.walk(top_dir):
        if not recursive: 
            dirs.clear() # Svuota la lista delle sotto-directory di `top_dir`
        for name in fnmatch.filter(files, pattern):
            yield os.path.join(path, name)


def file_inspector(file_name: str, pattern: str):
    """Cerca un dato pattern all'interno di un file di testo e restituisce un generatore.

    Nel seguente caso ad esempio viene cercato il testo `Regular` all'interno del modulo
    `re` (file `re.py` della libreria standard di Python:

        >>> for match in file_inspector(re.__file__, 'Regular'):
        ...     print(match, end='')
        ...     
        ... 
        # Secret Labs' Regular Expression Engine
        Regular expressions can contain both special and ordinary characters.

    Il pattern può essere una espressione regolare:

       >>> for match in file_inspector(re.__file__, '^Regular'):
       ...     print(match, end='')
       ...     
       ... 
       Regular expressions can contain both special and ordinary characters.
        
    """
    for line in open(file_name):
        if re.search(pattern, line):
            yield line


if __name__ == '__main__':
    import doctest, email
    doctest.testmod()
