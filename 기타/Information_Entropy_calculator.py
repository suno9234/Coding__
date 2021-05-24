import math as m
def calc(ps):
    answer=0
    total_p=0
    for p in ps:
        total_p+=p
        answer+= p*m.log2(1/p)
    print(total_p,answer)

calc([0.3,0.25,0.1,0.15,0.08,0.05,0.05,0.02])


# input list to calc