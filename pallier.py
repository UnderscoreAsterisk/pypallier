import gmpy2
from Crypto.Util import number
from time import time

def L(x, n):
	return gmpy2.t_div(x-1, n)

def generate_key(n_len):
	p=gmpy2.mpz(number.getPrime(n_len))
	q=gmpy2.mpz(number.getPrime(n_len))
	n=p*q
	phin=(p-1)*(q-1)
	lam=phin
	g=n+1
	m=number.inverse(phin,n)

	return (n,g),(lam,m)

def encrypt(m, key):
	(n, g) = key

	t = int(time())
	rand_state = gmpy2.random_state(t)
	r = gmpy2.mpz_random(rand_state, n-1)+1
	
	c = gmpy2.t_mod(g**m * r**n, n**2)
	return c

def decrypt(c, dkey, ekey):
	lam, mu = dkey
	n, g = ekey
	x = gmpy2.t_mod(c**lam, n**2)
	return gmpy2.t_mod(L(x, n)*mu, n)

if __name__ == '__main__':
	message = 103
	print "Encrypting message: %d" % message
	ekey, dkey = generate_key(10)

	e = encrypt(message, ekey)
	dmsg = decrypt(e, dkey, ekey)
	if message == dmsg:
		print "I do believe its working.. good"
	else:
		print "ERR: decrypted msg: %d" % dmsg