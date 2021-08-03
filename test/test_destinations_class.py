import pytest
from destination_classes import Destinations
from destination_classes import InvalidCoordinate

EXAMPLE_DATA = [
    "DUNDEE,EGPN,56.452499,-3.025833",
    "SWANSEA,EGFH,51.605333,-4.067833",
    "ODIHAM,EGVO,51.234139,-0.942825",
    "CULDROSE,EGDR,50.086092,-5.255711"]

EXAMPLE_DATA_DUPLICATE = [
    "DUNDEE,EGPN,56.452499,-3.025833",
    "SWANSEA,EGFH,51.605333,-4.067833",
    "ODIHAM,EGVO,51.234139,-0.942825",
    "ODTHER,XXXX,51.234139,-0.942825",
    "CULDROSE,EGDR,50.086092,-5.255711"]


def test_verify_data_bad():
    """
    Verify that creating a new destination with an invalid longitude raises 'InvalidCoordinate' exception.
    longitude -181.561625 should >= -180

    Returns
    -------
    None
    """
    lon_less_than = ["COTTESMORE,EGXJ,52.735711,-0.648769",
                     "BARKSTON HEATH,EGYE,52.962225,-181.561625"]

    with pytest.raises(InvalidCoordinate):
        airports = Destinations(lon_less_than)


def test_verify_data_good():
    """
    Verify that creating a new destination with a valid coordinates does not raise
    'InvalidCoordinate' exception.
    Returns
    -------

    """
    good = ["COTTESMORE,EGXJ,52.735711,-0.648769",
            "BARKSTON HEATH,EGYE,52.962225,-0.561625"]

    airports = Destinations(good)


def test_shortest_distance():
    """
    Verify that Destinations.shortest_distance successfully returns: '(location), distance, []'

        The location of the nearest airport (name,code,longitude,latitude)
        The distance to the nearest airport.
        No warning messages.

    Returns
    -------
    None
    """

    lands_end = (50.19669, -5.69011)
    john_o_groats = (58.64910, -2.68737)
    old_basing = (51.26950, -1.03896)

    airports = Destinations(EXAMPLE_DATA)

    assert (('CULDROSE', 'EGDR',	50.086092, -5.255711), 33.31035193167905, []) == \
           airports.shortest_distance(lands_end)

    assert (('DUNDEE', 'EGPN', 56.452499, -3.025833), 245.08334189079903, []) == \
           airports.shortest_distance(john_o_groats)

    assert (('ODIHAM', 'EGVO', 51.234139, -0.942825), 7.760514489316363, []) == \
           airports.shortest_distance(old_basing)


def test_shortest_distance_multiple_destinations_found():
    """
    Verify that if two airports are the same distance from the required position
    a warning message is returned.

    Returns
    -------
    None
    """
    old_basing = (51.26950, -1.03896)

    airports = Destinations(EXAMPLE_DATA_DUPLICATE)

    assert (('ODIHAM', 'EGVO', 51.234139, -0.942825), 7.760514489316363,
            ['WARNING: Multiple nearest airports found [ODTHER , ODIHAM]']) == \
           airports.shortest_distance(old_basing)
