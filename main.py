import cv2
import numpy as np
from matplotlib import pyplot as plt

import pallier

ekey, dkey = pallier.generate_key(7)

def new_encrypt(num):
	global ekey
	return int(pallier.encrypt(num, ekey))

def new_decrypt(num):
	global ekey
	global dkey
	return int(pallier.decrypt(num, dkey, ekey))

fname = "hat.png"

img = cv2.imread(fname)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = img.shape

print "Loaded %s in grayscale, encrypting image.." % fname

img_enc = np.zeros(shape=img.shape, dtype=np.uint64)

for row in range(height):
	for pixel in range(width):
		img_enc[row][pixel] = np.uint64(pallier.encrypt(img[row][pixel], ekey))

print "%s encrypted, Decrypting image.." % fname

img_dec = np.zeros(shape=img.shape, dtype=np.uint8)
for row in range(height):
	for pixel in range(width): 
		img_dec[row][pixel] = np.uint8(pallier.decrypt(img_enc[row][pixel], dkey, ekey))

print "Image decrypted"
cv2.imwrite("dec_"+fname, img_dec)

def show_and_wait(title, frame):
	cv2.imshow(title, frame)

	while True:
		if cv2.waitKey(1) == ord('q'):
			cv2.destroyAllWindows()
			break

def show_hist(frame):
	plt.hist(frame.ravel(), 256)
	plt.show()

def show_lenna():
	show_and_wait("Original", img)

def show_lenna_hist():
	show_hist(img)

def show_decrypted():
	show_and_wait("Decrypted Image", img_dec)

def show_decrypted_hist():
	show_hist(img_dec)

def show_encrypted_hist():
	show_hist(img_enc)

if __name__ == '__main__':
	show_hist(img)
	show_hist(img_enc)
	show_decrypted()