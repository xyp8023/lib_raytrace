
import cppimport.import_hook
import cppimport
import math
import numpy as np

ssp = cppimport.imp("ssp")
SSP = ssp.ssp([0.0,1.0,2.0], [1500.0, 1450.0, 1420.0])
print(SSP.raytrace(float(0.0), float(0.0), float((math.pi/180)*5), float(1.0)))


sparse_ssp = cppimport.imp("sparse_ssp")
S_SSP = sparse_ssp.sparsed_ssp([0.0,1.0,2.0], [1500.0, 1450.0, 1420.0])
print(S_SSP.raytrace(float(0.0), float(0.0), float((math.pi/180)*5), float(1.0), 0.001))


regular_ssp = cppimport.imp("regular_ssp")
R_SSP = regular_ssp.regular_ssp([0.0,1.0,2.0], [1500.0, 1450.0, 1420.0])
print(R_SSP.raytrace(float(0.0), float(0.0), float((math.pi/180)*5), float(1.0)))


data_ssp = cppimport.imp("data_ssp")
D_SSP = data_ssp.data_ssp([0.0,1.0,2.0], [1500.0, 1450.0, 1420.0])
print(D_SSP.raytrace(float(0.0), float(0.0), float((math.pi/180)*5), float(1.0)))
