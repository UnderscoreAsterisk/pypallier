import gmpy2
from Crypto.Util import number
def generate_key(n_len):
	p=gmpy2.mpz(number.getPrime(n_len))
	q=gmpy2.mpz(number.getPrime(n_len))
	n=p*q
	phin=(p-1)*(q-1)
	lam=phin
	g=n+1
	m=number.inverse(phin,n)
	return (n,g),(lam,m)
	
	# lam=gmpy2.lcm(p-1,q-1)
	# select random integer g
	# m=number.inverse((L(pow(g,lam,n*n))),n)

	

def L(x):
	pass

def encrypt():
	pass

def decrypt():
	pass
