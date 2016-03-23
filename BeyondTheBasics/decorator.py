
class InstanceCounter(object):
    count = 0 # this is a class variable

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def setVal(self, newVal):
        self.val = newVal

    def getVal(self):
        return self.val

    # the next method is actually operating on the class instead of the instance.
    # this is why it has the (cls) as a parameter and the return statemenet
    # has the cls.count which actually means that it is passing back the class
    # variable and not an instance variable. the parameter can have any name
    # however to make it clear it is good to use the cls. also notice the special
    # decorator.
    @classmethod
    def getCount(cls):
        return cls.count

a = InstanceCounter(5)
b = InstanceCounter(99)
c = InstanceCounter(83)

for obj in (a,b,c):
    print("val of obj: {}".format(obj.getVal()))
    print("count: {}".format(obj.getCount()))