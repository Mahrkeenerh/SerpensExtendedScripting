import bpy
from ..base_node import SN_ScriptingBaseNode
from ...utils import unique_collection_name, get_python_name


class SN_TryExceptNodeKeyd(bpy.types.Node, SN_ScriptingBaseNode):

    bl_idname = "SN_TryExceptNodeKeyd"
    bl_label = "Try Except"
    node_color = "PROGRAM"
    bl_width_default = 200

    print_errors: bpy.props.BoolProperty(
        name="Print Errors",
        description="Print Errors to the console",
        default=False,
        update=SN_ScriptingBaseNode._evaluate
    )

    def on_create(self, context):
        self.add_execute_input()
        self.add_execute_output("Try")
        self.add_execute_output("Else")
        self.add_execute_output("Continue")
        out = self.add_dynamic_execute_output("Exception")
        out.is_variable = True

    def draw_node(self, context, layout):
        layout.prop(self, "print_errors")

    def on_socket_name_change(self, socket):
        self._evaluate(bpy.context)

    def evaluate(self, context):
        try_code = self.outputs['Try'].python_value
        else_code = self.outputs['Else'].python_value
        continue_code = self.outputs['Continue'].python_value

        exceptions = ""
        for out in self.outputs:
            if out.is_variable and not out.dynamic:
                exception_code = out.python_value
                exception = f"except {out.name} as e:\n"
                if self.print_errors:
                    exception += f"    print(repr(e))\n"
                exception += f"    {exception_code}\n"
                if exception_code.strip():
                    exceptions += exception

        if not exceptions.strip():
            exceptions = f"except Exception as e:\n"
            if self.print_errors:
                exceptions += f"    print(repr(e))\n"
            else:
                exceptions += f"    pass\n"

        self.code = "try:\n"
        self.code += f"    {try_code if try_code.strip() else 'pass'}\n"
        self.code += f"{exceptions}"
        if else_code.strip():
            self.code += f"else:\n"
            self.code += f"    {else_code}\n"
        self.code += f"{continue_code}"
