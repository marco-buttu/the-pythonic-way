import argparse
parser = argparse.ArgumentParser() # Creo il parser
parser.add_argument('file') # Voglio fare il parsing di un argomento che chiamo `file`
args = parser.parse_args() # Faccio il parsing degli argomenti e assegno il namespace a `args`
lines = open(args.file).readlines() # Assegno a `lines` la lista delle linee del file
print(lines[0]) # Stampo la prima linea del file

