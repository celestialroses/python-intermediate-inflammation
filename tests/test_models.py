"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

from inflammation.models import daily_mean, daily_max

def test_daily_max_integers():
    """Test that the max function works for an array of positive integers.
    """

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    
    test_result = np.array([5, 6])
    npt.assert_array_equal(daily_max(test_input), test_result)