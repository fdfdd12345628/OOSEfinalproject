import abc


class Data(abc.ABC):
    def __init__(self):
        self._practitioners = [[]]
        self._activityContribution = 0

    @abc.abstractmethod
    def getIndividualScore(self, person: str) -> int:
        return NotImplemented

    @abc.abstractmethod
    def getPractitioners(self) -> tuple[tuple[str]]:
        return NotImplemented


class DataAggregator(abc.ABC):
    def __init__(self):
        self._events = []

    @abc.abstractmethod
    def getEvents(self) -> tuple[Data]:
        return NotImplemented

    @abc.abstractmethod
    def add(self, event: Data) -> bool:
        return NotImplemented
