########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Jack Deller
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

# you may need to put something here...
from enum import Enum

class Control(Enum):
    PUBLIC = 1
    CONFIDENTIAL = 2
    PRIVILEGED = 3
    SECRET = 4




def securityConditionRead(assetControl: Control, subjectControl: Control):
    return subjectControl.value >= assetControl.value #only someone of higher security can read

def securityConditionWrite(assetControl: Control, subjectControl: Control):
    return subjectControl.value <= assetControl.value #You must be of lower security to write something