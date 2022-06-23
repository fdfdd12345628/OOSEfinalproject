from base.data import Data, DataAggregator

from .conf import *

class Meeting(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners

    def getIndividualScore(self, person: str) -> float:
        personActivity = None

        # Find the person with exact name
        for p in self._practitioners:
            if p == person:
                personActivity = self._practitioners[p]
                break

        # Assign position value by different position
        positionValue = 0
        if personActivity== None:
            return 0
        if personActivity[0] == 'host':
            positionValue = 1 * personActivity[3]
        elif personActivity[0] == 'participant':
            positionValue = 0.8 * personActivity[3]

        # Count score base on weight in configuration file
        return meeting_personal_performance * personActivity[1] + \
               meeting_comment * personActivity[2] + \
               meeting_position * positionValue

class Expenditure(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners

    # Return corresponing score according to configuration file
    def getIndividualScore(self, person: str) -> float:
        # personActivity = self._practitioners[0]
        personActivity=list(self._practitioners.items())[0][1]
        if(personActivity[1] != personActivity[2]):
            return common_score
        elif(not personActivity[1] and not personActivity[2]):
            return failing_score
        else:
            return qualified_score 

class Task(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners
    def getIndividualScore(self, person: str) -> float:
        personActivity = None

        # Find the person with exact name
        for p in self._practitioners:
            if p == person:
                personActivity = self._practitioners[p]
                break

        # Assign position value by different position
        positionValue = 0
        if personActivity== None:
            return 0
        if personActivity[0] == 'leader':
            positionValue = 1 * personActivity[3]
        elif personActivity[0] == 'participant':
            positionValue = 0.8 * personActivity[3]

        # Count score base on weight in configuration file
        return task_personal_performance * personActivity[1] + \
               task_impression * personActivity[2] + \
               task_position * positionValue

class ChurchDataAggregator(DataAggregator):
    pass