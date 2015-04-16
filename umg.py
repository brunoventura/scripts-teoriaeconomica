#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
from prettytable import PrettyTable

args = sys.argv
table = PrettyTable(["Quantidade","UMG","Utilidade Total"])
last = None
total = 0
for x in range(1, len(args)):
	arg = None
	try:
		arg	= int(args[x])
	except ValueError:
		print "Valor inválido informado"
		break
	if last != None and arg >= last :
		print "O valor do UMG deve ser decrescente"
		break
	if int(arg) < 0 :
		print "O valor não pode ser negativo"
		break
	total += arg
	table.add_row([x, arg, total])
	last = arg
print table