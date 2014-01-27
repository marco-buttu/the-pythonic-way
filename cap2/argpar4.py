import argparse
parser = argparse.ArgumentParser() 
parser.add_argument('file', help='Nome del file da aprire') 
parser.add_argument('index', type=int, help='Indice della linea del file da visualizzare')
args = parser.parse_args() 
lines = open(args.file).readlines() 
print(lines[args.index])

