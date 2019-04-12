import ROOT

import json

import style

style.GoodStyle().cd()

from zg_fake_photon_event_weight import fake_photon_event_weight

xoffsetstart = 0.0;
yoffsetstart = 0.0;
xoffset = 0.20;
yoffset = 0.05;

xpositions = [0.68,0.68,0.68,0.68,0.445,0.445,0.445,0.445,0.21,0.21,0.21,0.21]
ypositions = [0,1,2,3,0,1,2,3,0,1,2,3]

def set_axis_fonts(thstack, coordinate, title):

    if coordinate == "x":
        axis = thstack.GetXaxis();
    elif coordinate == "y":
        axis = thstack.GetYaxis();
    else:
        assert(0)
    
    axis.SetLabelFont  (   42)
    axis.SetLabelOffset(0.015)
    axis.SetLabelSize  (0.050)
    axis.SetNdivisions (  505)
    axis.SetTitleFont  (   42)
    axis.SetTitleOffset(  1.5)
    axis.SetTitleSize  (0.050)
    if (coordinate == "y"):
        axis.SetTitleOffset(1.6)
    axis.SetTitle(title)    

def draw_legend(x1,y1,hist,label,options):

    legend = ROOT.TLegend(x1+xoffsetstart,y1+yoffsetstart,x1+xoffsetstart + xoffset,y1+yoffsetstart + yoffset)

    legend.SetBorderSize(     0)
    legend.SetFillColor (     0)
    legend.SetTextAlign (    12)
    legend.SetTextFont  (    42)
    legend.SetTextSize  ( 0.040)

    legend.AddEntry(hist,label,options)

    legend.Draw("same")

    #otherwise the legend goes out of scope and is deleted once the function finishes
    hist.label = legend


f_double_muon = ROOT.TFile("/afs/cern.ch/work/a/amlevin/data/ewkzgjj/2017/double_muon.root")
f_double_eg = ROOT.TFile("/afs/cern.ch/work/a/amlevin/data/ewkzgjj/2017/double_eg.root")
f_zgjets = ROOT.TFile("/afs/cern.ch/work/a/amlevin/data/ewkzgjj/2017/zgjets.root")


t_double_muon = f_double_muon.Get("Events")
t_double_eg = f_double_eg.Get("Events")
t_zgjets = f_zgjets.Get("Events")

h_data_mjj = ROOT.TH1F("data mjj","",5,150,400)
h_data_mll = ROOT.TH1F("data mjj","",8,70,110)

h_data_mjj.Sumw2()
h_data_mll.Sumw2()

h_zgjets_mjj = ROOT.TH1F("zgjets mjj","",5,150,400)
h_zgjets_mll = ROOT.TH1F("zgjets mll","",8,70,110)

h_zgjets_mjj.Sumw2()
h_zgjets_mll.Sumw2()

h_fake_photon_mjj = ROOT.TH1F("fake photon mjj","",5,150,400)
h_fake_photon_mll = ROOT.TH1F("fake photon mjj","",8,70,110)

h_fake_photon_mjj.Sumw2()
h_fake_photon_mll.Sumw2()

h_sum_mjj = ROOT.TH1F("sum","sum",5,150,400)
h_sum_mll = ROOT.TH1F("sum","sum",8,70,110)

h_sum_mjj.Sumw2()
h_sum_mll.Sumw2()

f_good_run_lumis=open("/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt")

good_run_lumis=json.loads(f_good_run_lumis.read())

zgjets_nweightedevents = f_zgjets.Get("nEventsGenWeighted").GetBinContent(1)

def pass_json(run,lumi):

    if str(run) not in good_run_lumis.keys():
        return False

    for lumi_pair in good_run_lumis[str(run)]:
        if lumi < lumi_pair[1] and lumi > lumi_pair[0]:
            return True

    return False    

for i in range(0,t_double_muon.GetEntries()):

    t_double_muon.GetEntry(i)

    if not pass_json(t_double_muon.run,t_double_muon.lumi):
        continue

    if t_double_muon.lepton_pdg_id != 13:
        continue

    if t_double_muon.photon_pt < 25:
        continue

    if t_double_muon.mjj > 400:
        continue

    if not (abs(t_double_muon.photon_eta) < 1.4442):
        continue

    if t_double_muon.photon_selection == 2:
        h_data_mll.Fill(t_double_muon.mll)
    elif t_double_muon.photon_selection == 0 or t_double_muon.photon_selection == 1:    
#        print str(t_double_muon.run) + " " + str(t_double_muon.lumi) + " " + str(t_double_muon.event)
        h_fake_photon_mll.Fill(t_double_muon.mll,fake_photon_event_weight(t_double_muon.photon_eta, t_double_muon.photon_pt,t_double_muon.lepton_pdg_id ))
    else:
        assert(0)

for i in range(0,t_zgjets.GetEntries()):

    t_zgjets.GetEntry(i)

    if t_zgjets.photon_pt < 25:
        continue

    if t_zgjets.mjj > 400:
        continue

    if not (abs(t_zgjets.photon_eta) < 1.4442):
        continue

    if t_zgjets.lepton_pdg_id != 13:
        continue

    if t_zgjets.photon_selection != 2:
        continue

#    print str(t_zgjets.run) + " " + str(t_zgjets.lumi) + " " + str(t_zgjets.event)

    if t_zgjets.gen_weight > 0:
        h_zgjets_mll.Fill(t_zgjets.mll,55.39*1000*41.37/zgjets_nweightedevents)

    else:    
        h_zgjets_mll.Fill(t_zgjets.mll,-55.39*1000*41.37/zgjets_nweightedevents)

c = ROOT.TCanvas()

h_zgjets_mll.SetLineColor(ROOT.kAzure-1)
h_fake_photon_mll.SetLineColor(ROOT.kMagenta)

h_zgjets_mll.SetFillColor(ROOT.kAzure-1)
h_fake_photon_mll.SetFillColor(ROOT.kMagenta)

h_zgjets_mll.SetFillStyle(1001)
h_fake_photon_mll.SetFillStyle(1001)

h_sum_mll.Add(h_zgjets_mll)
h_sum_mll.Add(h_fake_photon_mll)

h_stack = ROOT.THStack()

h_stack.Add(h_zgjets_mll)
h_stack.Add(h_fake_photon_mll)

h_data_mll.SetMinimum(0)
h_data_mll.SetMarkerStyle(ROOT.kFullCircle)
h_data_mll.SetLineWidth(3)
h_data_mll.SetLineColor(ROOT.kBlack)

set_axis_fonts(h_data_mll,"x","m_{ll} (GeV)")
set_axis_fonts(h_data_mll,"y","Events / bin")

h_data_mll.Draw()

h_stack.Draw("hist same")

h_data_mll.Draw("same")

j=0
draw_legend(xpositions[j],0.84 - ypositions[j]*yoffset,h_data_mll,"data","lp")
j=j+1
draw_legend(xpositions[j],0.84 - ypositions[j]*yoffset,h_fake_photon_mll,"fake photon","f")
j=j+1
draw_legend(xpositions[j],0.84 - ypositions[j]*yoffset,h_zgjets_mll,"zg+jets","f")

s="41.37 fb^{-1} (13 TeV)"
lumilabel = ROOT.TLatex (0.95, 0.93, s)
lumilabel.SetNDC ()
lumilabel.SetTextAlign (30)
lumilabel.SetTextFont (42)
lumilabel.SetTextSize (0.040)

cmslabel = ROOT.TLatex (0.18, 0.93, "")
cmslabel.SetNDC ()
cmslabel.SetTextAlign (10)
cmslabel.SetTextFont (42)
cmslabel.SetTextSize (0.040)

cmslabel.Draw ("same") 
lumilabel.Draw("same")

c.Update()
c.ForceUpdate()
c.Modified()

c.SaveAs("/eos/user/a/amlevin/www/tmp/delete_this.png")
