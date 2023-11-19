import numpy as np
from same_project.utils.same_util import add

def test_add():
    x: np.ndarray = np.array([1, 2, 3])
    y: np.ndarray = np.array([5, 9, 10])

    np.testing.assert_allclose(add(x, y), x + y)