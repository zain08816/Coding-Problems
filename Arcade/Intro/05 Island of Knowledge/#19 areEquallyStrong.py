def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):

    you = [yourLeft, yourRight]
    friend = [friendsLeft, friendsRight]

    if sorted(you) == sorted(friend):
        return True
    else:
        return False