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
        self.out.branch("lepton_pdg_id",  "i");
        self.out.branch("run",  "i");
        self.out.branch("lumi",  "i");
        self.out.branch("event",  "l");
        self.out.branch("photon_pt",  "F");
        self.out.branch("photon_eta",  "F");
        self.out.branch("mjj",  "F");
        self.out.branch("detajj",  "F");
        self.out.branch("zep",  "F");
        self.out.branch("mzg",  "F");
        self.out.branch("mengsvariable",  "F");
        #self.out.branch("EventMass",  "F");

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

        tight_photons = []

        tight_jets = []

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
            
            if photons[i].pt/photons[i].eCorr < 25:
                continue

            if not ((abs(photons[i].eta) < 1.4442) or (1.566 < abs(photons[i].eta) and abs(photons[i].eta) < 2.5) ):
                continue        

            if photons[i].cutBased == 0 or photons[i].cutBased == 1:
                continue

            if not photons[i].electronVeto:
                continue

            pass_lepton_dr_cut = True

            for j in range(0,len(tight_muons)):

                #print "deltaR(muons[tight_muons[j]].eta,muons[tight_muons[j]].phi,photons[i].eta,photons[i].phi) = "+str(deltaR(muons[tight_muons[j]].eta,muons[tight_muons[j]].phi,photons[i].eta,photons[i].phi))

                if deltaR(muons[tight_muons[j]].eta,muons[tight_muons[j]].phi,photons[i].eta,photons[i].phi) < 0.7:
                    pass_lepton_dr_cut = False

            for j in range(0,len(tight_electrons)):
                
                #print "deltaR(electrons[tight_electrons[j]].eta,electrons[tight_electrons[j]].phi,photons[i].eta,photons[i].phi) = "+str(deltaR(electrons[tight_electrons[j]].eta,electrons[tight_electrons[j]].phi,photons[i].eta,photons[i].phi))

                if deltaR(electrons[tight_electrons[j]].eta,electrons[tight_electrons[j]].phi,photons[i].eta,photons[i].phi) < 0.7:
                    pass_lepton_dr_cut = False

            for j in range(0,len(loose_but_not_tight_muons)):

                #print "deltaR(muons[loose_but_not_tight_muons[j]].eta,muons[loose_but_not_tight_muons[j]].phi,photons[i].eta,photons[i].phi) = "+str(deltaR(muons[loose_but_not_tight_muons[j]].eta,muons[loose_but_not_tight_muons[j]].phi,photons[i].eta,photons[i].phi))

                if deltaR(muons[loose_but_not_tight_muons[j]].eta,muons[loose_but_not_tight_muons[j]].phi,photons[i].eta,photons[i].phi) < 0.7:
                    pass_lepton_dr_cut = False

            for j in range(0,len(loose_but_not_tight_electrons)):

                #print "deltaR(electrons[loose_but_not_tight_electrons[j]].eta,electrons[loose_but_not_tight_electrons[j]].phi,photons[i].eta,photons[i].phi) = "+str(deltaR(electrons[loose_but_not_tight_electrons[j]].eta,electrons[loose_but_not_tight_electrons[j]].phi,photons[i].eta,photons[i].phi))

                if deltaR(electrons[loose_but_not_tight_electrons[j]].eta,electrons[loose_but_not_tight_electrons[j]].phi,photons[i].eta,photons[i].phi) < 0.7:
                    pass_lepton_dr_cut = False

            if not pass_lepton_dr_cut:
                continue

            tight_photons.append(i)

        for i in range(0,len(jets)):

            if jets[i].pt < 30:
                continue

            if abs(jets[i].eta) > 4.7:
                continue

            if not jets[i].jetId & (1 << 0):
                continue

            #if not jets[i].puId & (1 << 2):
            #    continue

            pass_photon_dr_cut = True

            for j in range(0,len(tight_photons)):

                if deltaR(photons[tight_photons[j]].eta,photons[tight_photons[j]].phi,jets[i].eta,jets[i].phi) < 0.5:
                    pass_photon_dr_cut = False

            if not pass_photon_dr_cut:
                continue

            pass_lepton_dr_cut = True

            for j in range(0,len(tight_muons)):

                if deltaR(muons[tight_muons[j]].eta,muons[tight_muons[j]].phi,jets[i].eta,jets[i].phi) < 0.4:
                    pass_lepton_dr_cut = False

            for j in range(0,len(tight_electrons)):
                
                if deltaR(electrons[tight_electrons[j]].eta,electrons[tight_electrons[j]].phi,jets[i].eta,jets[i].phi) < 0.4:
                    pass_lepton_dr_cut = False

            for j in range(0,len(loose_but_not_tight_muons)):

                if deltaR(muons[loose_but_not_tight_muons[j]].eta,muons[loose_but_not_tight_muons[j]].phi,jets[i].eta,jets[i].phi) < 0.4:
                    pass_lepton_dr_cut = False

            for j in range(0,len(loose_but_not_tight_electrons)):

                if deltaR(electrons[loose_but_not_tight_electrons[j]].eta,electrons[loose_but_not_tight_electrons[j]].phi,jets[i].eta,jets[i].phi) < 0.4:
                    pass_lepton_dr_cut = False

            if not pass_lepton_dr_cut:
                continue

            tight_jets.append(i)

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
                
#            print "selected meng lu muon event: " + str(event.event) + " " + str(event.luminosityBlock) + " " + str(event.run)

        if (len(tight_electrons) == 2) and (len(loose_but_not_tight_muons)+ len(tight_muons)+len(loose_but_not_tight_electrons) == 0):
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
                
#            print "selected meng lu electron event: " + str(event.event) + " " + str(event.luminosityBlock) + " " + str(event.run)

        if len(tight_jets) < 2:
            return False

        if len(tight_photons) == 0:
            return False

        if jets[tight_jets[0]].pt < 30:
            return False

        if jets[tight_jets[1]].pt < 30:
            return False

        if abs(jets[tight_jets[0]].eta) > 4.7:
            return False

        if abs(jets[tight_jets[1]].eta) > 4.7:
            return False

        if (jets[tight_jets[0]].p4() + jets[tight_jets[1]].p4()).M() < 150:
            return False

        #if abs(jets[0].p4().Eta() - jets[1].p4().Eta()) < 2.5:
        #    return False

        if photons[tight_photons[0]].pt/photons[tight_photons[0]].eCorr < 25:
            return False

        #if not ((abs(photons[tight_photons[0]].eta) < 1.4442) or (1.566 < abs(photons[tight_photons[0]].eta) and abs(photons[tight_photons[0]].eta) < 2.5) ):
        #    return False        

        if not abs(photons[tight_photons[0]].eta) < 1.4442:
            return False        

        if photons[tight_photons[0]].cutBased == 0 or photons[tight_photons[0]].cutBased == 1:
            return False

        if not photons[tight_photons[0]].electronVeto:
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

            self.out.fillBranch("zep",abs((muons[i1].p4() + muons[i2].p4() + photons[tight_photons[0]].p4()).Eta() - (jets[tight_jets[0]].eta + jets[tight_jets[1]].eta)/2))

            self.out.fillBranch("mzg",(muons[i1].p4() + muons[i2].p4() + photons[tight_photons[0]].p4()).M())

            self.out.fillBranch("mengsvariable",abs((muons[i1].p4() + muons[i2].p4() + photons[tight_photons[0]].p4()).Phi() - (jets[tight_jets[0]].p4() + jets[tight_jets[1]].p4()).Phi()/2))

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

            self.out.fillBranch("zep",abs((electrons[i1].p4() + electrons[i2].p4() + photons[tight_photons[0]].p4()).Eta() - (jets[tight_jets[0]].eta + jets[tight_jets[1]].eta)/2))

            self.out.fillBranch("mzg",(electrons[i1].p4() + electrons[i2].p4() + photons[tight_photons[0]].p4()).M())

            self.out.fillBranch("mengsvariable",abs((electrons[i1].p4() + electrons[i2].p4() + photons[tight_photons[0]].p4()).Phi() - (jets[tight_jets[0]].p4() + jets[tight_jets[1]].p4()).Phi()/2))

        else:
            return False

        print "selected event: " + str(event.event) + " " + str(event.luminosityBlock) + " " + str(event.run)


        self.out.fillBranch("photon_pt",photons[tight_photons[0]].pt)
        self.out.fillBranch("photon_eta",photons[tight_photons[0]].eta)
        self.out.fillBranch("mjj",(jets[tight_jets[0]].p4() + jets[tight_jets[1]].p4()).M())

        self.out.fillBranch("detajj",abs(jets[tight_jets[0]].eta - jets[tight_jets[1]].eta))
        self.out.fillBranch("event",event.event)
        self.out.fillBranch("lumi",event.luminosityBlock)
        self.out.fillBranch("run",event.run)        

        #print event.event


        #self.out.fillBranch("EventMass",eventSum.M())
        #if eventSum.M() < 2000:
        #    return False
        #else:
        #    return True

        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

exampleModule = lambda : exampleProducer() 

