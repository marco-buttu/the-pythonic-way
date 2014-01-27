#!/usr/bin/env python
"""Calcolo del valore minimo, massimo e medio dei dati presenti nei file con 
estensione `.data`.

Legge i file con estensione `.data` presenti nella directory corrente, e di 
ogni linea calcola il valore massimo, quello minimo e quello medio degli 
elementi. Salva questi risultati su dei file di output che hanno lo stesso 
nome dei file di input, ma con estensione `.dataout`.
Lo script prende un argomento opzionale `out_dir_name`, che indica la directory
nella quale salvare i file di output. Se questo argomento viene omesso, i file 
di output vengono salvati in una directory di nome `out`:

    $ python dataout.py [out_dir_name=out]

Se la directory di output non esiste, viene creata.
"""
import sys
import os

out_dir_name = sys.argv[1] if sys.argv[1:] else 'out'  # Nome directory output
try:
    os.mkdir(out_dir_name) # Crea la directory di output
    print('I file verranno scritti nella directory', out_dir_name)
except FileExistsError:
    print("I file verranno scritti nella directory", out_dir_name, "esistente")

for file_name in os.listdir():
    if file_name.endswith('.data'):
        out_file_name = os.path.join(out_dir_name, file_name + 'out')
        print('Sto per scrivere sul file `%s` ...' %out_file_name, end=' ')
        out = open(out_file_name, 'w')
        for line in open(file_name):
            d = [float(item) for item in line.split()] # Dati della linea
            out.write('%.2f   %.2f   %.2f\n' %(min(d), max(d), sum(d)/len(d)))
        print('Fatto!')

