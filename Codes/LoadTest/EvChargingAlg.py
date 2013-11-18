#!/usr/bin/python
# -*- coding: utf-8 -*-

class Alg:
	''' The Algorithm for EV charging'''
	def __init__(self, ldFileName, evList, limit):
		self.ldFileName = ldFileName
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
		remaining = self.total
		rsList = []
		tlList = []
		for ld in self.ldList:
			available = (self.limit - ld) if (self.limit - ld) > 0 else 0
			chargingLd = available if available < remaining else remaining
			rsList.append(chargingLd)
			tlList.append(chargingLd + ld)
			remaining -= chargingLd

		return rsList, tlList, remaining

class ValleyFilling(Alg):
	''' Valley filling charging scheme '''
	def setLimit(self, val):
		# Just for test use
		self.limit = val

	def solve(self):
		for level in range(self.limit + 1):
			# For each iteration, same as greedy, since it is already considered optimal
			remaining = self.total
			rsList = []
			tlList = []
			for ld in self.ldList:
				available = (level - ld) if (level - ld) > 0 else 0
				chargingLd = available if available < remaining else remaining
				rsList.append(chargingLd)
				tlList.append(chargingLd + ld)

				remaining -= chargingLd
			if remaining <= 0:
				break
		
		return rsList, tlList, remaining
