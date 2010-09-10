############
Installation
############

To install, run following commands::

    git clone git://github.com/ojii/ydjango.git
    ./init.sh
    bin/django syncdb --all
    bin/django migrate --fake

Note that you *could* alternatively do `bin/django syncdb` and 
`bin/django migrate` but the CMS migrations tend to take very long and fail on
sqlite.


Customizing local configurations
================================

If you want to change configurations only applying to your machine, copy
personal.cfg-dist and name it personal.cfg. Make a copy of
py_src/project/settings/personal.py-dist and name it
py_src/project/settings/personal.py. In that settings file, make the changes
you need. Run `bin/buildout -c personal.cfg` to tell your installation to use
that settings file.

###################
Deploying to server
###################

Adding a new server (project stage)
===================================

You can add new project stages (servers) by editing the deployment.py file.

Deploying to an existing server
===============================

If you have access to an existing server, you can deploy to that server using
`bin/fab <project-stage> deploy`, for example for the dev server, run
`bin/fab dev deploy`.
