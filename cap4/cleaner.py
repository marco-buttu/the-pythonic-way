#!/usr/bin/env python3.3
# File: cleaner.py
import argparse
import rmfiles

parser = argparse.ArgumentParser(description='Cancella files in modo ricorsivo')
parser.add_argument('-base_path', type=str, default='.', help='Percorso iniziale')
parser.add_argument('-suffix', type=str, default='.pyc', help='Suffisso dei files')
globals().update(vars(parser.parse_args()))

rmfiles.remove_recursively(base_path, suffix)
