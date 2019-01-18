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