import abc


class Data(abc.ABC):
    def __init__(self):
        self.practitioners = [[]]
        self.activityContribution = 0

    @abc.abstractmethod
    def getIndividualScore(self) -> int:
        return NotImplemented

    @abc.abstractmethod
    def getPractitioners(self) -> tuple[tuple[str]]:
        return NotImplemented


class DataAggregator(abc.ABC):
    def __init__(self):
        self.events = []

    @abc.abstractmethod
    def getEvents(self) -> tuple[Data]:
        return NotImplemented

    @abc.abstractmethod
    def addEvent(self, event: Data) -> bool:
        return NotImplemented
