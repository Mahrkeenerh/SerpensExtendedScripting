import re

import bpy
from ..base_node import SN_ScriptingBaseNode
from ...utils import unique_collection_name, get_python_name


class SN_ExpressionNode(bpy.types.Node, SN_ScriptingBaseNode):

    bl_idname = "SN_ExpressionNode"
    bl_label = "Expression"
    node_color = "PROGRAM"
    bl_width_default = 200

    def on_dynamic_socket_add(self, socket):
        socket["name"] = "inp_000"
        socket["name"] = unique_collection_name(socket.name, "inp_000", [inp.name for inp in self.inputs[1:-1]], "_", includes_name=True)

    def on_create(self, context):
        self.add_execute_input()
        self.add_execute_output()
        self.inputs[0].set_hide(True)
        self.outputs[0].set_hide(True)
        self.add_dynamic_data_input("Input").changeable = True
        self.add_data_output("Expression").changeable = True

    def update_expression(self, context):
        self["expression"] = self.expression.replace("\"", "'")
        self._evaluate(context)

    expression: bpy.props.StringProperty(
        name="Expression",
        description="Expression to evaluate",
        update=update_expression
    )

    def update_require_execute(self, context):
        if self.require_execute:
            self.outputs[1]["name"] = "Output"
        else:
            self.outputs[1]["name"] = "Expression"

        self.inputs[0].set_hide(not self.require_execute)
        self.outputs[0].set_hide(not self.require_execute)
        self._evaluate(context)

    require_execute: bpy.props.BoolProperty(
        name="Require Execute",
        description="Execute node and keep results",
        default=False,
        update=update_require_execute
    )

    def draw_node(self, context, layout):
        layout.label(text="Expression:")
        layout.prop(self, "expression", text="")
        layout.prop(self, "require_execute")

    def multiple_replace(self, string, rep):
        rep = dict((re.escape(k), v) for k, v in rep.items())
        pattern = re.compile("|".join(rep.keys()))
        return pattern.sub(lambda m: rep[re.escape(m.group(0))], string)

    def evaluate(self, context):
        to_replace = {i.name: i.python_value for i in self.inputs[1:-1]}

        if to_replace:
            expression = self.multiple_replace(self.expression, to_replace)
        else:
            expression = self.expression
        
        if not expression:
            expression = None

        if self.require_execute:
            self.code = f"return_{self.static_uid} = {expression}"
            self.code += f"\n{self.outputs[0].python_value}"
            self.outputs[1].python_value = f"return_{self.static_uid}"
        else:
            self.outputs[1].python_value = f"eval(\"{expression}\")"
