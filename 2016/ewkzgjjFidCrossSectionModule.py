import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR

class exampleProducer(Module):
    def __init__(self):
        pass
    def beginJob(self):
        self.nselectedevents = 0

        pass
    def endJob(self):

        print self.nselectedevents

        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        #self.out.branch("EventMass",  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        genjets = Collection(event, "GenJet")
        genparts = Collection(event, "GenPart")
        lheparts = Collection(event, "LHEPart")

        photons = []

        jets = []

        electrons = []

        muons = []

        for i in range(0,len(lheparts)):

            if lheparts[i].pdgId == 22:
                photons.append(i)

            if abs(lheparts[i].pdgId) == 11:
                muons.append(i)

            if abs(lheparts[i].pdgId) == 13:
                electrons.append(i)

            if abs(lheparts[i].pdgId) == 1 or abs(lheparts[i].pdgId) == 2 or abs(lheparts[i].pdgId) == 3 or abs(lheparts[i].pdgId) == 4 or abs(lheparts[i].pdgId) == 5 or abs(lheparts[i].pdgId) == 21:
                jets.append(i)

        assert(len(photons) == 1)
        
        assert((len(muons) == 0 and len(electrons) == 0) or (len(muons) == 2 and len(electrons) == 0) or (len(muons) == 0 and len(electrons) == 2)) 

        assert(len(jets) == 2)

        if lheparts[jets[0]].pt < 30 or lheparts[jets[1]].pt < 30:
            return False

        if abs(lheparts[jets[0]].eta) > 4.7 or abs(lheparts[jets[1]].eta) > 4.7:
            return False

        if (lheparts[jets[0]].p4() + lheparts[jets[1]].p4()).M() < 500:
            return False

        if abs(lheparts[jets[0]].eta -  lheparts[jets[1]].eta) < 2.5:
            return False

        if len(electrons) == 2:

            if lheparts[electrons[0]].pt < 25 or abs(lheparts[electrons[0]].eta) > 2.5:
                return False

            if lheparts[electrons[1]].pt < 25 or abs(lheparts[electrons[1]].eta) > 2.5:
                return False

            if (lheparts[electrons[0]].p4() + lheparts[electrons[1]].p4()).M() < 70 or (lheparts[electrons[0]].p4() + lheparts[electrons[1]].p4()).M() > 110:
                return False

            if deltaR(lheparts[photons[0]].eta,lheparts[photons[0]].phi,lheparts[electrons[0]].eta,lheparts[electrons[0]].phi) < 0.7:
                return False

            if deltaR(lheparts[photons[0]].eta,lheparts[photons[0]].phi,lheparts[electrons[1]].eta,lheparts[electrons[1]].phi) < 0.7:
                return False

            if deltaR(lheparts[jets[0]].eta,lheparts[jets[0]].phi,lheparts[electrons[0]].eta,lheparts[electrons[0]].phi) < 0.5:
                return False

            if deltaR(lheparts[jets[0]].eta,lheparts[jets[0]].phi,lheparts[electrons[1]].eta,lheparts[electrons[1]].phi) < 0.5:
                return False

            if deltaR(lheparts[jets[1]].eta,lheparts[jets[1]].phi,lheparts[electrons[0]].eta,lheparts[electrons[0]].phi) < 0.5:
                return False

            if deltaR(lheparts[jets[1]].eta,lheparts[jets[1]].phi,lheparts[electrons[1]].eta,lheparts[electrons[1]].phi) < 0.5:
                return False

        elif len(muons) == 2:

            if lheparts[muons[0]].pt < 20 or abs(lheparts[muons[0]].eta) > 2.4:
                return False

            if lheparts[muons[1]].pt < 20 or abs(lheparts[muons[1]].eta) > 2.4:
                return False

            if (lheparts[muons[0]].p4() + lheparts[muons[1]].p4()).M() < 70 or (lheparts[muons[0]].p4() + lheparts[muons[1]].p4()).M() > 110:
                return False

            if deltaR(lheparts[photons[0]].eta,lheparts[photons[0]].phi,lheparts[muons[0]].eta,lheparts[muons[0]].phi) < 0.7:
                return False

            if deltaR(lheparts[photons[0]].eta,lheparts[photons[0]].phi,lheparts[muons[1]].eta,lheparts[muons[1]].phi) < 0.7:
                return False

            if deltaR(lheparts[jets[0]].eta,lheparts[jets[0]].phi,lheparts[muons[0]].eta,lheparts[muons[0]].phi) < 0.5:
                return False

            if deltaR(lheparts[jets[0]].eta,lheparts[jets[0]].phi,lheparts[muons[1]].eta,lheparts[muons[1]].phi) < 0.5:
                return False

            if deltaR(lheparts[jets[1]].eta,lheparts[jets[1]].phi,lheparts[muons[0]].eta,lheparts[muons[0]].phi) < 0.5:
                return False

            if deltaR(lheparts[jets[1]].eta,lheparts[jets[1]].phi,lheparts[muons[1]].eta,lheparts[muons[1]].phi) < 0.5:
                return False
        else:
            return False

        if lheparts[photons[0]].pt < 25:
            return False

        if not ((abs(lheparts[photons[0]].eta) < 1.4442) or (1.566 < abs(lheparts[photons[0]].eta) and abs(lheparts[photons[0]].eta) < 2.5)):
            return False

        if deltaR(lheparts[jets[0]].eta,lheparts[jets[0]].phi,lheparts[jets[1]].eta,lheparts[jets[1]].phi) < 0.5:
            return False

        if deltaR(lheparts[jets[0]].eta,lheparts[jets[0]].phi,lheparts[photons[0]].eta,lheparts[photons[0]].phi) < 0.5:
            return False

        if deltaR(lheparts[jets[1]].eta,lheparts[jets[1]].phi,lheparts[photons[0]].eta,lheparts[photons[0]].phi) < 0.5:
            return False

        self.nselectedevents += 1

        return True

exampleModule = lambda : exampleProducer() 

