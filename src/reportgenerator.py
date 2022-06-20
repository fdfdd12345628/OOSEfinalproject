import abc
from convertor import Convertor


class ReportGenerator(abc.ABC):
    def __init__(self, convertor: Convertor):
        self.convertor = convertor

    @abc.abstractmethod
    def generate(self, person: str, filePath: str) -> bool:
        return NotImplemented
