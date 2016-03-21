class InstanceCounter(object):
    count = 0 # this is a class attribute

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def setVal(self, newVal):
        self.val = newVal

    def getVal(self):
        return self.val

    @classmethod # this is a decorator
    def getCount(cls):
        return cls.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print "val of obj: {}".format(obj.getVal())
    print "count: {}".format(obj.getCount())