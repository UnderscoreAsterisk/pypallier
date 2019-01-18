from PIL import Image

def extract(fname, function):
    data = Image.open(fname).getdata()
    return function(data)

if __name__ == '__main__':
    import functions
    print(extract("../Lenna.png", functions.addition))
    print(extract("../Lenna.png", functions.green))
    print(extract("../Lenna.png", functions.fibonacci))
    print(extract("../Lenna.png", functions.multiplication))
    print(extract("../Lenna.png", functions.alternate))