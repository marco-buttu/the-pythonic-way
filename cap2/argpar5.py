import argparse
parser = argparse.ArgumentParser() 
parser.add_argument('file', type=open, help='Nome del file da aprire') 
parser.add_argument('index', type=int, help='Indice della linea del file da visualizzare')
args = parser.parse_args() 
lines = args.file.readlines() 
print(lines[args.index])

