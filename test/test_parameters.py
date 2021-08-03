import argparse
import pytest
from parameters import Parameters
from .constants_for_testing import TEST_DATA_GOOD


def test_parameters_good():
    """
    Verify that the Parameters object contains attributes to match command line input parameters.
    Verify that position is converted from a string into a tuple(float, float)
    Returns
    -------
    None
    """
    test_args = argparse.Namespace()
    test_args.item = "doc"
    test_args.item = "file"
    test_args.item = "position"
    test_args.item = "gui"

    test_args.file = TEST_DATA_GOOD
    test_args.position = "51.26950,-1.03896"
    test_args.gui = True
    test_args.doc = False

    test_position = (51.2695, -1.03896)
    parameters = Parameters(test_args)
    assert parameters.csv_file == TEST_DATA_GOOD
    assert parameters.gui
    assert parameters.position == test_position


def test_parameters_value_error():
    """
    Verify that if position can not be converted to two floats, a ValueError exception is raised.

    Returns
    -------
    None
    """
    test_args = argparse.Namespace()
    test_args.item = "doc"
    test_args.item = "file"
    test_args.item = "position"
    test_args.item = "gui"

    test_args.file = TEST_DATA_GOOD
    test_args.gui = True
    test_args.doc = False
    test_args.position = "51.abc,-1.abc"

    with pytest.raises(ValueError):
        parameters = Parameters(test_args)
