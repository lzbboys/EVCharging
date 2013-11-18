import cPickle as pickle

class Alg:
	''' The Algorithm for EV charging'''
	def __init__(self, ldFileName, evList, limit):
		self.ldFileName = ldFileName
		self.rsFileName = 'result.txt'
		self.ldList = []
		self.evList = evList
		self.limit = limit

	def calcTotalLoad(self):
		self.total = 0
		for ev in self.evList:
			self.total += ev.reqLoad

	def readNonEvLoad(self):
		f = file(self.ldFileName, 'r')
		line = f.readline()
		f.close()
		line = line.splitlines()
		ldList = []
		for l in line:
			ldList.extend(l.split(','))
		
		for ld in ldList:
			self.ldList.append(int(ld))

class Greedy(Alg):
	''' Greedy charging scheme '''
	def solve(self):
		total = self.total
		rsList = []
		for ld in self.ldList:
			if total <= 0:
				break
			chargingLd = self.limit - ld
			rsList.append(chargingLd if chargingLd < total else total)
			total -= self.limit - ld

		print rsList
		f = file(self.rsFileName, 'w')
		for rs in rsList:
			f.write('%d,' % (rs))
		f.close()

class ValleyFilling(Alg):
	''' Valley filling charging scheme '''
