import abc

class TemplateMethodAbstractBaseClass(metaclass = abc.ABCMeta):
    def template_method(self):
        self._step1()
        self._step2()
        self._step3()
    def send_transaction(self):
        self._send_transaction()
    
    @abc.abstractmethod
    def _step1(): pass
    @abc.abstractmethod
    def _step2(): pass
    @abc.abstractmethod
    def _step3(): pass

    @abc.abstractmethod
    def _send_transaction(*arg): pass

class ConcreteImplementationClass(TemplateMethodAbstractBaseClass):
    def _step1():
        print("ConcreteImplementationClass._step1()")
    def _step2():
        print("ConcreteImplementationClass._step2()")
    def _step3():
        print("ConcreteImplementationClass._step3()")
    def _send_transaction(*arg):
        print("ConcreteImplementationClass._send_transaction()")