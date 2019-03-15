import ROOT

ROOT.gStyle.SetOptStat(0)

sieie_sideband_file = ROOT.TFile("/afs/cern.ch/work/a/amlevin/data/zg/zjets_fake_photon_template.root")
sieie_file = ROOT.TFile("/afs/cern.ch/work/a/amlevin/data/zg/zjets_fake_photon.root")

sieie_sideband_tree = sieie_sideband_file.Get("Events")
sieie_tree = sieie_file.Get("Events")

#sieie_sideband_th1f=ROOT.TH1F("sieie_1","sieie_1",100,0,0.05)
#sieie_th1f=ROOT.TH1F("sieie_2","sieie_2",100,0,0.05)

sieie_sideband_th1f=ROOT.TH1F("sieie_1","sieie_1",6,0.014,0.062)
sieie_th1f=ROOT.TH1F("sieie_2","sieie_2",6,0.014,0.062)

for i in range(sieie_sideband_tree.GetEntries()):
    sieie_sideband_tree.GetEntry(i)

    if not (abs(sieie_sideband_tree.photon_pt) > 25 and abs(sieie_sideband_tree.photon_pt) < 35):
        continue

    if not (abs(sieie_sideband_tree.photon_eta) > 1.566 and abs(sieie_sideband_tree.photon_eta) < 2.5):
        continue

    if not (abs(sieie_sideband_tree.lepton_pdg_id) == 13):
        continue

    if sieie_sideband_tree.gen_weight > 0:
        sieie_sideband_th1f.Fill(sieie_sideband_tree.photon_sieie)
    else:    
        sieie_sideband_th1f.Fill(sieie_sideband_tree.photon_sieie,-1)

for i in range(sieie_tree.GetEntries()):
    sieie_tree.GetEntry(i)

    if not (abs(sieie_tree.photon_pt) > 25 and abs(sieie_tree.photon_pt) < 35):
        continue

    if not (abs(sieie_tree.photon_eta) > 1.566 and abs(sieie_tree.photon_eta) < 2.5):
        continue

    if not (abs(sieie_tree.lepton_pdg_id) == 13):
        continue

    if not (sieie_tree.photon_selection == 2 or sieie_tree.photon_selection == 1):
        continue

    if not (sieie_tree.photon_gen_matching == 0):
        continue

    if sieie_tree.gen_weight > 0:
        sieie_th1f.Fill(sieie_tree.photon_sieie)
    else:    
        sieie_th1f.Fill(sieie_tree.photon_sieie,-1)

c1 = ROOT.TCanvas()

sieie_th1f.SetTitle("")
sieie_sideband_th1f.SetTitle("")

sieie_th1f.Scale(1/sieie_th1f.Integral())
sieie_sideband_th1f.Scale(1/sieie_sideband_th1f.Integral())

sieie_th1f.GetXaxis().SetTitle("\sigma_{i\eta i\eta}")

sieie_th1f.SetLineColor(ROOT.kRed)
sieie_sideband_th1f.SetLineColor(ROOT.kBlue)

sieie_th1f.SetLineWidth(3)
sieie_sideband_th1f.SetLineWidth(3)

sieie_th1f.Draw()
sieie_sideband_th1f.Draw("same")

leg=ROOT.TLegend(.58,.73,.88,.88)
leg.AddEntry(sieie_th1f,"z+jets MC","l")
leg.AddEntry(sieie_sideband_th1f,"z+jets sideband MC","l")

leg.Draw("same")

c1.SaveAs("/eos/user/a/amlevin/www/tmp/delete_this.png")
