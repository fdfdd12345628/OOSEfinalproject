from base.data import Data, DataAggregator
from .conf import *

class GASTScore(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners

    def getIndividualScore(self, person: str) -> int:
        return self._practitioners[common_name][1]


class SchoolScore(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners

    def getIndividualScore(self, person: str) -> int:

        return self._practitioners[common_name][1]


class ProgramType(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners

    def getIndividualScore(self, person: str) -> int:
        return self._practitioners[common_name][1]


class Competition(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners

    def getIndividualScore(self, person: str) -> int:
        return self._practitioners[common_name][1]


class SchoolActivity(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners

    def getIndividualScore(self, person: str) -> int:
        return self._practitioners[common_name][1]


class EESelectionDataAggregator(DataAggregator):
    pass

