from math_series import __version__
from math_series.series import fibonacci


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci1():
    # input
    v=0
    #output
    fibonResult=1
    assert fibonacci(v)==fibonResult

def test_fibonacci2():
    # input
    v=5
    #output
    fibonResult=8
    assert fibonacci(v)==fibonResult