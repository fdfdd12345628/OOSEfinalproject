from base.data import Data, DataAggregator

from .conf import *


class Meeting(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners

    def getIndividualScore(self, person: str) -> int:
        personActivity = None

        # Find the person with exact name
        for p in self._practitioners:
            if p == person:
                personActivity = self._practitioners[p]
                break

        # Assign position value by different position
        positionValue = 0
        if personActivity[0] == 'host':
            positionValue = 1 * personActivity[3]
        elif personActivity[0] == 'participant':
            positionValue = 0.8 * personActivity[3]

        # Count score base on weight in configuration file
        return meeting_personal_performance * personActivity[1] + \
               meeting_comment * personActivity[2] + \
               meeting_position * positionValue


class ProjectDataAggregator(DataAggregator):
    pass
