import typing

import requests
import bs4


MACHINE_STATS_URL = "https://www.cs.colostate.edu/machinestats/"


def fetch_machine_info() -> typing.Sequence[typing.MutableMapping[str, str]]:
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

    machines: typing.Sequence[typing.MutableMapping[str, str]] = []
    for row in rows:
        cols = [td.get_text(strip=True) for td in row.find_all('td')]
        assert len(cols) == len(headers), f"Table row contained {len(cols)} columns, expected {len(headers)}"
        info_dict = dict(zip(headers, cols))
        machines.append(info_dict)
    return machines
