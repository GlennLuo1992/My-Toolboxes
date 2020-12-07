# coding=utf-8
import arcpy
import sys
from FieldCleanTool import FieldCleanTool

reload(sys)
sys.setdefaultencoding("utf-8")


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "CommonTools"
        self.alias = "CommonTools"

        # List of tool classes associated with this toolbox
        self.tools = [FieldCleanTool]