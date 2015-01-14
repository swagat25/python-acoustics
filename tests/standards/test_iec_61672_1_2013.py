import numpy as np

from acoustics.standards.iec_61672_1_2013 import *

def test_fast_level():
    """Test whether integration with time-constant FAST gives the correct level.
    
    Note that the reference sound pressure is used.
    
    In this test the amplitude of the sine is 1, which means the mean squared $MS$ is 0.5
    With a reference pressure $p_r$ of 2.0e-5 the level should be 91 decibel
    
    .. math:: L = 10 \cdot \\log_{10}{\\left(\\frac{MS}{p_r^2} \\right)}
    
    .. math:: L = 10 \cdot \\log_{10}{\\left(\\frac{0.5}{(2e-5)^2} \\right)} = 91
    
    """
    
    fs = 4000.0
    f = 400.0
    duration = 3.0
    samples = int(duration*fs)
    t = np.arange(samples) / fs
    
    x = np.sin(2.0*np.pi*f*t)
    times, levels = fast_level(x, fs)
    assert( abs(levels.mean() - 91 ) < 0.05 ) 
    
    
    x *= 4.0
    times, levels = fast_level(x, fs)
    assert( abs(levels.mean() - 103 ) < 0.05 ) 
    
    
def test_slow_level():
    """Test whether integration with time-constant SLOW gives the correct level.
    """
    
    fs = 4000.0
    f = 400.0
    duration = 3.0
    samples = int(duration*fs)
    t = np.arange(samples) / fs
    
    x = np.sin(2.0*np.pi*f*t)
    times, levels = fast_level(x, fs)
    assert( abs(levels.mean() - 91 ) < 0.05 ) 
    
    
    x *= 4.0
    times, levels = fast_level(x, fs)
    assert( abs(levels.mean() - 103 ) < 0.05 ) 
    
        
    