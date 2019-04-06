#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from  ewkzgjjModule import *

from  countHistogramsModule import *

from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

p=PostProcessor(".",inputFiles(),None,"ewkzgjj_keep_and_drop.txt",[countHistogramsModule(),ewkzgjjModule()],provenance=True,justcount=False,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel = "ewkzgjj_output_branch_selection.txt")

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/2A93F220-480C-E811-B41A-FA163E62B5E7.root","root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/3C52A3B5-540C-E811-8F16-FA163EA77E04.root","root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/3E58C862-A20C-E811-A231-90E2BAC9B7A8.root","root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/464C1632-A20C-E811-9FA3-FA163E5303D3.root","root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/54EEA3FF-460C-E811-AF8A-FA163EED3A98.root"],"nJet >= 2 && Jet_pt[0] >= 30 && Jet_pt[1] >= 30 && nPhoton >= 1 && Photon_pt[0] > 25 && nMuon >= 2 && Muon_pt[0] > 20 && Muon_pt[1] > 20","keep_and_drop.txt",[exampleModule()],provenance=True,justcount=False,noOut=False)
#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/2A93F220-480C-E811-B41A-FA163E62B5E7.root"],"nJet >= 2 && Jet_pt[0] >= 30 && Jet_pt[1] >= 30 && nPhoton >= 1 && Photon_pt[0] > 25 && nMuon >= 2 && Muon_pt[0] > 20 && Muon_pt[1] > 20","keep_and_drop.txt",[exampleModule()],provenance=True,justcount=False,noOut=False)

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2016G/DoubleMuon/NANOAOD/05Feb2018-v1/20000/0CF614B4-700C-E811-B3AC-FA163EB9BAB5.root"],None,"ewkzgjj_keep_and_drop.txt",[countHistogramsModule(),ewkzgjjModule()],provenance=True,justcount=False,jsonInput="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",noOut=False,outputbranchsel = "ewkzgjj_output_branch_selection.txt")

p.run()
