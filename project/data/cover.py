import sys

import data.message as message

class Cover():

    def __init_subclass__(
        cls,
        lTag = 'null',
        lReport = 'null',
        lIndex = 0
    ):
        cls.tag = message.tagDict[lTag]
        cls.report = message.reportDict[lReport][lIndex]
        cls.content = cls.tag + cls.report

    def __del__(self) -> None:
        pass

    def print(self):
        print(self.content)

    def print(self, tag, report, index):
        self.tag = message.tagDict[tag]
        self.report = message.reportDict[report][index]
        self.content = self.tag + self.report

        print(self.content)

    def error(self):
        print(message.reportDict['error'][0], sys.exc_info()[0])

