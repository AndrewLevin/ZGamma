#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from  zgRealPhotonTemplateModule import *

from countHistogramsModule import *

#from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/100000/08265D2D-B066-E811-929E-5EE3F46D4772.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/100000/CE3FDB71-A466-E811-8898-001E67E6F67F.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/100000/F632B479-9E66-E811-97CB-0CC47AD98BC6.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/100000/F880A27A-7866-E811-99B7-C4346BC8D390.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/2AB69B55-A666-E811-AF5A-E2D1094F814F.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/381EF8C1-5D66-E811-8A1F-0CC47AD98D0C.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/70689210-7A66-E811-B9AE-5EE3F46D4772.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/80F25A5E-A666-E811-957B-0CC47AD99052.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/C828C60D-6D66-E811-A322-5EE3F46D4772.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/E463BF72-8A66-E811-9938-0CC47ADAF3DA.root"],"","zg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "zg_real_photon_template_output_branch_selection.txt")

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/100000/08265D2D-B066-E811-929E-5EE3F46D4772.root"],"","zg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "output_branch_selection.txt") #works

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/100000/CE3FDB71-A466-E811-8898-001E67E6F67F.root"],"","zg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "output_branch_selection.txt") #works

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/100000/F632B479-9E66-E811-97CB-0CC47AD98BC6.root"],"","zg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "output_branch_selection.txt") #works

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/100000/F880A27A-7866-E811-99B7-C4346BC8D390.root"],"","zg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "output_branch_selection.txt") #works

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/2AB69B55-A666-E811-AF5A-E2D1094F814F.root"],"","zg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "output_branch_selection.txt") #works

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/381EF8C1-5D66-E811-8A1F-0CC47AD98D0C.root"],"","zg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "output_branch_selection.txt")  #works

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/70689210-7A66-E811-B9AE-5EE3F46D4772.root"],"","zg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "output_branch_selection.txt") #works

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/80F25A5E-A666-E811-957B-0CC47AD99052.root"],"","zg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "output_branch_selection.txt") #works

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/C828C60D-6D66-E811-A322-5EE3F46D4772.root"],"","zg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "output_branch_selection.txt") #works

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/50000/E463BF72-8A66-E811-9938-0CC47ADAF3DA.root"],"","zg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),exampleModule()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "output_branch_selection.txt") #works

p.run()

print "DONE"
os.system("ls -lR")
