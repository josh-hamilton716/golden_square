
def check_sentence(text):
    if text == "":
        return True
    
    if (text[0] == text[0].upper()) and (text[-1] in [".","!","?"]):
        return True
    return False

