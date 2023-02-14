import bpy
from ...base_node import SN_ScriptingBaseNode



class SN_ForExecuteNode(bpy.types.Node, SN_ScriptingBaseNode):

    bl_idname = "SN_WhileExecuteNode"
    bl_label = "Loop While (Execute)"
    bl_width_default = 200
    node_color = "PROGRAM"
    
    def on_create(self, context):
        self.add_execute_input()
        self.add_boolean_input("Condition")
        self.add_execute_output("Repeat")
        self.add_execute_output("Continue")

    def evaluate(self, context):
        self.code = f"""
                    while {self.inputs['Condition'].python_value}:
                        {self.indent(self.outputs['Repeat'].python_value, 6) if self.outputs['Repeat'].python_value.strip() else 'break'}
                    {self.indent(self.outputs['Continue'].python_value, 5)}
                    """
