# python 3
# this class combines all basic features of a generic player
import numpy as np

"""
pseudo code du coordinateur
p = np.rand(48)
prices = {"purchase": p, "sale": p}

p = Player()
## pour tous les acteurs sauf la station de recharge 
## scenario_data est un np.array de taille 48
## pour la station de recharge
## scenario_data est:
## def set_scenario(self, scenario_data):
##        arr_dep = list(scenario_data.values())[:self.nb_slow+self.nb_fast]
##        self.depart = {"slow": [d[1] for d in arr_dep[:self.nb_slow]], "fast": [d[1] for d in arr_dep[self.nb_slow:self.nb_fast+self.nb_slow]]}
##        self.arrival = {"slow": [d[0] for d in arr_dep[:self.nb_slow]], "fast": [d[0] for d in arr_dep[self.nb_slow:self.nb_fast+self.nb_slow]]}

p.set_scenario(scenario_data)


for i in range(N):
    p.set_prices(prices)
    load_player_24h = p.compute_all_load()


"""

class Player:

	def __init__(self):
		# some player might not have parameters
		self.parameters = 0
		self.horizon = 48

	def set_scenario(self, scenario_data):
		self.data = scenario_data
		# Pour les VE
		# arr_dep = list(scenario_data.values())[:self.nb_slow+self.nb_fast]
		# self.depart = {"slow": [d[1] for d in arr_dep[:self.nb_slow]], "fast": [d[1] for d in arr_dep[self.nb_slow:self.nb_fast+self.nb_slow]]}
		# self.arrival = {"slow": [d[0] for d in arr_dep[:self.nb_slow]], "fast": [d[0] for d in arr_dep[self.nb_slow:self.nb_fast+self.nb_slow]]}
		

	def set_prices(self, prices):
		self.prices = prices

	def compute_all_load(self):
		load = np.zeros(self.horizon)
		# for time in range(self.horizon):
		# 	load[time] = self.compute_load(time)
		return load

	def take_decision(self, time):
		# TO BE COMPLETED
		return 0

	def compute_load(self, time):
		load = self.take_decision(time)
		# do stuff ?
		return load

	def reset(self):
		# reset all observed data
		pass

	
if __name__ == '__main__':
	mon_acteur = Player()
	load_0 = mon_acteur.compute_load(0)
	load_0 = mon_acteur.compute_load(1)	
