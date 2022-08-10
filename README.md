# Script Function

Serpens 3 package containing a single new node `Script Function`.

This node allows to run a custom python Function from a script, and receive the return results.



![Default Script Function node](/docs_images/default_script_function.png)

- `Name` is the function name, and **must match**
- `Use Keyword Arguments` is a boolean, determining, if the function uses keyword arguments, or positional arguments


&nbsp;

# Initialization

To allow usage of Script Functions, the Script file containing python functions must first be loaded.

When changes are made, the script must be reloaded.

![Initialization](/docs_images/initialization.png)

``` python
# addon.py
def combine_strings(string1, string2):
    return string1 + string2
```


&nbsp;

# Executing Custom Function

![Custom Function Call](/docs_images/custom_function.png)

- `string1` and `string2` are the function parameter inputs, **naming must match**, **position doesn't have to match**
- `output` is the return value of function, can be **named anything**

&nbsp;

mismatched arguments:

![Custom Function Call Mismatch Arguments](/docs_images/custom_function_mismatch.png)


&nbsp;

# Executing Custom Function without Keyword Arguments

![Custom Function without Keyword Arguments](/docs_images/custom_function_without.png)

- `first` and `second` are the function paremeter inputs, but **naming doesn't have to match**, **position matters**


&nbsp;

# Executing Python Functions

![Python Function](/docs_images/function.png)


&nbsp;

# Multiple Outputs

``` python
# addon.py
def swap_input(string1, string2):
    return string2, string1
```

Multiple outputs can either be combined, or split into separate outputs.

![Multiple Outputs Combined](/docs_images/multiple_combined.png)

![Multiple Outputs Separated](/docs_images/multiple_separated.png)
