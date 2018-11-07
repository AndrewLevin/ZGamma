#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from  ewkzgjjFidCrossSectionModule import *

from  countHistogramsModule import *

p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv3/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/NANOAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/8C3E68AB-F5D2-E811-9D8A-E0071B7AC750.root"],None,"ewkzgjj_fid_cross_section_keep_and_drop.txt",[exampleModule()],provenance=True,justcount=False,noOut=False,histDirName="myhistdir",histFileName="myhistfile.root")

p.run()
