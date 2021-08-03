from destination_classes import Destinations
from utilities import read_data_from_file
from database import create_database
from constants import DATABASE
import sqlite3
from .constants_for_testing import TEST_DATA_GOOD


def test_load_database():
    """
    Verify that a 'Destinations.destinations' data can be persisted in a database and that the data
    can then be retrieved.

    Returns
    -------
    None
    """
    test_row = ('WELSHPOOL', 'EGCW', 52.628611, -3.153333)

    airports = Destinations(
        read_data_from_file(TEST_DATA_GOOD))
    create_database(airports.destinations)

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()

    rows = cur.execute('SELECT * FROM airports where NAME = "WELSHPOOL"')
    items = [item for item in rows]
    assert items[0] == test_row

    rows = cur.execute('SELECT NAME FROM airports where Latitude = 52.628611 and Longitude = -3.153333')
    items = [item for item in rows]
    assert items[0][0] == "WELSHPOOL"
