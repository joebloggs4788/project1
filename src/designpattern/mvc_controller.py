

# function grouping

# import os
# def name_in_file(filename, name):
#     if not os.path.exists(filename):
#         return False
#     return name in read_names(filename)

# def get_message(name):
#     if name_in_file('names.dat', name):
#         return "Welcome back {}!".format(name)
#     write_name('names.dat', name)
#     return "Hi {}, it is good to meet you".format(name)

# if __name__ == "__main__":
#     main(sys.argv[1])

import sys

from mvc_model import NameModel
from mvc_view import GreetingView

class GreetingController(object):
    def __init__(self):
        self.model = NameModel()
        self.view = GreetingView()
    def handle(self, request):
        if request in self.model.get_name_list():
            greeting = self.view.generate_greeting(name=request, instore=True)
        else:
            self.model.save_name(request)
            greeting = self.view.generate_greeting(name=request, instore=False)
        self.view.update_view(greeting)

def main(name):
    request_handler = GreetingController()
    request_handler.handle(name)

if __name__ == "__main__":
    main(sys.argv[1])
