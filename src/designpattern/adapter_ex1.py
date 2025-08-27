# This is what the generic implementation of the idea would look like:
class ObjectAdapter(object):
    def __init__(self, what_i_have, provided_function):
        self.what_i_have = what_i_have
        self.required_function = provided_function
    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)