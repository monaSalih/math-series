from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci1():
    # input
    v=0
    #output
    fibonResult=0
    assert fibonacci(v)==fibonResult

def test_fibonacci2():
    # input
    v=2
    #output
    assert fibonacci(v)==1

def test_fibonacci3():
    # input
    v=3
    #output
    fibonResult=2
    assert fibonacci(v)==fibonResult

def lucas_test1():
    # input
    v=3
    #output
    lucasResult=0
    assert lucas(v)==lucasResult

def lucas_test2():
    # input
    v=5
    #output
    lucasResult=11
    assert lucas(v)==lucasResult

def lucas_test3():
    # input
    v=0
    #outputu
    lucasResult=2
    assert lucas(v)==lucasResult

def test_sum_series():
    assert sum_series(3, 4, 2) == 8

def test_sum_series2():
    assert sum_series(5,5,5) == 40