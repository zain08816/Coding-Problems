def properOrImproper(a):
    if abs(a[0]/a[1]) >= 1:
        return 'Improper'
    
    else:
        return 'Proper'