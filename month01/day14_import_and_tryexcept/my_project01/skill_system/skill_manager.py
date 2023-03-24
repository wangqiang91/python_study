import os
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append(path1)


from skill_system.skill_deployer import *

class Manager:
    def manager_method01(self):
        print("执行skill_manager中类Manager下的method01")

Deployer().deployer_method01()