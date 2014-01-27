#!/usr/bin/env python3
# File: rmfiles.py
"""Rimuovi tutti i file con un dato suffisso.

Questo modulo definisce la funzione `remove_recursively()`.
Questa prende due argomenti, `from_` e `suffix`, e  rimuove a
partire dalla directory `from_`, in modo ricorsivo, tutti i 
files che hanno suffisso `suffix`. Per default, rimuove tutti 
i files con suffisso `.pyc`, a partire dalla directory corrente.

Quando il file viene eseguito dalla linea di comando, viene
chiamata la funzione `remove_recursively()` con i valori di
default.
"""

import os

def remove_recursively(from_='.', suffix='.pyc'):
    for root, dirs, files in os.walk(from_):
        found = [file for file in files if file.endswith(suffix)]
        for file in found:
            os.remove(os.path.join(root, file))
            print(os.path.join(root, file), 'file removed')

if __name__ == "__main__":
    remove_recursively()
