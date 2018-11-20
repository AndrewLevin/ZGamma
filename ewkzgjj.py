import ROOT

from array import array

f = ROOT.TFile("/afs/cern.ch/work/a/amlevin/data/ewkzgjj/ewkzgjj.root")

t = f.Get("Events")

binningmjj=array('f',[500,800,1200,1600])
binningdetajj=array('f',[2.5,4.5,6,7.5])

h = ROOT.TH2F("h","h",len(binningdetajj)-1, binningdetajj,len(binningmjj)-1, binningmjj )

xs = 0.1084 

n_weighted_events_run_over = f.Get("nWeightedEvents").GetBinContent(1)

for i in range(0,t.GetEntries()):

    detajj = t.detajj
    mjj = t.mjj

    if detajj > h.GetXaxis().GetBinLowEdge(h.GetNbinsX()):
        detajj = h.GetXaxis().GetBinCenter(h.GetNbinsX())

    if mjj > h.GetYaxis().GetBinLowEdge(h.GetNbinsY()):  
        mjj = h.GetYaxis().GetBinCenter(h.GetNbinsY())  

    w = xs * 1000 * 35.9 / n_weighted_events_run_over     

    h.Fill(detajj,mjj)

h.Print("all")
