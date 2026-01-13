#9

def padding(text, length):
    if len(text) % length != 0:
        text += "\x04" * (length - len(text) % length)
    return text
# print(padding("YELLOW SUBMARINE", 20))



#10