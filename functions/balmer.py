## Balmer Series for hydrogen and deuterium

from math import pi

def HDBalmer(n_i, n_f):

	k=8.99e9
	e=1.60e-19
	m_e=9.11e-31
	m_p=1.6726219e-27
	h=6.63e-34
	c=299792485
	M = 2*m_p #Proton + Neutron
	mu = (m_e*M)/(m_e+M) #Reduced Mass
	
	Ryd=1.097373e7 #[1/m]
	
	#n2=2
	#n3=3
	#n4=4
	#n5=5
	#n6=6
	#n7=7
	#n8=8

	Hwave= (Ryd*((1.0/n_f**2)-(1.0/n_i**2)))**(-1)
	Dwave= ((mu/m_e)*Ryd*((1.0/n_f**2)-(1.0/n_i**2)))**(-1)
	return Hwave, Dwave, Hwave - Dwave