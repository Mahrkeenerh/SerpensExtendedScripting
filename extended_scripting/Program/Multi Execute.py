import bpy
from ..base_node import SN_ScriptingBaseNode


class SN_MultiExecuteNode(bpy.types.Node, SN_ScriptingBaseNode):

    bl_idname = "SN_MultiExecuteNode"
    bl_label = "Multi Execute"
    node_color = "PROGRAM"

    def on_create(self, context):
        self.add_execute_input()
        self.add_execute_output()
        self.add_dynamic_execute_input()
        self.add_dynamic_execute_output()

    def on_dynamic_socket_add(self, socket):
        socket.python_value = self.code

    def evaluate(self, context):
        self.code = f"{self.outputs[0].python_value}"
        for output in self.outputs[1:-1]:
            self.code += f"\n{output.python_value}"
