import pytest
from .constants_for_testing import TEST_DATA_GOOD
from utilities import validate_coordinates, \
    validate_file_headings, validate_file_data, \
    InvalidFileHeadingError, InvalidFileDataError, read_data_from_file


def test_validate_file_headings():
    """
    Verify that validate_file_headings raises an 'InvalidFileHeadingError' exception for invalid headings

    Returns
    -------
    None
    """
    good_headings = "NAME,ICAO,Latitude,Longitude"
    # using typo's in heading names: NAMEE, Lattitude
    bad_headings = "NAMEE,ICAO,Lattitude,Longitude"

    assert validate_file_headings(good_headings)

    with pytest.raises(InvalidFileHeadingError):
        validate_file_headings(bad_headings)


def test_validate_file_data():
    """
    Verify that validate_file_data raises an 'InvalidFileDataError' exception for invalid data.

    Returns
    -------
    None
    """
    good_data = [
        "DUNDEE,EGPN,56.452499,-3.025833",
        "SWANSEA,EGFH,51.605333,-4.067833",
    ]
    # using invalid float value -3.02583a3
    bad_data1 = [
        "DUNDEE,EGPN,56.452499,-3.02583a3",
        "SWANSEA,EGFH,51.605333,-4.067833",
    ]
    # using invalid float value 51.60b5333
    bad_data2 = [
        "DUNDEE,EGPN,56.452499,-3.025833",
        "SWANSEA,EGFH,51.60b5333,-4.067833",
    ]
    # using missing airport code field
    bad_data3 = [
        "DUNDEE,EGPN,56.452499,-3.02583a3",
        "SWANSEA,51.605333,-4.067833",
    ]

    assert validate_file_data(good_data)

    with pytest.raises(InvalidFileDataError):
        validate_file_data(bad_data1)
    with pytest.raises(InvalidFileDataError):
        validate_file_data(bad_data2)
    with pytest.raises(InvalidFileDataError):
        validate_file_data(bad_data3)


def test_read_data_from_file():
    """
    Verify that read_data_from_file successfully reads data from a csv file.

    Returns
    -------
    None
    """
    test_data = [
        "HONINGTON,EGXH,52.342611,0.772939",
        "WELSHPOOL,EGCW,52.628611,-3.153333"]

    data = read_data_from_file(TEST_DATA_GOOD)

    assert data == test_data


def test_validate_coordinates():
    """
    Verify that validate_coordinates returns the correct message when passed invalid coordinates.
    valid values: -90 >= latitude <= 90 and -180 >= longitude <=180

    Returns
    -------

    """
    lat_less_than = (-91.00, 1.0)
    lat_more_than = (91.00, 1.0)
    lon_less_than = (1.00, -181.0)
    lon_more_than = (1.00, 181.0)

    assert validate_coordinates(lat_less_than) == [lat_less_than, "latitude less than -90"]
    assert validate_coordinates(lat_more_than) == [lat_more_than, "latitude greater than 90"]
    assert validate_coordinates(lon_less_than) == [lon_less_than, "longitude less than -180"]
    assert validate_coordinates(lon_more_than) == [lon_more_than, "longitude greater than 180"]

