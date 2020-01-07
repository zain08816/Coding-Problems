def electionsWinners(votes, k):  
    votes = sorted(votes)
    
    if not k:
        top_votes = votes.count(votes[-1])
        if top_votes >= 2:
            return 0
        else:
            return 1
    return sum(1 for v in votes if v+k > votes[-1])
        