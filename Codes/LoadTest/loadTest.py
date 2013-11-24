#!/usr/bin/python
# -*- coding: utf-8 -*-

# load test for different kind of charging schemes

from EvClass import Ev
from EvChargingAlg import *

evList = [Ev(3), Ev(5), Ev(7), Ev(2)]

limit = 7

solver1 = Greedy('nonEvLoad.txt', evList, limit)
solver1.calcTotalLoad()
solver1.readNonEvLoad()

rsList, tlList, remaining = solver1.solve()
f = file('result.txt', 'w')
#for rs, tl in zip(rsList, tlList):
#	print>>f, '%s %s,' % (rs, tl),

for rs in rsList:
	print>>f, '%s,' % rs,
print>>f, ''
for tl in tlList:
	print>>f, '%s,' % tl,
print>>f, ''

print>>f, remaining
f.close()

solver2 = ValleyFilling('nonEvLoad.txt', evList, limit)
solver2.calcTotalLoad()
solver2.readNonEvLoad()

solver2.setLimit(5)
rsList, tlList, remaining = solver2.solve()
f = file('result.txt', 'a')
#for rs, tl in zip(rsList, tlList):
#	print>>f, '%s %s,' % (rs, tl),

for rs in rsList:
	print>>f, '%s,' % rs,
print>>f, ''
for tl in tlList:
	print>>f, '%s,' % tl,
print>>f, ''

print>>f, remaining
f.close()
