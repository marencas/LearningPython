class MaxSizeList(object):

    def __init__(self, intVal):
        self.maxSize = intVal
        self.myList = []

    def __str__(self):
        return str(len(self.myList))

    # below is the method that I created for this assignment. after reviewing how the course
    # instructor solved the problem i can see where i created more lines of code unnecessarily.
    def push(self, listVal):
        if len(self.myList) == self.maxSize:
            self.myList.pop(0)
            self.myList.append(listVal)
        else:
            self.myList.append(listVal)

    # this is the code that was created by the instructor of the course
    def coursePush(self, listVal):
        self.myList.append(listVal)
        if len(self.myList) > self.maxSize:
            self.myList.pop(0)

    def getList(self):
        return self.myList