## python 3
# this class combines all basic features of a generic player
import numpy as np
from pulp import *
import pandas as pd
from pulp import *
import numpy as np
sys.path.append(os.getcwd()+'/../../')
df = pd.read_csv("data_center_weekly_scenarios.csv", sep = ";")
l_IT_global = np.array(df["cons (kW)"])
hotwater_price_prevision
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
EER = 4
dt = 0.5
COP_CS = EER + 1
Tcom = 60 +273
Tr = 35 +273
e = 0.5
COP_HP = Tcom * e / (Tcom - Tr)



class Data_center:

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
        l_IT = np.array([l_IT_global[i+time]]for i in range(self.horizon)) #on étudie le scénario à partir de la consommation minimale entre t et t+24h
        lambdas = self.prices()
        problem = LpProblem("data_center", LpMinimize)
        alphas = [0 for i in range(48)]
        alpha = [0 for i in range(48)]
        LI = [0 for i in range(48)]
        for i in range(horizon):
            var_name = "alpha_" + str(i)
            alphas[i] = LpVariable(var_name, 0.0, 1.0)

        l_NF = [0 for i in range(self.horizon)]
        h_r = [0 for i in range(self.horizon)]
        l_HP = [0 for i in range(self.horizon)]
        h_DC = [0 for i in range(self.horizon)]
        li = [0 for i in range(self.horizon)]

        for t in range(self.horizon):
            l_NF[t] = (1 + 1 / (EER * dt)) * l_IT[t]
            h_r[t] = l_IT[t] * COP_CS / EER
            l_HP[t] = alphas[t] * h_r[t] / ((COP_HP - 1) * dt)
            h_DC[t] = COP_HP * dt * l_HP[t]
            cons_name = "production limite en " + str(t)
            problem += h_DC[t] <= 10
            li[t] = l_HP[t] + l_NF[t]

        problem += np.sum([lambdas[i] * (l_NF[i] + h_DC[i]) - hotwater_price_prevision[i] * h_DC[i] for i in range(self.horizon)]), "objectif"

        problem.solve()
        for i in range (48):
            alpha[i] = alphas[i].value()
            LI[i] = li[i].value() #permet d'avoir les aleurs effectives

        self.set_scenario(LI)# on actualise la consommation effective pour la journée qui vient
        return 0

    def compute_load(self, time):
        load = self.take_decision(time)
        # do stuff ?
        return load

    def reset(self):
        # reset all observed data
        pass


if __name__ == '__main__':
    mon_acteur = Data_center()
    load_0 = mon_acteur.compute_load(0)
    load_0 = mon_acteur.compute_load(1)

