##import sys
##import os
##sys.path.append(os.path.abspath("\Users\User\OneDrive\Desktop\git\Python\exampleAssessment\Tests"))

import pytest
##from Tests 
import example

def test_endsPy():
    assert example.endsPy("ilovepy") == True
    assert example.endsPy("welovepy") == True
    assert example.endsPy("welovepyforreal") == False
    assert example.endsPy("pyiscool") == False
    assert example.endsPy("hurrayforpY") == True