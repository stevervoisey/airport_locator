import sys
import os
from messages import DOCUMENTATION, USAGE
from utilities import validate_coordinates


def exit_on_error(message):
    """
    display a message and terminate

    Parameters
    ----------
    message : str
        message to display

    Returns
    -------
        n/a
    """
    print(F'{message}\n{USAGE}')
    sys.exit()


class Parameters:
    """
    Perform additional verification and manipulation of command line arguments parsed by argparse.
    arguments are the made available as class instance attributes.
    """
    def __init__(self, args):
        """
        Parameters
        ----------
        args : Namespace
            Namespace returned from argparse as 'parser.parse_args(arguments)'
            used to access all command line arguments passed to the script.
        """
        if args.doc:
            self._doc()
        self.csv_file = args.file
        self.gui = args.gui
        self.position = args.position

        self._set_parameters()
        self._verify_parameters()

    @staticmethod
    def _doc():
        # Display documentation and exit.
        print(DOCUMENTATION)
        print(USAGE)
        sys.exit()

    def _set_parameters(self):
        # convert position to tuple(float, float)
        if self.position is not None:
            self.position = self.position.split(',')
            self.position = [float(self.position[0]), float(self.position[1])]
            self.position = tuple(self.position)

    def _verify_parameters(self):
        # Check for mandatory parameter 'csv_file'
        if not self.csv_file:
            exit_on_error("lookup_airport.py: error: the following arguments are required: --file")
        # verify 'csv_file' is a valid file
        if not os.path.isfile(self.csv_file):
            exit_on_error(F"invalid --file [{self.csv_file}] - not a valid file.")
        # verify position is valid coordinate pair (latitude,longitude)
        if self.position is not None:
            validate_coordinates(self.position)
