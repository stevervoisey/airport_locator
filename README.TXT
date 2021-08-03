Developed with python V3.8

Quick Start:

> unzip AirportLocator.zip
> cd AirportLocator/appcode
> python ./lookup_airport.py --help
> python ./lookup_airport.py --file=../data/uk_airport_coords.csv
> python ./lookup_airport.py --file=../data/uk_airport_coords.csv --position="51.26950,-1.03896"
> python ./lookup_airport.py --file=../data/uk_airport_coords.csv --gui
  open a browser at url http://127.0.0.1:5000/

to test
> pwd
..\AirportLocator
> python -m pytest -v



Python tool to locate the nearest airport to a given position.

The script requires an input file containing the data to be used in the search.
See data/uk_airport_coords.csv
Any file with the same format can also be used.

Distances are direct, as the crow files and calculated as a distance on the surface of a sphere.

The position to search from can be entered from the command line, or via a menu/gui after the tool
has started.

For more information use the --doc argument.

usage: lookup_airport.py [-h] [-d] [--file FILE] [--gui] [--position POSITION]

Nearest airport locator

optional arguments:
  -h, --help           show this help message and exit
  -d, --doc            Display additional documentation about the tool.
  --file FILE          mandatory: full path and file name for the data input file.
  --gui                optional:  startup a web gui user interface.
  --position POSITION  optional:  Position to calculate distance from.

    --position is an optional argument. When omitted the user will be prompted for
    a position.

ISSUES:

pytest
======

External test file locations need full path.
This has been defined in one location 'constants_for_testing.py'.
This WILL have to be updated for a new environment if absolute file path changes.

The following command works as expected and should be used for running pytest.
In addition, each test can be executed individually inside pycharm.

    Code uses:  from parameters import Parameters
    Test uses:  from parameters import Parameters
                from .test_constants import PROJECT_DIRECTORY

    > pwd
    ..\AirportLocator
    > python -m pytest -v

The following command will NOT work.

    > pwd
    ..\AirportLocator
    > pytest -v OR pytest -v --cache-clear

ImportError while importing test module 'D:\WORK\Development\Python\Code\L3Harris\AirportLocatorProject\AirportLocator\test\test_parameters.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\DEVELOPMENT\Python_03\3.8.4\lib\importlib\__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test\test_parameters.py:3: in <module>
    from parameters import Parameters
E   ModuleNotFoundError: No module named 'parameters'

OLD:

Fixed: Use command 'python -m pytest' test imports use '.' code imports standard.

pytest must be run in the folder containing the tests to avoid issues finding test data files.
pytest will look for the files in its execution directory, not the directory containing the tests.
Could resolve with absolute file paths, but this would not enable distribution via zipfile.

Fixed: As above
validate_coordinates should be located in utilities.py
  from utilities import validate_coordinates

Fixed:
The string constants DOCUMENTATION, HELP_EPILOG_TEXT, USAGE should all be located in messages.py

This does not cause a problem running the application, but currently this causes issues for pytest.

Suspect issue with pytest and virtual environments.


Consequently, the validate_coordinates function is defined twice!
in paramaters.py and utilities.py

Fixed:
Code will be restored to original location once pytest issue has been resolved.

web gui form validation to be added.

Fixed:
Documented url changed from: http://127.0.0.1:5000/ to http://127.0.0.1:5001/