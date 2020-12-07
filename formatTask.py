# coding=utf-8
import arcpy
import sys

# 重新加载sys模块，为什么必须要加载详情请看我的第一篇python文章 https://blog.csdn.net/yetugeng/article/details/84836722
reload(sys)
# 重新设置字符集（此时不会出现提示，别怀疑自己敲错了）
sys.setdefaultencoding("utf-8")


def format_field(field_name, input_feature, new_field_alias, new_field_name):
    fields = arcpy.ListFields(input_feature)
    base_field = None
    for field in fields:
        encode_field_baseName = field.baseName.encode(encoding='UTF-8', errors='strict')
        encode_field_name = field_name.encode(encoding='UTF-8', errors='strict')
        if encode_field_baseName == encode_field_name:
            base_field = field
            break
    arcpy.AddMessage("开始进行字段处理...")
    arcpy.AddMessage("开始处理步骤一(1/6)")
    arcpy.AddField_management(in_table=input_feature, field_alias=new_field_alias, field_name="fd8e112",
                              field_type=base_field.type,
                              field_length=base_field.length)
    arcpy.AddMessage("开始处理步骤二(2/6)")
    arcpy.CalculateField_management(input_feature, "fd8e112", "!{}!".format(field_name), "PYTHON_9.3")
    arcpy.AddMessage("开始处理步骤三(3/6)")
    arcpy.DeleteField_management(input_feature, field_name)
    arcpy.AddMessage("开始处理步骤四(4/6)")
    arcpy.AddField_management(in_table=input_feature, field_alias=new_field_alias, field_name=new_field_name,
                              field_type=base_field.type,
                              field_length=base_field.length)
    arcpy.AddMessage("开始处理步骤五(5/6)")
    arcpy.CalculateField_management(input_feature, new_field_name, "!fd8e112!", "PYTHON_9.3")
    arcpy.AddMessage("开始处理步骤六(6/6)")
    arcpy.DeleteField_management(input_feature, "fd8e112")


p_input_feature = r'E:\重要文档\1工作任务\智慧海安\海安示范应用数据整理\haianCompany.gdb\haianCompany'
p_field_name = "电话"
p_new_field_name = "tel"
p_new_field_alias = "teleNum"
format_field(field_name=p_field_name,
             input_feature=p_input_feature,
             new_field_name=p_new_field_name,
             new_field_alias=p_new_field_alias)
