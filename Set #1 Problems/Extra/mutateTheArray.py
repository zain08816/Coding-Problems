def mutateTheArray(n, a):
        res = []
        if n == 1:
                return a
        for i in range(n):
                
                if i == 0:
                        res.append(0 + a[i] + a[i+1])
        
                elif i == n-1:
                        res.append(a[i-1] + a[i] + 0)
                
                else:
                        res.append(a[i-1] + a[i] + a[i+1])
                        
        return res