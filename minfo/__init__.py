import enum
import typing

import requests
import bs4


MACHINE_STATS_URL = "https://www.cs.colostate.edu/machinestats/"


class MinfoFields(enum.StrEnum):
    """Enumeration representing the header fields in the machinestats table.
    Order and string value of enumeration must match the contents of the table.
    """
    HOST = 'Hostname'
    LOCATION = 'Location'
    DATE = 'Date'
    TIME = 'Time'
    CPU_USAGE = 'CPU Usage (%)'
    LOAD_AVG = 'Load Average'
    MEM_USAGE = 'Memory Usage (%)'
    GPU_USAGE = 'GPU Memory Usage (%)'
    RDP_SESSIONS = 'RDP Sessions Used'
    UP_TIME = 'Up Time'
    USERS = 'Logged-in Users'


def fetch_machine_info() -> typing.Sequence[typing.MutableMapping[MinfoFields, str]]:
    response = requests.get(MACHINE_STATS_URL)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    assert table is not None, "URL did not contain a Machine Info table..."

    rows = table.find_all('tr')
    assert rows is not None, "Machine Info table contained no rows..."
    header = rows.pop(0)

    headers = [th.get_text(strip=True) for th in header.find_all('th')]
    assert headers is not None, "Header Row contained no entries..."
    assert len(headers) == len(MinfoFields), "Header Row does not contain the expected number of fields..."
    assert all(field == minfo_field.value for field, minfo_field in zip(headers, MinfoFields)), "Header Row contents do not match the expected fields..."

    machines: typing.Sequence[typing.MutableMapping[MinfoFields, str]] = []
    for row in rows:
        cols = [td.get_text(strip=True) for td in row.find_all('td')]
        assert len(cols) == len(MinfoFields), f"Table row contained {len(cols)} columns, expected {len(MinfoFields)}"
        info_dict = dict(zip(MinfoFields, cols))
        machines.append(info_dict)
    return machines
