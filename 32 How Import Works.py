import sklearn
""" When modules are imported, the module is assigned to the current scope. Here it is present in the global scope
"""

print(sklearn.__version__)

""" Now to know from where various modules like sklearn etc are called, we have a seperate module 'sys'
It will give you a list of repositories from where it will try  to import the modules, based on hierarchy.
The hierarchy can be changed as well.
"""

import sys
print(sys.path)

"""Trying to import a class within a module. Here RandomForestClassifier is an ensemble class."""
from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

"""Importing a .py file from the same directory"""
import main
print(main.print_hi("Manan"))

""" If you ever write an important function which you feel will come handy a lot, write the function down on 
a file and copy it in the same directory. Later you can alsways import the file and use the function in it.
"""