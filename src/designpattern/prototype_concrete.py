import prototype_interface as interface
from copy import deepcopy

class Concrete(interface.Prototype):
    def clone(self):
        return deepcopy(self)