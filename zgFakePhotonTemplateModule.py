import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR

class exampleProducer(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("photon_sieie",  "F");
        self.out.branch("photon_pt",  "F");
        self.out.branch("photon_eta",  "F");
        self.out.branch("gen_weight",  "F");
        self.out.branch("lepton_pdg_id",  "I");
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        photons = Collection(event, "Photon")

        tight_muons = []

        loose_but_not_tight_muons = []

        tight_electrons = []

        loose_but_not_tight_electrons = []

        selected_photons = []

        for i in range(0,len(muons)):

            if muons[i].pt < 20:
                continue

            if abs(muons[i].eta) > 2.4:
                continue

            if muons[i].tightId and muons[i].pfRelIso04_all < 0.15:
                tight_muons.append(i)
            elif muons[i].pfRelIso04_all < 0.25:
                loose_but_not_tight_muons.append(i)

        for i in range (0,len(electrons)):

            if electrons[i].pt/electrons[i].eCorr < 20:
                continue

            if abs(electrons[i].eta) > 2.5:
                continue

            if (abs(electrons[i].eta + electrons[i].deltaEtaSC) < 1.479 and abs(electrons[i].dz) < 0.1 and abs(electrons[i].dxy) < 0.05) or (abs(electrons[i].eta + electrons[i].deltaEtaSC) > 1.479 and abs(electrons[i].dz) < 0.2 and abs(electrons[i].dxy) < 0.1):
                if electrons[i].cutBased >= 3:
                    tight_electrons.append(i)
                elif electrons[i].cutBased >= 1:
                    loose_but_not_tight_electrons.append(i)

        for i in range (0,len(photons)):

            if photons[i].pt/photons[i].eCorr < 20:
                continue

            if not ((abs(photons[i].eta) < 1.4442) or (1.566 < abs(photons[i].eta) and abs(photons[i].eta) < 2.5) ):
                continue

            #invert the medium photon ID with the sigma_ietaieta cut removed
            mask = (1 << 1) | (1 << 3) | (1 << 5) | (1 << 11) | (1 << 13)

            if not (mask & photons[i].vidNestedWPBitmap == mask):
                continue

            if photons[i].pixelSeed:
                continue

            if photons[i].pfRelIso03_chg*photons[i].pt > 10 or photons[i].pfRelIso03_chg*photons[i].pt < 4:
                continue
            
            pass_lepton_dr_cut = True

            for j in range(0,len(tight_muons)):

                if deltaR(muons[tight_muons[j]].eta,muons[tight_muons[j]].phi,photons[i].eta,photons[i].phi) < 0.7:
                    pass_lepton_dr_cut = False

            for j in range(0,len(tight_electrons)):
                
                if deltaR(electrons[tight_electrons[j]].eta,electrons[tight_electrons[j]].phi,photons[i].eta,photons[i].phi) < 0.7:
                    pass_lepton_dr_cut = False

            for j in range(0,len(loose_but_not_tight_muons)):

                if deltaR(muons[loose_but_not_tight_muons[j]].eta,muons[loose_but_not_tight_muons[j]].phi,photons[i].eta,photons[i].phi) < 0.7:
                    pass_lepton_dr_cut = False

            for j in range(0,len(loose_but_not_tight_electrons)):

                if deltaR(electrons[loose_but_not_tight_electrons[j]].eta,electrons[loose_but_not_tight_electrons[j]].phi,photons[i].eta,photons[i].phi) < 0.7:
                    pass_lepton_dr_cut = False

            if not pass_lepton_dr_cut:
                continue

            selected_photons.append(i)

        if (len(tight_muons) == 2) and (len(loose_but_not_tight_electrons)+ len(tight_electrons)+len(loose_but_not_tight_muons) == 0):
            if len(tight_muons) == 2:
                i1 = tight_muons[0]

                i2 = tight_muons[1]

            elif len(loose_but_not_tight_muons) == 2:    
                i1 = loose_but_not_tight_muons[0]

                i2 = loose_but_not_tight_muons[1]
            else:
                i1 = tight_muons[0]

                i2 = loose_but_not_tight_muons[0]

            if muons[i1].charge == muons[i2].charge:
                return False

            if not event.HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ and not event.HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ:
                return False

            if muons[i1].pt < 25:
                return False

            if muons[i2].pt < 25:
                return False

            if abs(muons[i1].eta) > 2.4:
                return False
                
            if abs(muons[i2].eta) > 2.4:
                return False

            if ((muons[i1].p4() + muons[i2].p4()).M() > 110) or ((muons[i1].p4() + muons[i2].p4()).M() < 70) :
                return False
                
        elif (len(tight_electrons) == 2) and (len(loose_but_not_tight_muons)+ len(tight_muons)+len(loose_but_not_tight_electrons) == 0):
            i1 = tight_electrons[0]

            i2 = tight_electrons[1]

            if electrons[i1].charge == electrons[i2].charge:
                return False

            if not event.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ:
                return False
                
            if electrons[i1].pt < 20:
                return False

            if electrons[i2].pt < 20:
                return False

            if abs(electrons[i1].eta) > 2.5:
                return False
                
            if abs(electrons[i2].eta) > 2.5:
                return False
                
            if ((electrons[i1].p4() + electrons[i2].p4()).M() > 110) or ((electrons[i1].p4() + electrons[i2].p4()).M() < 70) :
                return False

        if len(selected_photons) == 0:
            return False

        if len(loose_but_not_tight_muons) + len(loose_but_not_tight_electrons) + len(tight_electrons) + len(tight_muons) > 2:
            return False

        if len(tight_muons) == 2:

            i1 = tight_muons[0]

            i2 = tight_muons[1]

            if not event.HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ and not event.HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ:
                return False
            
            if muons[i1].pt < 20:
                return False

            if muons[i2].pt < 20:
                return False

            if abs(muons[i1].eta) > 2.4:
                return False

            if abs(muons[i2].eta) > 2.4:
                return False

            if muons[i1].pfRelIso04_all > 0.15:
                return False

            if muons[i2].pfRelIso04_all > 0.15:
                return False

            if not muons[i1].tightId:
                return False

            if not muons[i2].tightId:
                return False

            if muons[i1].charge == muons[i2].charge:
                return False
            
            if ((muons[i1].p4() + muons[i2].p4()).M() > 110) or ((muons[i1].p4() + muons[i2].p4()).M() < 70) :
                return False

            self.out.fillBranch("lepton_pdg_id",13)

        elif len(tight_electrons) == 2:

            i1 = tight_electrons[0]

            i2 = tight_electrons[1]

            if not event.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ:
                return False

            if electrons[i1].cutBased < 3:
                return False

            if electrons[i2].cutBased < 3:
                return False

            if electrons[i1].pt/electrons[i1].eCorr < 25:
                return False

            if electrons[i2].pt/electrons[i2].eCorr < 25:
                return False

            if abs(electrons[i1].eta) > 2.5:
                return False

            if abs(electrons[i2].eta) > 2.5:
                return False

            if electrons[i1].charge == electrons[i2].charge:
                return False
            
            if ((electrons[i1].p4() + electrons[i2].p4()).M() > 110) or ((electrons[i1].p4() + electrons[i2].p4()).M() < 70) :
                return False

            self.out.fillBranch("lepton_pdg_id",11)

        else:
            return False

        print "selected event: " + str(event.event) + " " + str(event.luminosityBlock) + " " + str(event.run)

        self.out.fillBranch("photon_sieie",photons[selected_photons[0]].sieie)
        self.out.fillBranch("photon_pt",photons[selected_photons[0]].pt)
        self.out.fillBranch("photon_eta",photons[selected_photons[0]].eta)

        try:
            self.out.fillBranch("gen_weight",event.Generator_weight)
        except:
            pass

        return True

exampleModule = lambda : exampleProducer() 

