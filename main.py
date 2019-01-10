import cv2
import numpy as np
from matplotlib import pyplot as plt

import pallier

fname = "Lenna.png"

img = cv2.imread(fname)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray Lenna", img)

print "Loaded %s in grayscale, encrypting image.." % fname

encrypt_vec = np.vectorize(pallier.encrypt)
img_enc = encrypt_vec(img)

print "%s encrypted, Decrypting image.." % fname
dec = None
decrypt_vec = np.vectorize(pallier.decrypt)
img_dec = decrypt_vec(img)

print "Image decrypted"

def show_and_wait(title, frame):
	cv2.imshow(title, frame)

	while True:
		if cv2.waitKey(1) == ord('q'):
			cv2.destroyAllWindows()
			break

def show_hist(frame):
	plt.hist(frame.ravel(), 256, [0, 256])
	plt.show()

def show_lenna():
	show_and_wait("Gray Lenna", img)

def show_lenna_hist():
	show_hist(img)

def show_encrypted():
	show_hist(img_enc)
	show_and_wait("Encrypted Lenna", img_enc)

def show_decrypted():
	show_hist(img_dec)
	show_and_wait("Decrypted Lenna", img_dec)

if __name__ == '__main__':
	show_encrypted()