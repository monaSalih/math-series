def fibonacci(x):
    if x==1:
        return 1
    elif x==0:
        return 0
    else:
        return(fibonacci(x-1)+fibonacci(x-2))

def lucas(x):
    if x==0:
        return 2
    elif x==1:
        return 1
    else:
        return (lucas(x-1)+lucas(x-2))

def sum_series(x,val1,val2):
    if x==0:
        return val1
    if x==1:
        return val2
    return (sum_series(x-1)+sum_series(x-2))



    