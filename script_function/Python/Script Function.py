import bpy
from ..base_node import SN_ScriptingBaseNode
from ...utils import unique_collection_name, get_python_name


class SN_ScriptFunctionNodeKeyd(bpy.types.Node, SN_ScriptingBaseNode):

    bl_idname = "SN_ScriptFunctionNodeKeyd"
    bl_label = "Script Function"
    node_color = "PROGRAM"
    bl_width_default = 200

    def on_socket_name_change(self, socket):
        if socket in self.inputs[1:-1]:
            socket["name"] = get_python_name(socket.name, "Arg", lower=False)
            socket["name"] = unique_collection_name(socket.name, "Arg", [inp.name for inp in self.inputs[1:-1]], "_", includes_name=True)
        elif socket in self.outputs[1:-1]:
            socket["name"] = get_python_name(socket.name, "Out", lower=False)
            socket["name"] = unique_collection_name(socket.name, "Out", [out.name for out in self.outputs[1:-1]], "_", includes_name=True)
            socket.python_value = socket.name
        self._evaluate(bpy.context)

    def on_dynamic_socket_add(self, socket):
        if socket in self.inputs[1:-1]:
            socket["name"] = get_python_name(socket.name, "Arg", lower=False)
            socket["name"] = unique_collection_name(socket.name, "Arg", [inp.name for inp in self.inputs[1:-1]], "_", includes_name=True)
        elif socket in self.outputs[1:-1]:
            socket["name"] = get_python_name(socket.name, "Out", lower=False)
            socket["name"] = unique_collection_name(socket.name, "Out", [out.name for out in self.outputs[1:-1]], "_", includes_name=True)
            socket.python_value = socket.name

    def on_create(self, context):
        self.add_execute_input()
        self.add_execute_output()
        inp = self.add_dynamic_data_input("Arg")
        inp.is_variable = True
        inp.changeable = True
        out = self.add_dynamic_data_output("Out")
        out.is_variable = True
        out.changeable = True

    def update_function_name(self, context):
        self["function_name"] = self.function_name.replace("\"", "'")
        self._evaluate(context)

    function_name: bpy.props.StringProperty(
        name="Name",
        description="Name of the function to run",
        update=update_function_name
    )

    def self_eval(self, context):
        self._evaluate(context)

    use_keyword_arguments: bpy.props.BoolProperty(
        name="Use Keyword Arguments",
        description="Use Keyword Arguments to call function, else positional arguments.",
        default=True,
        update=self_eval
    )

    def draw_node(self, context, layout):
        # layout.label(text="Function:")
        # layout.prop(self, "function_name", text="")
        row = layout.row(align=True)
        row.prop(self, "function_name")
        layout.prop(self, "use_keyword_arguments")
    
    def set_outputs(self):
        if len(self.outputs) == 3:
            self.outputs[1].python_value = f"return_{self.static_uid}"
        else:
            for i in range(len(self.outputs) - 2):
                self.outputs[1 + i].python_value = f"return_{self.static_uid}[{i}]"

    def evaluate(self, context):
        if self.use_keyword_arguments:
            args = ", ".join(f"{inp.name}={inp.python_value}" for inp in self.inputs[1:-1])
        else:
            args = ", ".join(f"{inp.python_value}" for inp in self.inputs[1:-1])
        self.code = f"return_{self.static_uid} = {self.function_name}({args})"
        self.code += f"\n{self.outputs[0].python_value}"
        self.set_outputs()
