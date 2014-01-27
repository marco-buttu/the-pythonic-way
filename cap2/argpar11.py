import argparse
parser = argparse.ArgumentParser() 
parser.add_argument('-f', '--file', type=argparse.FileType(), required=True, 
        help='Nome del file da aprire') 
parser.add_argument('-i', '--index', type=int, default=0, help='Indice della linea')
args = parser.parse_args() 
lines = args.file.readlines() 
print(lines[args.index])

