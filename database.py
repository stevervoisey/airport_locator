import sqlite3


def create_database(data: list) -> None:
    """
    create a simple database to persist airport location data.
    currently not used.

    Parameters
    ----------
    data : list[tuple]]

    Returns
    -------
    None

    """
    con = sqlite3.connect('airport.db')
    cur = con.cursor()

    cur.execute('''drop table if exists airports''')
    cur.execute('''CREATE TABLE airports
                (NAME text, ICAO text, Latitude real, Longitude real)''')

    for row in data:
        cur.execute("INSERT INTO airports VALUES (?, ?, ?, ?)", row)

    con.commit()
    con.close()
