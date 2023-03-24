import os
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append(path1)

from common.list_helper import *

List_Helper.helper_method01()

class Deployer:
    def deployer_method01(self):
        print("执行skill_deployer中类Deployer下的method01")