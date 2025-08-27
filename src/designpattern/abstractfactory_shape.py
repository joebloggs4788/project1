import abc
from factory_shape import Circle, Square

class AbstractFactory(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def make_object(self):
        return

class CircleFactory(AbstractFactory):
    def make_object(self):
        # do something
        return Circle()
    
class SquareFactory(AbstractFactory):
    def make_object(self):
        # do something
        return Square()
    
def draw_function(factory):
    drawable = factory.make_object()
    drawable.draw()
    
def prepare_client():
    squareFactory = SquareFactory()
    draw_function(squareFactory)
    circleFactory = CircleFactory()
    draw_function(circleFactory)


