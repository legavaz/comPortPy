

def removeFix(mString=""):
    goodLetter = '0123456789'
    result = ''
    for let in mString:
        for blet in goodLetter:
            if let == blet:
                result += let

    return result

