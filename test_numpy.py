import numpy as np

def test_numpy():
  a = np.arange(15).reshape(3, 5)
  assert a.shape == (3,5)
