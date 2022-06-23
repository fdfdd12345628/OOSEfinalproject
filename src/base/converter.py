import abc

from .data import DataAggregator


class Converter(abc.ABC):
    def __init__(self, aggregator: DataAggregator):
        self._aggregator = aggregator

    @abc.abstractmethod
    def getIndividualScore(self, person: str) -> float:
        return NotImplemented

    @abc.abstractmethod
    def getGroupScore(self, person: str) -> dict:
        return NotImplemented
