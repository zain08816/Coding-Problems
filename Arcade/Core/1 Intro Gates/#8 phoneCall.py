def phoneCall(min1, min2_10, min11, s):
    time = 0
    
    if s >= min1:
        time += 1
        s -= min1
    while s >= min2_10 and time < 10:
        time += 1
        s -= min2_10
    while s >= min11 and time >= 10:
        time += 1
        s -= min11
    
    return time