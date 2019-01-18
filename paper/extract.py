from PIL import Image
import functions

def extract(fname, function):
    data = Image.open(fname).getdata()
    return function(data)

m = extract("../Lenna.png", functions.addition)
print(m)