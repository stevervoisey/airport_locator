import re


class InvalidCoordinate(Exception):
    """Raise exception when coordinates (latitude,longitude) contain invalid values."""
    pass


class InvalidFileHeadingError(Exception):
    """Raise exception when data file has invalid headings."""
    pass


class InvalidFileDataError(Exception):
    """Raise exception when file data contains invalid data types."""
    pass


def validate_file_headings(headings: str) -> bool:
    """
    Verify "headings" comma separated str matches the expected headings for airport location data.
    Expected value "NAME,ICAO,Latitude,Longitude"

    Parameters
    ----------
    headings : str
        comma separated string.

    Raises
    ------
    InvalidFileHeadingError

    Returns
    -------
    True
    """

    if not re.search('^NAME,ICAO,Latitude,Longitude$', headings):
        raise InvalidFileHeadingError(F"INVALID HEADINGS: {headings}")
    return True


def validate_file_data(data: list) -> bool:
    """
    Verify each comma separated data row matches the expected format for airport location data.
    Expected format "string,string,float,float"

    Parameters
    ----------
    data : list[str]

    Raises
    -----
    InvalidFileDataError

    Returns
    -------
    True
    """
    for line in data:
        if not re.search(r'^[\w\s]+,\w+,[+-]?\d+(\.\d*)?,[+-]?\d+(\.\d*)?$', line):
            raise InvalidFileDataError(F"INVALID FILE DATA: {line}")
    return True


def read_data_from_file(file: str) -> list:
    """
    Open file, verify the contents, strip off headings and return data as a list.

    Parameters
    ----------
    file : str
        Filename of a csv data file. If file is not in the current directory filename should include
        the path.

    Returns
    -------
    list[str]

    """
    with open(file) as data_file:
        contents = [row.rstrip() for row in data_file]
        validate_file_headings(contents[0])
        validate_file_data(contents[1:])
        return contents[1:]


def validate_coordinates(coordinates: tuple) -> list:
    """
    Verify a pair of numbers are valid (latitude,longitude) coordinates.
        latitude  >=  -90 and <=  90
        longitude >= -180 and <= 180
    Return a list of all issues found.
    An empty list indicates success.

    Parameters
    ----------
    coordinates : tuple(float, float)

    Returns
    -------
    list[str]
    """
    if float(coordinates[0]) < -90:
        return[coordinates, "latitude less than -90"]
    if float(coordinates[0]) > 90:
        return[coordinates, "latitude greater than 90"]
    if float(coordinates[1]) < -180:
        return[coordinates, "longitude less than -180"]
    if float(coordinates[1]) > 180:
        return[coordinates, "longitude greater than 180"]
