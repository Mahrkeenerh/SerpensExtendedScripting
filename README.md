# Extended Scripting

Serpens 3 package containing new scripting nodes.

This package is free, but you can support me through: [paypal.me/mahrkeenerh](https://paypal.me/mahrkeenerh)


| [Donate](https://paypal.me/mahrkeenerh) | [Download](https://github.com/Mahrkeenerh/SerpensExtendedScripting/releases/latest/download/extended_scripting.zip) |
| - | - |

&nbsp;

# Nodes:
- [Script Function Node](#script-function)
- [Expression Node](#expression)


&nbsp;


# Script Function Node

This node allows to run a custom python Function from a script, and receive the return results.

If `Use Keyword Arguments` is checked, the function uses keyword arguments, otherwise positional arguments.

![Default Script Function node](/docs_images/default_script_function.png)


&nbsp;

## Initialization

To allow usage of Script Functions, the Script file containing python functions must first be loaded.

When changes are made, the script must be reloaded.

![Initialization](/docs_images/initialization.png)

``` python
# addon.py
def combine_strings(string1, string2):
    return string1 + string2
```


&nbsp;

## Executing Custom Function

![Custom Function Call](/docs_images/custom_function.png)

- `string1` and `string2` are the function parameter inputs, **naming must match**, **position doesn't have to match**
- `output` is the return value of function, can be **named anything**

&nbsp;

mismatched arguments:

![Custom Function Call Mismatch Arguments](/docs_images/custom_function_mismatch.png)


&nbsp;

## Executing Custom Function without Keyword Arguments

![Custom Function without Keyword Arguments](/docs_images/custom_function_without.png)

- `first` and `second` are the function paremeter inputs, but **naming doesn't have to match**, **position matters**


&nbsp;

## Multiple Outputs

``` python
# addon.py
def swap_input(string1, string2):
    return string2, string1
```

Multiple outputs can either be combined, or split into separate outputs.

![Multiple Outputs Combined](/docs_images/multiple_combined.png)

![Multiple Outputs Separated](/docs_images/multiple_separated.png)


&nbsp;

# Expression Node

This node allows you to define a python expression, or execute the python expression (to preserve current state).

![Expression Default Node](/docs_images/expression_default.png)

![Expression Require Execute](/docs_images/expression_require_execute.png)


&nbsp;

## Altering inputs

![Expression to lower](/docs_images/expression_lower.png)


&nbsp;

## Using libraries

In order to use other libraries that require to be imported, the `import` first must be executed. Then the library can be used anywhere in the addon.

![Import math](/docs_images/expression_import.png)

![Expression math ceil](/docs_images/expression_ceil.png)


&nbsp;

## Combining Expressions

`Expression` nodes can be combined to improve readability.

![Combined Expressions](/docs_images/expressions_combined.png)
