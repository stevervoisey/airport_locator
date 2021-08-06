"""
Single location to define all text constants.
Used to provide help and usage information
"""

USAGE = """
usage: > python lookup_airport.py --file=directory/uk_airport_coords.csv
For help: python lookup_airport.py --help or --doc
"""

# Add any required additional help text to appear at end of parameter help.
HELP_EPILOG_TEXT = """
--position is an optional argument. When omitted the user will be prompted for a position.
"""

DOCUMENTATION = """
This tool will locate the nearest airport from a given set of data, to the coordinates entered by the user.
Nearest means direct, as the crow flies, distance from the location entered.

When running the tool a data file must be supplied containing the locations of the airports to be 
used in the search.

Optionally a location can be entered on the command line when running the tool.
When a location has been entered the nearest airport will be displayed and the tool will terminate.

If a location is not entered the user will be prompted for a location and the nearest airport will be
displayed. 
The user can then search for additional locations until they decide to exit from the tool.

The location is specified as a set of comma separated numerical coordinates: latitude,longitude

If the tool is being executed in an environment that can start a web browser, 
for example a windows laptop or PC, command line switch "--gui" will provide a prototype web browser 
interface.

The interface is fully functional, however it currently runs using the Python development webserver 
listening on port 5000.

Once the web browser has started the the gui can be accessed using the url http://127.0.0.1:5000/ 

The data should be supplied in a plain text, csv file.
The first line of the file contains the headings and MUST match:

    NAME,ICAO,Latitude,Longitude

The remaining lines contain the data, for example:

    HONINGTON,EGXH,52.342611,0.772939

For example, the first 5 lines of a data file could look like:

    NAME,ICAO,Latitude,Longitude
    HONINGTON,EGXH,52.342611,0.772939
    WELSHPOOL,EGCW,52.628611,-3.153333
    CRANFIELD,EGTC,52.072222,-0.616667
    KEMBLE,EGBP,51.668056,-2.056944

Example usage:

    > python lookup_airport.py --file=data/uk_airport_coords.csv
    > python lookup_airport.py --file=data/uk_airport_coords.csv --gui
    > python lookup_airport.py --file=data/uk_airport_coords.csv --position="51.26950,-1.03896"

"""

