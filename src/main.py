def churchDemo():
    pass


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
    reportgenerator.generate(conf.common_name, 'report.xls')


def projectDemo():
    from project.converter import ProjectConverter
    from project.data import Meeting, ProjectDataAggregator
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
    dataAggregator = ProjectDataAggregator()
    dataAggregator.add(m1)
    dataAggregator.add(m2)
    convertor = ProjectConverter(dataAggregator)
    reportgenerator = ProjectReportGenerator(convertor)
    reportgenerator.generate('Harry', 'report.xls')


if __name__ == '__main__':
    EEDemo()
