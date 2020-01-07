def addBorder(picture):
    for i in range(len(picture)):
        picture[i] = "*"+picture[i]+"*"
    picture.insert(0, len(picture[0])*'*')
    picture.append(len(picture[0])*'*')
    return picture