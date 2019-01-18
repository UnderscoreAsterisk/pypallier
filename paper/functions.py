def addition(data):
    offsets = [416, 387, 385, 379, 373, 427, 457, 398, 383, 366, 381, 380, 428]
    i = 0
    msg = ""
    for o in offsets:
        msg += chr(sum(data[i])-o)
        i += 1
    return msg