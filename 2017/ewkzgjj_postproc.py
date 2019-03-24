#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from  ewkzgjjModule import *

from  countHistogramsModule import *

#from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

#p=PostProcessor(".",inputFiles(),None,"ewkzgjj_keep_and_drop.txt",[countHistogramsModule(),ewkzgjjModule()],provenance=True,justcount=False,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel = "ewkzgjj_output_branch_selection.txt")

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2017B/DoubleEG/NANOAOD/Nano14Dec2018-v1/10000/FC0F0BE5-5D07-9C4A-B1FB-EDE0BCE0B842.root"],None,"keep_and_drop.txt",[countHistogramsModule(),ewkzgjjModule()],provenance=True,justcount=False,noOut=False,outputbranchsel = "output_branch_selection.txt")

p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAODv4/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v3/260000/05CC0B0B-8D53-1941-9804-072BC83F2439.root"],None,"keep_and_drop.txt",[countHistogramsModule(),ewkzgjjModule()],provenance=True,justcount=False,noOut=False,outputbranchsel = "output_branch_selection.txt")

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAODv4/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v3/260000/05CC0B0B-8D53-1941-9804-072BC83F2439.root"],"event == 49051079","keep_and_drop.txt",[countHistogramsModule(),ewkzgjjModule()],provenance=True,justcount=False,noOut=False,outputbranchsel = "output_branch_selection.txt")

p.run()
