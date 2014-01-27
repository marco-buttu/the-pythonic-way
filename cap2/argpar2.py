import argparse
parser = argparse.ArgumentParser() 
parser.add_argument('file', help='Nome del file da aprire') 
args = parser.parse_args() 
lines = open(args.file).readlines() 
print(lines[0])

