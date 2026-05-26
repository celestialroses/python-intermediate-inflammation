"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean
from inflammation.models import daily_mean, daily_max, daily_min

import pytest


#################################################################
@pytest.mark.parametrize(

        '''test_input, test_result''',
        # pass array with the values
        # definition of the parameters
        [
            ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),   #expected inputs and results?
            ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
            # (np.zeros(3,5)),np.zeros(5)) # does the same as line with all zeros (5 zeros in data structure with 3 times 5)
        ]
)
        

def test_daily_mean(test_input, test_result):
    '''Test that mean function works for both zeros and integers'''
    npt.assert_array_equal(daily_mean(test_input), test_result) # this so far is just to run it



def test_daily_mean_string():
    '''Test for TypeError when parsing strings'''
    with pytest.raises(TypeError):
        error_expected = daily_mean(['Hi', 'there'])
        

##############################################################

def test_daily_max_string():
    ''' Test for TypeError when parsing strings '''
    with pytest.raises(TypeError):
        error_expected = daily_max(['Hello', 'there' ])   


def test_daily_max_integers():
    """Test that the max function works for an array of positive and negative integers.
    """
    # # test_input = np.array([[1, 2, -9], [-3, 4, -2], [-1, 5, -6]])
    # # test_result = np.array([1, 5, -2])  
    # #  
    # # test_input = np.array([[1, 2, -8],
    # #                        [3, 4, -1],
    # #                        [5, 6, -2]])
    
    # # test_result = np.array([5, 6, -3])

    # test_input = np.array([[1, 2, -9], [-3, 4, -2], [-1, 5, -6]])
    # test_result = np.array([5, 6, -3], [-3, 4, -2], [-1, 5, -6]])              # update test_output accordingly

    # npt.assert_array_equal(daily_max(test_input), test_result)

    test_input = np.array([
        [1, 2, -9],
        [-3, 4, -2],
        [-1, 5, -6]
    ])

    test_result = np.array([1, 5, -2])

    npt.assert_array_equal(daily_max(test_input), test_result)

