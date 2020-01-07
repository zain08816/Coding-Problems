def newRoadSystem(roadRegister):
    my_list = roadRegister
    
    row_totals = [ sum(x) for x in my_list ]
    col_totals = [ sum(x) for x in zip(*my_list) ]
    
    if row_totals == col_totals:
        return True
    return False