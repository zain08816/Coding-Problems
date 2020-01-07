def digitsProduct(product):
    if product == 0:
        return 10
    if product < 10:
        return product

    start = 11
    
    for i in range(2, product//2):
        if (product%i) == 0:
            
            for _ in range(200):
                p = 1
                for i in str(start):
                    p = p*int(i)
                    if p == product:
                        return start
                start += 1
    return -1
    

        
        
