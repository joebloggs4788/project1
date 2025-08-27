from abc import abstractmethod, ABCMeta

class Prototype(metaclass = ABCMeta):
    @abstractmethod
    def clone(self):
        pass