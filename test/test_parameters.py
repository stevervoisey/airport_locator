import argparse
import pdb

import pytest
from parameters import Parameters
from exceptions import MissingRequiredParameters, InvalidDataFileInputParameter
from .constants_for_testing import TEST_DATA_GOOD


@pytest.fixture()
def generate_args():
    """
    A fixture to generate a standard set of input arguments as an argparse.Namespace().
    Individual tests can then modify individual arguments as required.

    Returns
    -------
    test_args - argparse.Namespace() as returned by argparse
    """
    test_args = argparse.Namespace()
    test_args.item = "doc"
    test_args.item = "file"
    test_args.item = "position"
    test_args.item = "gui"
    test_args.item = "gui_simple"

    test_args.file = TEST_DATA_GOOD
    test_args.position = "51.26950,-1.03896"
    test_args.gui = True
    test_args.gui_simple = True
    test_args.doc = False

    return test_args


def test_parameters_good(generate_args):
    """
    Verify that the Parameters object contains attributes to match command line input parameters.
    Verify that position is converted from a string into a tuple(float, float)
    Returns
    -------
    None
    """

    test_args = generate_args
    test_position = (51.2695, -1.03896)
    parameters = Parameters(test_args)
    assert parameters.csv_file == TEST_DATA_GOOD
    assert parameters.gui
    assert parameters.gui_simple
    assert parameters.position == test_position


def test_parameters_value_error(generate_args):
    """
    Verify that if position can not be converted to two floats, a ValueError exception is raised.

    Returns
    -------
    None
    """
    test_args = generate_args
    test_args.position = "51.abc,-1.abc"

    with pytest.raises(ValueError):
        parameters = Parameters(test_args)


def test_parameters_missing_data_file(generate_args):
    """
    Verify that if the --file is None, a MissingRequiredParameters exception is raised.

    Returns
    -------
    None
    """
    test_args = generate_args
    test_args.file = None

    with pytest.raises(MissingRequiredParameters):
        parameters = Parameters(test_args)


def test_parameters_invalid_data_file(generate_args):
    """
    Verify that if --file contains an invalid file path, an InvalidDataFileInputParameter exception is raised.

    Returns
    -------
    None
    """
    test_args = generate_args
    test_args.file = "I_DO_NOT_EXIST.DATA"

    with pytest.raises(InvalidDataFileInputParameter):
        parameters = Parameters(test_args)
