import random 

def estimate_wallis(iters):
    acc = 1.0
    for n in range(1, iters+1):
        acc = acc* (4*(n**2))/(4*(n**2)-1)
    estimate = 2 * acc
    return estimate


def estimate_monte(iters):
    inside = 0.0
    for _ in range(iters):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) <=1:
            inside += 1
    estimate = str(4*inside/iters)
    return estimate