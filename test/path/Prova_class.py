import json
from pathlib import Path


class ProvaClass:
    _file_content: dict

    def __init__(self):
        splitted = str(Path(__file__).absolute())
        print(splitted)

    def read_data(self, data_to_read):
        return self._file_content[data_to_read]
