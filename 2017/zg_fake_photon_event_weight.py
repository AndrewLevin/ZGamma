import ROOT

from array import array

photon_ptbins=array('d', [25,30,40,50,70,100,135,400])

import json

import numpy as np

#fake_photon_event_weights = json.load(open("fake_photon_event_weights/fake_photon_event_weights_data.txt"))
fake_photon_event_weights = json.load(open("fake_photon_event_weights_data.txt"))

fake_photon_event_weights_muon_barrel = list(np.array(fake_photon_event_weights["muon_barrel"])[:,0])

fake_photon_event_weights_muon_endcap = list(np.array(fake_photon_event_weights["muon_endcap"])[:,0])

fake_photon_event_weights_electron_barrel = list(np.array(fake_photon_event_weights["electron_barrel"])[:,0])

fake_photon_event_weights_electron_endcap = list(np.array(fake_photon_event_weights["electron_endcap"])[:,0])

fake_photon_event_weights_muon_barrel_hist=ROOT.TH1F("fake_photon_event_weights_muon_barrel_hist","fake_photon_event_weights_muon_barrel_hist",len(photon_ptbins)-1,photon_ptbins)
fake_photon_event_weights_electron_barrel_hist=ROOT.TH1F("fake_photon_event_weights_electron_barrel_hist","fake_photon_event_weights_electron_barrel_hist",len(photon_ptbins)-1,photon_ptbins)
fake_photon_event_weights_muon_endcap_hist=ROOT.TH1F("fake_photon_event_weights_muon_endcap_hist","fake_photon_event_weights_muon_endcap_hist",len(photon_ptbins)-1,photon_ptbins)
fake_photon_event_weights_electron_endcap_hist=ROOT.TH1F("fake_photon_event_weights_electron_endcap_hist","fake_photon_event_weights_electron_endcap_hist",len(photon_ptbins)-1,photon_ptbins)

for i in range(fake_photon_event_weights_muon_barrel_hist.GetNbinsX()):
    fake_photon_event_weights_muon_barrel_hist.SetBinContent(i+1,fake_photon_event_weights_muon_barrel[i])

for i in range(fake_photon_event_weights_electron_barrel_hist.GetNbinsX()):
    fake_photon_event_weights_electron_barrel_hist.SetBinContent(i+1,fake_photon_event_weights_electron_barrel[i])

for i in range(fake_photon_event_weights_muon_endcap_hist.GetNbinsX()):
    fake_photon_event_weights_muon_endcap_hist.SetBinContent(i+1,fake_photon_event_weights_muon_endcap[i])

for i in range(fake_photon_event_weights_electron_endcap_hist.GetNbinsX()):
    fake_photon_event_weights_electron_endcap_hist.SetBinContent(i+1,fake_photon_event_weights_electron_endcap[i])

print fake_photon_event_weights_muon_barrel

def fake_photon_event_weight(eta,pt,lepton_pdg_id,use_alt=False,stat_err_up = False):

    if abs(lepton_pdg_id) == 11:
        if abs(eta) < 1.4442:
            mypt   = min(pt,399.999)
            fr = fake_photon_event_weights_electron_barrel_hist.GetBinContent(fake_photon_event_weights_electron_barrel_hist.GetXaxis().FindFixBin(mypt))
            return fr

        elif 1.566 < abs(eta) and abs(eta) < 2.5:
            mypt   = min(pt,399.999)
            fr = fake_photon_event_weights_electron_endcap_hist.GetBinContent(fake_photon_event_weights_electron_endcap_hist.GetXaxis().FindFixBin(mypt))
            return fr

        else:

            assert(0)
    elif abs(lepton_pdg_id) == 13:
        if abs(eta) < 1.4442:
            mypt   = min(pt,399.999)
            fr = fake_photon_event_weights_muon_barrel_hist.GetBinContent(fake_photon_event_weights_muon_barrel_hist.GetXaxis().FindFixBin(mypt))
            return fr

        elif 1.566 < abs(eta) and abs(eta) < 2.5:
            mypt   = min(pt,399.999)
            fr = fake_photon_event_weights_muon_endcap_hist.GetBinContent(fake_photon_event_weights_muon_endcap_hist.GetXaxis().FindFixBin(mypt))
            return fr

        else:

            assert(0)

    else:

        assert(0)
