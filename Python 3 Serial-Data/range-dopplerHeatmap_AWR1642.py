import numpy as np
filename = 'test.dat'
indata = np.loadtxt(filename, usecols=(0,1)) # make sure the rest is ignored
tlines_bool = indata[:,0]==-9999
Nparticles = np.diff(np.where(tlines_bool)[0][:2])[0] - 1
# TODO: error handling: diff(np.where(tlines_bool)) should be constant
times = indata[tlines_bool,1]
positions = indata[np.logical_not(tlines_bool),:].reshape(-1,Nparticles,2)
