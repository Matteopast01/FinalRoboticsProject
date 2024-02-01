

class Knowledge:
    _data: str

    def __new__(cls):
        # TODO initialize attributes in the constructor
        if not hasattr(cls, 'instance'):
            cls.instance = super(Knowledge, cls).__new__(cls)
            cls.instance._data = ""
        return cls.instance

    def set_data(self, new_data):
        self._data = new_data

    def get_data(self):
        return self._data
