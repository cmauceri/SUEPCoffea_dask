import uproot
import numpy as np
import ROOT
import awkward as ak
file=uproot.open("/eos/user/j/jreicher/SUEP/WH_private_signals/merged/WHleptonicpythia_leptonic_M125.0_MD1.00_T0.25_HT-1_UL16_NANOAOD.root")
events = file['Events'].arrays(['Flag_goodVertices',
                'Flag_globalSuperTightHalo2016Filter',
                'Flag_HBHENoiseFilter',
                'Flag_HBHENoiseIsoFilter',
                'Flag_EcalDeadCellTriggerPrimitiveFilter',
                'Flag_BadPFMuonFilter',
                'Flag_BadPFMuonDzFilter',
                'Flag_eeBadScFilter',
                'HLT_IsoMu27',
                'HLT_IsoMu24',
                'HLT_Mu50',
                'Muon_pt'])

triggerSingleMuon = (
            events.HLT_IsoMu27
            | events.HLT_IsoMu24
            | events.HLT_Mu50
        )
    
cutAnyFilter = (
                (events.Flag_goodVertices)
                & (events.Flag_globalSuperTightHalo2016Filter)
                & (events.Flag_HBHENoiseFilter)
                & (events.Flag_HBHENoiseIsoFilter)
                & (events.Flag_EcalDeadCellTriggerPrimitiveFilter)
                & (events.Flag_BadPFMuonFilter)
                & (events.Flag_BadPFMuonDzFilter)
                & (events.Flag_eeBadScFilter)
            )
def efficiencies(evs,trigger):
    # Define bin size, max and min for the pT
    pt_bin=10
    max_pt=200
    min_pt=0
    # Initialize array for efficiencies
    effs=np.zeros(int(max_pt/pt_bin))
    #  fill efficiencies in bins of pT
    for cut in range(20):
        cut_pt=(evs.Muon_pt) > (cut*pt_bin) #& (evs.Muon_pt < (cut*pt_bin + pt_bin))
        #print(cut_pt)
        cut_sig=evs[cut_pt]
        cut_tr=evs[trigger & cut_pt]
        #print(len(cut_tr))
        #print(cut_sig)
        effs[cut]=len(cut_tr)/len(cut_sig)
    return effs
signal=events.Muon_pt
efficiencies(events,triggerSingleMuon)
