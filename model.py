import re


class Model:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        """
        Validate the name
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+[A-Za-z0-9.-]\b'
        if re.fullmatch(pattern, value):
            self.__name = value
        else:
            raise ValueError(f'Invalid name address: {value}')

    def save(self):
        """
        Save the name into a file
        :return:
        """
        with open('names.txt', 'a') as f:
            f.write(self.name + '\n')
