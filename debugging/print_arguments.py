#!/usr/bin/python3
"""print_arguments.py - Affiche les arguments de la ligne de commande (sauf le nom du script)."""

import sys

# Parcours tous les arguments à partir de l'index 1 (on ignore sys.argv[0] qui contient le nom du script)
for i in range(1, len(sys.argv)):
    print(sys.argv[i])

