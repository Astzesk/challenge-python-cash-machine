import sys

from ..storage.message import *

class Cover():

    def __init_subclass__(
        cls,
        lTag = 'null',
        lReport = 'null',
        lIndex = 0
    ):
        cls.tag = tagDict[lTag]
        cls.report = reportDict[lReport][lIndex]
        cls.content = cls.tag + cls.report

    def __del__(self) -> None:
        pass

    def print(self):
        print(self.content)

    def print(self, tag, report, index):
        self.tag = tagDict[tag]
        self.report = reportDict[report][index]
        self.content = self.tag + self.report

        print(self.content)

    def printReport(self, report, index):
        return reportDict[report][index]

    def error(self):
        print(reportDict['error'][0], sys.exc_info()[0:])

