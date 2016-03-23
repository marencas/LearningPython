
# the abc module provides facilities for creating abstract class, which are classes that are designed
# to be inherited not instantiated
import abc

class GetterSetter(object):
    __metaclass__ = abc.ABCMeta # this is what makes the abstract base class

    @abc.abstractmethod # decorator
    def set_val(self, input):
        """Set a vlue in the instance"""
        return

    @abc.abstractmethod # decorator
    def get_val(self):
        """Get and return a value from the instance.."""
        return

# now any class that uses the GetterSetter class above to inherit from must implement all the
# abstract methods that are in the abstract class

class MyClass(GetterSetter):

    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val

x = MyClass()
x.set_val(45)
print(x.get_val())
