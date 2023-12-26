def k_anonymity_score(k_anon_res):
    k = k_anon_res
    if  k < 3:
        score = 0
    elif k == 3:
        score = 60
    elif k == 4: 
        score = 70
    elif (5 <= k <= 10): 
        score = 80
    elif (10 <= k <= 15):
        score = 90
    else: 
        score = 100
    
    return score


def anon_ss_score(anon_ss_res):
    anon_ss_res = min(anon_ss_res,1000)
    score = (anon_ss_res / 1000) * 100
    return score

def combined_score(k_anon_score, anon_ss_score):
    score = (0.8 * k_anon_score) + (0.2 * anon_ss_score)
    return score