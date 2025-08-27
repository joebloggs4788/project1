class SingletonObj(object):
    class _SingletonObj():
        def __init__(self):
            self.val = None
        def __str__(self):
            return "{0!r} {1}".format(self, self.val)
    # the rest of the class definition will follow here, as per the previous logging script
        def bling(self):
            print("bling in _SingletonObj is invoked")


    instance = None
    def __new__(cls):
        if not SingletonObj.instance:
            SingletonObj.instance = SingletonObj._SingletonObj()
        # return SingletonObj.instance
        # return cls()
        return super(SingletonObj, cls).__new__(cls)
        
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)
    # def bling(self):
    #     print("bling in SingletonObj is invoked")


if __name__ == '__main__':
    obj = SingletonObj()
    obj.bling()
    # print(dir(obj))
    # print(obj)
    # print("{0!r}".format(obj))
