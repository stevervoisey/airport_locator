import sys
from messages import USAGE


class DisplayDocumentationAndExit(Exception):
    """Raise exception when --doc is passed on the command line.
       This is not an issue, but an exception allows for testing and a single sys exit point in the code.
    """
    pass


class NoConfigurationFileFound(Exception):
    """Raise exception when a mandatory input parameter is missing."""
    pass


class MissingRequiredParameters(Exception):
    """Raise exception when a mandatory input parameter is missing."""
    pass


class InvalidDataFileInputParameter(Exception):
    """Raise an exception when the --file parameter points to a non-existent file."""
    pass


class InvalidCoordinate(Exception):
    """Raise exception when coordinates (latitude,longitude) contain invalid values."""
    pass


class InvalidFileHeadingError(Exception):
    """Raise exception when data file has invalid headings."""
    pass


class InvalidFileDataError(Exception):
    """Raise exception when file data contains invalid data types."""
    pass


def exit_on_error(message):
    """
    display a message and terminate
    provide a single point of exit for the application.

    Parameters
    ----------
    message : str
        message to display

    Returns
    -------
        n/a
    """
    if message:
        print(F'{message}\n{USAGE}')
    sys.exit()

