# coding=utf-8
import arcpy
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class FieldCleanTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "FieldCleanTools"
        self.description = "一键修改字段名称、别名，用于规范化数据字段"
        self.canRunInBackground = False

    def getParameterInfo(self):
        param0 = arcpy.Parameter(
            displayName='Input Features',
            name='in_features',
            datatype="GPFeatureLayer",
            parameterType='Required',
            direction='Input')
        param1 = arcpy.Parameter(
            displayName='Field',
            name='base_field',
            datatype='Field',
            parameterType='Required',
            direction='Input')
        param2 = arcpy.Parameter(
            displayName='New Field Name',
            name='new_field_Name',
            datatype='GPVariant',
            parameterType='Required',
            direction='Input')
        param3 = arcpy.Parameter(
            displayName='New Field Alias',
            name='new_field_Alias',
            datatype='GPVariant',
            parameterType='Required',
            direction='Input')
        param1.parameterDependencies = [param0.name]
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_feature = parameters[0].valueAsText
        field_name = parameters[1].valueAsText
        new_field_name = parameters[2].valueAsText
        new_field_alias = parameters[3].valueAsText
        self.format_field(field_name, input_feature, new_field_alias, new_field_name)
        return

    def format_field(self, field_name, input_feature, new_field_alias, new_field_name):
        fields = arcpy.ListFields(input_feature)
        base_field = None
        for field in fields:
            if field.baseName == field_name:
                base_field = field
                break
        arcpy.AddMessage("正在创建新字段...")
        arcpy.AddMessage("(1/6)")
        arcpy.AddField_management(in_table=input_feature, field_alias=new_field_alias, field_name="fd8e112",
                                  field_type=base_field.type,
                                  field_length=base_field.length)
        arcpy.AddMessage("(2/6)")
        arcpy.CalculateField_management(input_feature, "fd8e112", "!{}!".format(field_name), "PYTHON_9.3")
        arcpy.AddMessage("(3/6)")
        arcpy.DeleteField_management(input_feature, field_name)
        arcpy.AddMessage("(4/6)")
        arcpy.AddField_management(in_table=input_feature, field_alias=new_field_alias, field_name=new_field_name,
                                  field_type=base_field.type,
                                  field_length=base_field.length)
        arcpy.AddMessage("(5/6)")
        arcpy.CalculateField_management(input_feature, new_field_name, "!fd8e112!", "PYTHON_9.3")
        arcpy.AddMessage("(6/6)")
        arcpy.DeleteField_management(input_feature, "fd8e112")
        arcpy.AddMessage("完成！")
