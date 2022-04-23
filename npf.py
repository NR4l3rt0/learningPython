import numpy_financial as npf

print(npf.pv(rate=0.07, nper=15, pmt=0, fv=150000))

print(npf.pmt(rate=0.03, nper=30, pv=0, fv=100000))
