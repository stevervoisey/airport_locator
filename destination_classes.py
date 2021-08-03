from math import cos, asin, sqrt, pi
from utilities import validate_coordinates, InvalidCoordinate


class Destinations:
    """
    Stores a list of airport location coordinates. Given a new coordinate, find the nearest airport.

    The list of airport locations must be provided as strings in the following format:
        ["name,code,latitude,longitude",
         "name,code,latitude,longitude",]

    'latitude' and 'longitude' are string values that must be convertible to float coordinates.
    Example:
        "DUNDEE,EGPN,56.452499,-3.025833",
        "SWANSEA,EGFH,51.605333,-4.067833",

    attributes
    ----------
    destinations : list[("name","code",float(latitude),float(longitude)),(...),]
        verified list of destination tuples.
        storing as tuples simplifies persisting in a database if required in future.

    public methods
    --------------
    shortest_distance(position)
        Find nearest stored location to position and distance from position.

    Raises exceptions
    -----------------
        InvalidCoordinate()
    """
    def __init__(self, raw_destinations: list):
        """
        parameters
        ----------
        raw_destinations : list["name,code,latitude,longitude"]
            list of airport locations
        """
        self.destinations = []
        self._convert_data(raw_destinations)
        self._verify_data()

    @staticmethod
    def _circular_distance_from_lat_lon(lat1, lon1, lat2, lon2):
        # Calculate the spherical distance between two coordinates using the haversine formula.
        p = pi/180
        a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
        return 12742 * asin(sqrt(a))  # 2*R*asin...

    def _convert_data(self, raw_destinations: list):
        # split each string into a four elements: [str, str, float, float]
        for row in raw_destinations:
            lrow = row.rstrip().split(',')
            lrow = (lrow[0], lrow[1], float(lrow[2]), float(lrow[3]))
            self.destinations.append(lrow)

    def _verify_data(self):
        # If any destination coordinates are invalid raise exception 'InvalidCoordinate'
        for row in self.destinations:
            fails = validate_coordinates((row[2], row[3]))
            if fails is not None:
                raise InvalidCoordinate(F"{fails[1]} in coordinates {fails[0]}")

    def _circular_distance(self, coord1: tuple, coord2: tuple):
        # split up coordinates into latitude,longitude pairs
        return self._circular_distance_from_lat_lon(coord1[0], coord1[1], coord2[0], coord2[1])

    def shortest_distance(self, position: tuple) -> tuple:
        """
        Calculate the shortest distance between two points on a sphere.

        For each location stored in 'self.destinations', calculate the distance from the argument 'position'.
        Return the shortest distance found.
        If two locations have the same, shortest distance, Return a warning.

        parameters
        ----------
            position : tuple(float, float)
                tuple of float numbers representing a pair of coordinates (latitude, longitude)
        return
        ------
            tuple(str, str, float, float, float, list[str])
            tuple containing the:
                closest destination to position -> name, code, latitude, longitude
                distance from position          -> distance
                message list                    -> messages

            messages:
            list of messages indicating any issues that may have occurred, specifically if
            two destinations are at the same distance from position.
            Typically this list should be empty.
        """
        equal_destinations = []
        messages = []
        short_destination = None

        short_distance = self._circular_distance(position, (self.destinations[0][2], self.destinations[0][3])) + 1
        for destination in self.destinations:
            distance = self._circular_distance(position, (destination[2], destination[3]))
            if short_destination is not None and distance == short_distance:
                equal_destinations.append([destination[0], distance])
            if distance < short_distance:
                short_distance = distance
                short_destination = destination

        for entry in equal_destinations:
            if entry[1] == short_distance:
                messages.append(
                    F'WARNING: Multiple nearest airports found [{entry[0]} , {short_destination[0]}]')

        return short_destination, short_distance, messages
