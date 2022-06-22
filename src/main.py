from project.converter import ProjectConverter
from project.data import Meeting, ProjectDataAggregator
from project.reportgenerator import ProjectReportGenerator


def projectDemo():
    m1 = Meeting({
        'Harry': [
            'host', 1, 2, 5
        ],
        'Jane': [
            'participant', 4, 5, 3
        ]
    })
    m2 = Meeting({
        'Jane': [
            'host', 3, 3, 2
        ],
        'Harry': [
            'participant', 1, 2, 3
        ],
        'Billy': [
            'participant', 5, 5, 5
        ],
    })
    dataAggregator = ProjectDataAggregator()
    dataAggregator.add(m1)
    dataAggregator.add(m2)
    convertor = ProjectConverter(dataAggregator)
    reportgenerator = ProjectReportGenerator(convertor)
    reportgenerator.generate('Harry', 'report.xls')


if __name__ == '__main__':
    projectDemo()
