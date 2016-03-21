class HL7Msg(object):

    def __init__(self, filePath):
        self.filePath = self.formatFile(filePath)

    def parseMsg(self):
        self.msg = open(self.filePath).read()
        self.splitLines = self.msg.split('\n')
        return self.splitLines

    def msgType(self):
        self.splitFileNm = fileNm.split('|')
        self.msgType = self.splitFileNm[8]
        self.msgType = self.msgType.split('^')
        self.msgType = self.msgType[-1]
        return self.msgType

    @staticmethod
    def formatFile(name):
        fileNameList = list(name)
        for x in range(len(fileNameList)):
            if fileNameList[x] == '\\':
                fileNameList[x] = '/'
        name = ''.join(fileNameList)
        return name

a = HL7Msg(r"C:\users\castillom\pythoncode\sampleHL7.txt")
print a.filePath
print a.parseMsg()
print a.msgType()
