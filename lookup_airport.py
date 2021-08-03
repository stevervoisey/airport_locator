"""
usage: lookup_airport.py [-h] [-d] [--file FILE] [--gui] [--position POSITION]

Nearest airport locator

optional arguments:
  -h, --help           show this help message and exit
  -d, --doc            Display additional documentation about the tool.
  --file FILE          full path and file name for the data input file.
  --gui                startup a web gui user interface.
  --position POSITION  Position to calculate distance from.

    --position is an optional argument. When omitted the user will be prompted for
    a position.
"""
import sys,os
import argparse
from parameters import Parameters
from messages import DOCUMENTATION, HELP_EPILOG_TEXT
from utilities import read_data_from_file
from destination_classes import Destinations
from console_menu import main_menu
# from flask_simple_gui import app # - Example of simple GUI using HTML form
from flask_form_gui import app # Using flask_wtf form


def process_arguments(arguments: list):
    """
    use argparse to process all command line arguments

    Parameters
    ----------
    arguments : list
        list of command line arguments to process
        typically 'sys.argv[1:]' all arguments except the script name.


    Returns
    -------
    namespace
        namespace generated by argparse -> parser.parse_args(arguments)
    """
    parser = argparse.ArgumentParser(
        description='Nearest airport locator',
        epilog=HELP_EPILOG_TEXT
    )

    parser.add_argument(
        "-d", "--doc",
        help="Display additional documentation about the tool.",
        action='store_true',
        default=False
    )

    parser.add_argument(
        "--file",
        required=False,  # This is a required parameter, unless --doc is passed. So handle in parameters
        type=str,
        help="full path and file name for the data input file.",
        default=None
    )

    parser.add_argument(
        "--gui",
        help="startup a web gui user interface.",
        action='store_true',
        default=False
    )

    parser.add_argument(
        "--position",
        type=str,
        help="Position to calculate distance from.",
        default=None
    )
    return parser.parse_args(arguments)


def main():
    """
    A tool to find the nearest airport, direct as the crow flies, from a given location.

    The tool will load a csv data file containing airport locations.
    The user can either enter a position on the command line or be prompted for a position
    by a gui/console menu.

    For additional documentation see messages.DOCUMENTATION

    logic:

    Process input parameters
    Generate a Destinations object
    If position is passed on the command line, display nearest airport and exit.
    Otherwise:
        If gui is passed on the command line, start up a flask GUI to prompt for position
           and display nearest airport.

        Else start up a console menu to prompt for position and display nearest airport.

        Keep prompting for additional positions until user decides to exit.

    Note: The flask gui is currently just a prototype and is displayed using the python development
          server running on http://127.0.0.1:5001/

    Returns
    -------
    None
    """
    parameters = Parameters(process_arguments(sys.argv[1:]))
    airports = Destinations(read_data_from_file(parameters.csv_file))

    if parameters.position is not None:
        nearest, distance, messages = airports.shortest_distance(parameters.position)
        print(F'nearest airport to {parameters.position} is: {nearest[0]} '
              F'location:({nearest[2]},{nearest[3]}) '
              F'distance: {distance:.2f} km')
        if messages:
            print(messages)
        sys.exit()
    elif parameters.gui:
        app.config['documentation'] = DOCUMENTATION.split("\n")
        app.config['airports'] = airports
        app.run(port=5001, debug=True)
    else:
        main_menu(airports)


if __name__ == '__main__':
    main()