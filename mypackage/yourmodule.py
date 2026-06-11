def rank(scores):
    avg = []
    for s in scores:
        avg.append(sum(s)/len(s))           # [75, 70, 55, 65]
    #avg = [sum(s)/len(s) for s in scores]
    sorted_avg = sorted(avg,reverse = True) # [75 ,70, 65, 55]

    result = []
    for i in avg :
        result.append(sorted_avg.index(i) +1)
    #result = [avg_sort.index(i)+1 for i in avg]
    return result

def is_prime(num_list):
    result = []
    for num in num_list:
        isprime = True
        for i in range(2,num):
            if num % i == 0:
                isprime = False
                break
        result.append(isprime)

    return result
