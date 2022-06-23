def churchDemo():
    from church.data import Expenditure, Task, ChurchDataAggregator, Meeting
    from church.converter import ChurchConverter
    from church.reportgenerator import ChurchReportGenerator
    m1 = Meeting({
        'Potter': [
            'host', 1, 2, 5
        ],
        'Kevin': [
            'participant', 4, 5, 3
        ]
    })
    m2 = Meeting({
        'Kevin': [
            'host', 3, 3, 3
        ],
        'Stephen': [
            'participant', 3, 2, 1
        ],
        'John': [
            'participant', 5, 5, 5
        ],
        'Potter': [
            'participant', 2, 4, 4
        ]
    })
    e1 = Expenditure({
        'Potter': [
            'spender', True, True
        ]
    })
    e2 = Expenditure({
        'Kevin': [
            'spender', False, False
        ]
    })
    t1 = Task({
        'Potter': [
            'leader', 5, 5, 5
        ],
        'Christine': [
            'participant', 3, 5, 4
        ],
        'John': [
            'participant', 5, 5, 5
        ]
    })
    t2 = Task({
        'Christine': [
            'leader', 5, 5, 5
        ],
        'Stephen': [
            'participant', 5, 5, 5
        ]
    })
    dataAggregator = ChurchDataAggregator()
    dataAggregator.add(m1)
    dataAggregator.add(m2)
    dataAggregator.add(e1)
    dataAggregator.add(e2)
    dataAggregator.add(t1)
    dataAggregator.add(t2)
    convertor = ChurchConverter(dataAggregator)
    reportgenerator = ChurchReportGenerator(convertor)
    reportgenerator.generate('Potter', 'churchReport.xls')


def EEDemo():
    import EE.conf as conf
    from EE.data import GASTScore, SchoolScore, ProgramType, Competition, SchoolActivity, EESelectionDataAggregator
    from EE.converter import EESelectionConverter
    from EE.reportgenerator import EESelectionReportGenerator

    # Range 0~5 for GAST score
    GASTScore1 = GASTScore({
        conf.common_name: ['participant', 5]
    })
    # Range 0~5 for school score
    SchoolScore1 = SchoolScore({
        conf.common_name: ['participant', 4]
    })
    ProgramType1 = ProgramType({
        conf.common_name: ['participant', conf.normal_program_type]
    })
    Competition1 = Competition({
        conf.common_name: ['participant', conf.EE_related_competition_type]
    })
    Competition2 = Competition({
        conf.common_name: ['participant', conf.normal_competition_type]
    })
    SchoolActivity1 = SchoolActivity({
        conf.common_name: ['participant', conf.EE_related_activity_type]
    })
    SchoolActivity2 = SchoolActivity({
        conf.common_name: ['participant', conf.EE_related_activity_type]
    })

    dataAggregator = EESelectionDataAggregator()
    dataAggregator.add(GASTScore1)
    dataAggregator.add(SchoolScore1)
    dataAggregator.add(ProgramType1)
    dataAggregator.add(Competition1)
    dataAggregator.add(Competition2)
    dataAggregator.add(SchoolActivity1)
    dataAggregator.add(SchoolActivity2)

    convertor = EESelectionConverter(dataAggregator)
    reportgenerator = EESelectionReportGenerator(convertor)
    reportgenerator.generate(conf.common_name, 'EEReport.xls')


def projectDemo():
    from project.converter import ProjectConverter
    from project.data import GitRecord, Meeting, ProjectDataAggregator, Task, Expenditure
    from project.reportgenerator import ProjectReportGenerator
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
    e1 = Expenditure({
        'Harry': [
            'spender', True, False
        ]
    })
    e2 = Expenditure({
        'Billy': [
            'spender', False, True
        ]
    })
    t1 = Task({
        'Sean': [
            'leader', 5, 5, 5
        ],
        'Harry': [
            'participant', 3, 3, 2
        ],
        'Eric': [
            'participant', 4, 4, 5
        ]
    })
    t2 = Task({
        'Sean': [
            'leader', 4, 3, 2
        ],
        'Jane': [
            'participant', 2, 3, 4
        ],
        'Eric': [
            'participant', 3, 3, 3
        ]
    })
    g1 = GitRecord({
        'Eric': [
            'committer', True, 5
        ],
        'Sean': [
            'committer', True, 4
        ]
    })
    dataAggregator = ProjectDataAggregator()
    dataAggregator.add(m1)
    dataAggregator.add(m2)
    dataAggregator.add(e1)
    dataAggregator.add(e2)
    dataAggregator.add(t1)
    dataAggregator.add(t2)
    dataAggregator.add(g1)
    convertor = ProjectConverter(dataAggregator)
    reportgenerator = ProjectReportGenerator(convertor)
    reportgenerator.generate('Jane', 'projectReport.xls')


if __name__ == '__main__':
    churchDemo()
    projectDemo()
    EEDemo()
    print('Done')
   