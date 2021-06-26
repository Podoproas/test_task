import re                               # as I understood regex lib is in standard library
import gzip
import pprint
from typing import Iterable, Dict, TextIO, Tuple, Union


def check_comment(line: str) -> bool:
    """
    Checks if the line is a comment line: comment line starts with #
    :param line:
    :return:
    """
    return line.startswith("#")         # in assumption that comments begin with the first letter


def is_empty_string(line: str) -> bool:
    """
    Checks if the line is an empty line containing only space characters ending with \n
    :param line:
    :return:
    """
    return len(re.findall(r'^\s*\n$', line)) == 1


def get_key_and_value(line: str) -> Tuple[Union[str, None], str]:
    """
    Using regex expr. find key and value in a string in assumption key do not begin with space character
    (such keys will be interpreted as a value of a previous key)
    :param line: String where key and value have to be present in
    :return: key may be None and value as a string without any space characters at the beginning or end
    """
    #
    match = re.match(r'^(?:(?P<key>[^\s].*?)\s*:)?\s*(?P<value>.*?)\s*$', line)
    return match.group('key'), match.group('value')


def get_valid_line(io: TextIO):
    """
    Yeilds a new line from a file excepting comment lines
    :param io: TextIO object with readline() method
    :return:
    """
    line = io.readline()
    while line:
        while check_comment(line):
            line = io.readline()
        yield line
        line = io.readline()


def get_document(io: TextIO) -> Iterable[Dict]:
    """
    Yields documents that are read from a file
    :param io: TextIO object with readline() method
    :return: document
    """
    document = {}
    key = None
    for line in get_valid_line(io):
        if is_empty_string(line):
            if document == {}:
                continue
            yield document
            document = {}
        else:
            new_key, value = get_key_and_value(line)
            key = new_key if new_key else key

            if key is None:
                raise ValueError("No key for the first line in document")

            if key not in document:
                document[key] = ""
            document[key] += ("\n" if len(document[key]) else "") + value
    return document


def parse_file(path: str) -> Iterable[Dict]:
    """
    :param path: full path to a file as a string
    :return: None
    """
    try:
        gzip.open(path, mode="rt").readline()       # trying to read file as a gzip file
        file = gzip.open(path, mode="rt")
    except gzip.BadGzipFile:
        file = open(path, "r")
    except IOError as err1:
        print(f"Some error in reading file {path}\n")
        raise err1

    with file:
        for doc in get_document(file):
            yield doc


def load_data(path: str) -> None:
    parsed_data = parse_file(path)

    for document in parsed_data:
        pprint.pprint(document)


if __name__ == "__main__":
    load_data('example.txt')
