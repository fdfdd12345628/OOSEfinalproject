from base.converter import Converter
from base.data import Data
from .data import GASTScore, SchoolScore, ProgramType, Competition, SchoolActivity
from .conf import *


class EESelectionConverter(Converter):

    def getIndividualScore(self, person: str) -> float:
        totalScore = 0

        for e in self._aggregator.getEvents():
            totalScore += e.getIndividualScore(person)
        relatedEventList = self.getRelatedEventList()
        for eventList in relatedEventList:
            totalScore += self.countRelatedScore(eventList[0], eventList[1], eventList[2])
        return totalScore

    def getGroupScore(self, person: str) -> dict:
        groupScore = {}
        relatedEventList = self.getRelatedEventList()
        for eventList in relatedEventList:
            groupScore[eventList[3]] = self.countRelatedScore(eventList[0], eventList[1], eventList[2])
        return groupScore

    def getRelatedEventList(self) -> list:
        eventList = []
        isTalent = False
        isEERelatedActivity = False
        isEERelatedCompetition = False
        for e in self._aggregator.getEvents():
            if type(e) is ProgramType and e.getPractitioners()[common_name][1] == talent_program_type:
                isTalent = True
            if type(e) is SchoolActivity and e.getPractitioners()[common_name][1] == EE_related_activity_type:
                isEERelatedActivity = True
            if type(e) is Competition and e.getPractitioners()[common_name][1] == EE_related_competition_type:
                isEERelatedCompetition = True

        if isTalent:
            eventList.append([SchoolScore, ProgramType, 0.3, '資優班與在校成績加成'])
        if isEERelatedActivity and isEERelatedCompetition:
            eventList.append([SchoolActivity, Competition, 0.5, '電機相關活動與比賽加成'])
        return eventList

    def countRelatedScore(self, matchClass1: Data, matchClass2: Data, multiplier: float) -> float:
        existEvent1 = False
        existEvent2 = False
        for e in self._aggregator.getEvents():
            if type(e) is matchClass1:
                existEvent1 = True
            if type(e) is matchClass2:
                existEvent2 = True

        score = 0
        if existEvent1 and existEvent2:
            for e in self._aggregator.getEvents():
                if type(e) is matchClass1 or type(e) is matchClass2:
                    score += e.getIndividualScore(common_name) * multiplier

        return score
