import os
from utilities import validate_coordinates


def clear():
    """
    clear the console depending on the type of os.
    Returns
    -------
    None
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def main_menu(airports) -> None:
    """
    Simple console menu to prompt for a position and then display the nearest airport.

    Parameters
    ----------
    airports : Destination object

    Returns
    -------
    None

    """
    clear()
    print("Welcome to the nearest airport lookup utility.\n")

    while True:
        print_menu()
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            clear()
            print('Wrong input type. Please enter a number ...')
            continue
        # Check what choice was entered and act accordingly
        if option == 1:
            option1(airports)
        elif option == 2:
            print('Bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 2.')


menu_options = {
    1: 'Find nearest airport',
    2: 'Exit',
}


def print_menu() -> None:
    """
    simple console menu to prompt for a location and then display the nearest airport.

    Returns
    -------
    None
    """
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1(airports) -> None:
    """
    User has selected 'Find nearest airport'.
    Prompt for 'latitude' and 'longitude' and display nearest airport.

    Parameters
    ----------
    airports : Destinations object

    Returns None
    -------
    """
    clear()
    while True:
        latitude = read_float("Enter latitude: ")
        longitude = read_float("Enter longitude: ")
        fails = validate_coordinates((latitude, longitude))
        if fails is not None:
            print(F'Invalid coordinates, please enter valid values.')
            print(F'{fails[1]} {fails[0]}')
        else:
            nearest, distance, messages = airports.shortest_distance((latitude, longitude))
            print(F'\nnearest airport to ({latitude},{longitude}) '
                  F'is: {nearest[0]} location: ({nearest[2]},{nearest[3]}) '
                  F'distance: {distance:.2f} km')
            if messages:
                print(messages)
            input("\nHit any key to continue")
            clear()
            return


def read_float(message):
    """
    Use 'message' to prompt for a float value. Keep prompting until a valid float value is entered.

    Parameters
    ----------
    message : str
        input message prompt string

    Returns
    -------
    float
    """
    while True:
        value = None
        try:
            value = float(input(message))
        except ValueError:
            clear()
            print('Wrong input. Please enter a number ...')

        if isinstance(value, float):
            return value
