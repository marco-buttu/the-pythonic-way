import argparse
parser = argparse.ArgumentParser() 
parser.add_argument('-f', '--file', type=argparse.FileType(), help='Nome del file da aprire') 
parser.add_argument('-i', '--index', type=int, help='Indice della linea del file da visualizzare')
args = parser.parse_args() 
lines = args.file.readlines() 
print(lines[args.index])

