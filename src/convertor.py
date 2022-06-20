import abc
from data import Data, DataAggregator


class Convertor(abc.ABC):
    def __init__(self, aggregator: DataAggregator):
        self.aggregator = aggregator

    @abc.abstractmethod
    def getIndividualScore(self, person: str) -> int:
        return NotImplemented

    @abc.abstractmethod
    def getGroupScore(self, person: str) -> dict:
        return NotImplemented
