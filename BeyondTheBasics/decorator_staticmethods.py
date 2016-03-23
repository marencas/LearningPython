class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterInt(val)
        InstanceCounter.count += 1

    @staticmethod
    def filterInt(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

a = InstanceCounter(5)
b = InstanceCounter(99)
c = InstanceCounter(83)

print a.val
print b.val
print c.val