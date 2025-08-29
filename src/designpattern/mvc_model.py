
# initial grouping of functions
# import os

# def get_append_write(filename):
#     if os.path.exists(filename):
#         return 'a'
#     return 'w'

# def read_names(filename):
#     with open(filename, 'r') as data_file:
#         names = data_file.read().split('\n')
#         return names

# def write_name(filename, name):
#     with open(filename, get_append_write(filename)) as data_file:
#         data_file.write("{}\n".format(name))

import os
class NameModel(object):
    def __init__(self):
        self.filename = 'names.dat'
    def _get_append_write(self):
        if os.path.exists(self.filename):
            return 'a'
        return 'w'
    def get_name_list(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as data_file:
            names = data_file.read().split('\n')
            return names
    def save_name(self, name):
        with open(self.filename, self._get_append_write()) as data_file:
            data_file.write("{}\n".format(name))

