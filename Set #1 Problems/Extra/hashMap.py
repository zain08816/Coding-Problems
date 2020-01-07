def hashMap(queryType, query):
        res = 0
        h = []
        for i, q in enumerate(queryType):

                if q == 'insert':
                        h.append(query[i])
                        
                if q == 'get':
                        for item in h:
                                if item[0] == query[i][0]:
                                        res += item[1]
                                
                if q == 'addToKey':
                        for item in h:
                                item[0] += query[i][0]
        
                
                if q == 'addToValue':
                        for item in h:
                                item[1] += query[i][0]
        return res