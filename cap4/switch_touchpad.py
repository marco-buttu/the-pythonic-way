#! /usr/bin/env python3
"""Su Ubuntu 11.04: abilita il TouchPad se disabilitato, altrimenti lo disabilita"""
from os import popen
out = popen('xinput list-props "SynPS/2 Synaptics TouchPad"')
base = 'xinput set-int-prop "SynPS/2 Synaptics TouchPad" "Device Enabled" 8 '
for line in out: # Itera sulle linee dell'output del comando
    line = line.strip()
    if line.startswith("Device Enabled"):
        # Esegui il comando `base + '0'` (disabilita) o `base + '1'` (abilita)
        popen(base + '0') if line.endswith('1') else popen(base + '1')

