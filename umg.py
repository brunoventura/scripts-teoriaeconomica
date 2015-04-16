#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

del sys.argv[0]
args = sys.argv
x = []
y = []
cells = []
last = None
total = 0
for n in range(0, len(args)):
	arg = None
	try:
		arg	= int(args[n])
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
	x.append(n+1)
	y.append(arg)
	cells.append([n+1, arg, total])
	last = arg

columns = ["Quantidade","UMG","Utilidade Total"]

plt.subplots_adjust(top=0.8, left=0.2, right=0.8)

plt.subplot(2, 1, 2)
plt.plot(x, [a[2] for a in cells], '-o')
plt.axis([0, len(args)*1.1, 0, total*1.1])

plt.subplot(2, 1, 1)
plt.plot(x, y, '-o')
plt.axis([0, len(args)*1.1, 0, int(args[0])*1.1])

plt.table(cellText = cells,cellLoc='center', colLabels=columns, loc='top')

plt.show()