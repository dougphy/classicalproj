import ROOT
from ROOT import gStyle

def gstyle():
    ROOT.gROOT.ProcessLine('TGaxis::SetMaxDigits(2);')    
    gStyle.SetFrameBorderMode(0)
    gStyle.SetFrameFillColor(0)
    gStyle.SetCanvasBorderMode(0)
    gStyle.SetCanvasColor(0)
    gStyle.SetPadBorderMode(0)
    gStyle.SetPadColor(0)
    gStyle.SetStatColor(0)
    gStyle.SetTitleFont(42,'')
    gStyle.SetLabelFont(42,'x')
    gStyle.SetTitleFont(42,'x')
    gStyle.SetLabelFont(42,'y')
    gStyle.SetTitleFont(42,'y')
    gStyle.SetLabelFont(42,'z')
    gStyle.SetTitleFont(42,'z')
    gStyle.SetLabelSize(0.042,'x')
    gStyle.SetTitleSize(0.048,'x')
    gStyle.SetLabelSize(0.042,'y')
    gStyle.SetTitleSize(0.048,'y')
    gStyle.SetLabelSize(0.042,'z')
    gStyle.SetTitleSize(0.048,'z')
    gStyle.SetTitleSize(0.048,'')
    gStyle.SetTitleAlign(23)
    gStyle.SetTitleX(0.5)
    gStyle.SetTitleBorderSize(0)
    gStyle.SetTitleFillColor(0)
    gStyle.SetTitleStyle(0)
    gStyle.SetOptStat(0)
    gStyle.SetStatBorderSize(0)
    gStyle.SetStatFont(42)
    gStyle.SetStatFontSize(0.042)
    gStyle.SetStatY(0.9)
    gStyle.SetStatX(0.86)
    gStyle.SetLegendBorderSize(0)
    gStyle.SetLegendFillColor(0)
    gStyle.SetFuncWidth(2)
    gStyle.SetFuncColor(2)
    gStyle.SetPadTopMargin(0.08)
    gStyle.SetPadBottomMargin(0.12)
    gStyle.SetPadLeftMargin(0.12)
    gStyle.SetPadRightMargin(0.08)  
    gStyle.SetCanvasDefX(400)
    gStyle.SetCanvasDefY(20)
    gStyle.SetCanvasDefH(420)
    gStyle.SetCanvasDefW(510)
    gStyle.SetFrameBorderMode(0)
    gStyle.SetFrameLineWidth(2)
    gStyle.SetHistLineWidth(2)
    gStyle.SetTitleOffset(1.16,'y')
    gStyle.SetTitleOffset(1.20,'x')
