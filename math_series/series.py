def fibonacci(x):
    if x==1:
        return 1
    if x==0:
        return 0
    else:
        return(fibonacci(x-1)+fibonacci(x+2))
        