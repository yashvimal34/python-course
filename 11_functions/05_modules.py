# Python provides two types of modules:
# 1. Built in modules.
# 2. External modules.
# List of all the built in Modules: https://docs.python.org/3/py-modindex.html

import math
import mymodule
import requests 
print(math.sqrt(56))
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)