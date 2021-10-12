def fibonacci(x):
    """
fibonaci series = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
what value of 5 in fibonaci series mean the value for postion 5 in series
input =3
output =1
    """
    if x==1:
        return 1
    elif x==0:
        return 0
    else:
        return(fibonacci(x-1)+fibonacci(x-2))

def lucas(x):
    """
licas series = 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 …………..
what value of 5 in licas series mean the value for postion 5 in series
input =5
output =11
    """
    if x==0:
        return 2
    elif x==1:
        return 1
    else:
        return (lucas(x-1)+lucas(x-2))


def mySeries(x,val1,val2):
    
    if x==0:
        return val1
    elif x==1:
        return val2
    else:
        return (mySeries(x-1,val1,val2)+mySeries(x-2,val1,val2))
"""
mySeries accept3 parameters 2 of them optional and give them(0,1) if they didnt enter
if val1==0 and val2==1 go to fibonacci(x)
if val1==2 and val2==1 go to return lucas(x)
else calculate the sumation for input value
 input=(5,5,5)
 output= 40

    """
def sum_series(x,val1=0,val2=1):
    if val1==0 and val2==1:
        return fibonacci(x)
    elif val1==2 and val2==1:
        return lucas(x)
    else:
        return mySeries(x,val1,val2)





    