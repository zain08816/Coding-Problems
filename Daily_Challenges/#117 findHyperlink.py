def findHyperlink(text):
    url = []
    
    p = text.find('<a href=') + 8
    text = text[p:]

    for i in range(1, len(text)):
        if text[i] == ">":
            break
        url.append(text[i])
    url.pop()
    
    return ''.join(url)