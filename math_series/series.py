def fibonacci(x):
    if x==1:
        return 1
    elif x==0:
        return 0
    else:
        return(fibonacci(x-1)+fibonacci(x-2))

def lucas(x):
    if(x==0):
        return 2
    else:
        return (lucas(x-1)+lucas(x-2))
