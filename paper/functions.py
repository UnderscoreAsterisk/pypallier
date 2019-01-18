def addition(data):
    offsets = [416, 387, 385, 379, 373, 427, 457, 398, 383, 366, 381, 380, 428]
    i = 0
    msg = ""
    for o in offsets:
        msg += chr(sum(data[i])-o)
        i += 1
    return msg

def green(data):
	offsets =[126,121,137,137,327,5624,2912,327,257,137,127]
	msg=''
	for i in offsets:
		msg+=chr(data[i][1])
	return msg
def alternate(data):
	offsets=[(6651,0),(121,1),(12,2),(4094,0),(327,1),(20,2),(3583,0),(5624,1),(5,2),(13820,0),(5624,1),(5,2),(7671,0),(121,1),(5624,1),(22,2),(5113,0),(329,1),(42,2),(5624,0),(121,1)]
	msg=''
	for i in offsets:
		msg+=chr(data[i[0]][i[1]])
	return msg