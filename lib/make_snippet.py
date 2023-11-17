

def make_snippet(string1):
    list1 = string1.split()
    text = ""
    if len(list1) < 5:
        text = string1
    else:
        for y in range(5):
            if y == 4:
                text = text + str(list1[y]) + "..."
            else:
                text = text + str(list1[y]) + " "
    return text
