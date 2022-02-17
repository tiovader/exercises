def get_coordinate(record: tuple[str]) -> str:
    '''

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    '''

    return record[-1]


def convert_coordinate(coordinate: str) -> tuple[str]:
    '''

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual
                      components.
    '''

    return tuple(coordinate)

a = str, str
def compare_records(azara_record: tuple, rui_record: tuple) -> bool:
    '''

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    '''

    return tuple(azara_record[1]) == rui_record[1]


def create_record(azara_record: tuple, rui_record: tuple) -> tuple:
    '''

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are
                      incompatible.
    '''

    return azara_record + rui_record if compare_records(azara_record, rui_record) else 'not a match'


def clean_up(combined_record_group: tuple[tuple]) -> str:
    '''

    :param combined_record_group: tuple of tuples - everything from both
                                                    participants.
    :return: tuple of tuples - everything "cleaned", with excess coordinates
                               and information removed.
    '''

    return ''.join('{}\n'.format(element[:1] + element[2:]) for element in combined_record_group)
    