# load test for different kind of charging schemes

from EvClass import Ev
from EvChargingAlg import Greedy

evList = [Ev(3), Ev(5), Ev(8), Ev(2)]

limit = 7

solver = Greedy('nonEvLoad.txt', evList, limit)
solver.calcTotalLoad()
solver.readNonEvLoad()

solver.solve()

