def GetPrefireWeights(self, events):
    if self.era == "2016" or self.era == "2017" or self.era == "2016apv":
        if self.scouting == 1:
            self.out_vars["prefire_nom"] = events.prefire
            self.out_vars["prefire_up"] = events.prefireup
            self.out_vars["prefire_down"] = events.prefiredown
        else:
            self.out_vars["prefire_nom"] = events.L1PreFiringWeight.Nom
            self.out_vars["prefire_up"] = events.L1PreFiringWeight.Up
            self.out_vars["prefire_down"] = events.L1PreFiringWeight.Dn
    else:
        self.out_vars["prefire_nom"] = 1.0
        self.out_vars["prefire_up"] = 1.0
        self.out_vars["prefire_down"] = 1.0
    return
