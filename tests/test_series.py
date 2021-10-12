from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


def test_version():
    assert __version__ == '0.1.0'
#1
def test_fibonacci1():
    # input
    v=0
    #output
    fibonResult=0
    assert fibonacci(v)==fibonResult
#2
def test_fibonacci2():
    # input
    v=2
    #output
    assert fibonacci(v)==1
#3
def test_fibonacci3():
    # input
    v=3
    #output
    fibonResult=2
    assert fibonacci(v)==fibonResult
#4
def test_lucas1():
    # input
    v=3
    #output
    lucasResult=4
    assert lucas(v)==lucasResult
#5
def test_lucas2():
    # input
    v=5
    #output
    lucasResult=11
    assert lucas(v)==lucasResult
#6
def test_lucas3():
    # input
    v=0
    #outputu
    lucasResult=2
    assert lucas(v)==lucasResult
#7
def test_sum_series():
    assert sum_series(3, 4, 2) == 8
#8
def test_sum_series2():
    assert sum_series(5,5,5) == 40