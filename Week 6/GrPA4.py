'''
Question's too long
'''

def two_level_sort(scores):
    d = {}
    for score in scores:
        if score[1] not in d:
            d[score[1]] = []
        d[score[1]].append(score[0])
    
    score_list = list(d.keys())
    for i in range(len(score_list)-1):
        for j in range(0, len(score_list)-i-1):
            if score_list[j] > score_list[j+1]:
                score_list[j], score_list[j+1] = score_list[j+1], score_list[j]
    
    for key in d:
        values = d[key]
        for i in range(len(values)-1):
            for j in range(0, len(values)-i-1):
                if values[j] > values[j+1]:
                    values[j], values[j+1] = values[j+1], values[j]
        d[key] = values
    
    final = []
    for key in score_list:
        for value in d[key]:
            final.append((value, key))
    
    return final
