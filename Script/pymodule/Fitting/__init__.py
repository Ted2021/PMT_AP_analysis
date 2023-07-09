import os
import ROOT as RT

from .Fitting import *

path = __file__.split("__init__.py")
RT.gROOT.LoadMacro(path[0] + "macro/Fitting.h")