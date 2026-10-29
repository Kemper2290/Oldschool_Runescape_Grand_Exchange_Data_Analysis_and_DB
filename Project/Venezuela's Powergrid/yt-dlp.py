
import numpy as np
import sys
print(sys.version)
print("hello world")


import pkgutil

# Iterate through all available modules in the current environment
for module_info in pkgutil.iter_modules():
    print(module_info.name)
