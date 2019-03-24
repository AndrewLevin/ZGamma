#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from  zgFakePhotonModule import *

from  countHistogramsModule import *

from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

p=PostProcessor(".",inputFiles(),None,"zg_fake_photon_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel = "zg_fake_photon_output_branch_selection.txt")

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2017B/DoubleEG/NANOAOD/Nano14Dec2018-v1/10000/FC0F0BE5-5D07-9C4A-B1FB-EDE0BCE0B842.root"],"","zg_fake_photon_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,outputbranchsel = "output_branch_selection.txt")

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2017C/DoubleEG/NANOAOD/Nano14Dec2018-v1/90000/F97D46E1-FABC-4F4F-873D-9BCACCD1FFCF.root"],"","zg_fake_photon_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,outputbranchsel = "output_branch_selection.txt")

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2017F/DoubleMuon/NANOAOD/Nano14Dec2018-v1/90000/30F35CF0-A0D2-B24A-99CA-38775280E38F.root "],"","zg_fake_photon_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,outputbranchsel = "output_branch_selection.txt")

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2017B/DoubleMuon/NANOAOD/Nano14Dec2018-v1/280000/FB901F01-98AA-214F-A2C2-D67630861952.root"],"","zg_fake_photon_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,outputbranchsel = "output_branch_selection.txt")

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/2A93F220-480C-E811-B41A-FA163E62B5E7.root","root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/3C52A3B5-540C-E811-8F16-FA163EA77E04.root","root://cms-xrd-global.cern.ch/store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/3E58C862-A20C-E811-A231-90E2BAC9B7A8.root","root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/464C1632-A20C-E811-9FA3-FA163E5303D3.root","root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/54EEA3FF-460C-E811-AF8A-FA163EED3A98.root"],"","zg_fake_photon_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,outputbranchsel = "output_branch_selection.txt")

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/40000/E44F048D-A613-E811-8DBC-02163E013BEB.root"],"","zg_fake_photon_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,outputbranchsel = "output_branch_selection.txt")

p.run()
