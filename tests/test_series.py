from math_series import __version__
from math_series.series import fibonacci


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci():
    # input
    v=5
    #output
    fibonResult=8
    assert fibonacci(v)==fibonResult