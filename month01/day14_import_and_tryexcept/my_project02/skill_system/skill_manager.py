import os
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append(path1)

from common import *
ListHelper().list_helper_method01()

class SkillManager:
    def skill_manager_method01(self):
        print("测试001")

def skillmethod02():
    print("ceshi")