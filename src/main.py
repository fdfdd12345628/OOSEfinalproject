from data import Data, DataAggregator
from convertor import Convertor
from reportgenerator import ReportGenerator

if __name__ == '__main__':
    m = Data()
    t = Data()
    dataAggregator = DataAggregator()
    convertor = Convertor(dataAggregator)
    reportgenerator = ReportGenerator(convertor)
    reportgenerator.generate('Harry', 'report.xls')
