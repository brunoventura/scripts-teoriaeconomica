#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt

del sys.argv[0]
args = sys.argv

def umgplot(x, y, pltnr) :
	x = np.array(x)
	y = np.array(y)

	z = np.polyfit(x,y,len(args)-1)
	p = np.poly1d(z)
	xp = np.linspace(1, len(args), 100)	

	plt.subplot(2, 1, pltnr)
	plt.plot(x, y, '.', xp, p(xp),'-')
	plt.axis([0, len(args)*1.1, 0, max(y)*1.1])

x = []
y = []
cells = []
last = None
total = 0
if len(args) == 0 :
	print "A quantidade de argumentos tem que ser maior que zero"
	sys.exit()

for n in range(0, len(args)):
	arg = None
	try:
		arg	= int(args[n])
	except ValueError:
		print "Valor inválido informado"
		sys.exit()
	if last != None and arg >= last :
		print "O valor do UMG deve ser decrescente"
		sys.exit()
	if int(arg) < 0 :
		print "O valor não pode ser negativo"
		sys.exit()
	total += arg
	x.append(n+1)
	y.append(arg)
	cells.append([n+1, arg, total])
	last = arg

columns = ["Quantidade","UMG","Utilidade Total"]

plt.subplots_adjust(top=0.8, left=0.2, right=0.8)

umgplot(x, [a[2] for a in cells], 2)
umgplot(x, y, 1)

plt.table(cellText = cells,cellLoc='center', colLabels=columns, loc='top')
plt.show()