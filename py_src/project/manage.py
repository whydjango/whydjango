#!/usr/bin/python
'''
Created on Sep 2, 2010

@author: Chris Glass (chirstopher.glass@divio.ch)
'''
from django.core.management import execute_manager

import sys

"""
HOW TO DEBUG AND RUN FROM ECLIPSE:
----------------------------------

1. Make sure you have a recent pyDev version. To make sure it'll work, try to create a new project as
a "PyDev Django Project". If this is available to you, you're all set. Otherwise update PyDev :)

2. Checkout your project / project template as usual.

3. ./init.sh and bin/buildout as usual - Get your project up and running as usual.

4. When your project works, right-click on it in eclipse and select the "PyDev" menu, 
then "Set as Django project"

5. Right-click on the project again and choose "Properties", "PyDEV PYTHONPATH", 
then select the "String substitution variable" tab. Add a new variable with 
the name "DJANGO_MANAGE_LOCATION", and the value "py_src/project/manage.py".

6. Now right-click your *project* again, and "Run as..." -> "PyDev: Django" :)
You can now put breakpoints in your code (by double-clicking on the margin next to the line you want)
and use "Debug as..." -> "PyDev: Django" !

(7.) If you are not used to the Eclipse debug view, you might want to check out the following
website http://www.ibm.com/developerworks/library/os-ecbug/ . It's written for Java developers, but
you should be able to understand it in a Pythonic context I'm sure :)

Yay :)

"""

# The relative path is: ../../bin/django:
imat = sys.argv[0]
filename = imat.replace('py_src/project/manage.py','bin/django')

# This will only work on unix :(
lines = None
with open(filename, 'r') as working_file:
    lines = working_file.readlines()
    
recording = False
egg_paths = []
for line in lines:
    if recording:
        if ']' in line:
            recording = False
        else:
            egg_path = line.replace('\'','').replace(',','').replace(' ','').replace('\n','')
            egg_paths.append(egg_path)
    else:
        if 'sys.path[0:0] = [' in line:
            recording = True
            
sys.path[0:0] = egg_paths

try:
    import settings.switcher as setting_file # Assumes it's located in settings/
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'development_local.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(setting_file)
