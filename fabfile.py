from fabric.api import *
import datetime
import os
from deployment import settings, project_name

env.project_name = project_name

def load_settings(identifier):
    if not any(settings[identifier]['hosts']):
        raise RuntimeError("Hosts not defined, stopping...")
    env.identifier = identifier
    for key, value in settings[identifier].items():
        setattr(env, key, value)

# helpers
def cdrun(command):
    run('cd %s; %s' % (env.path, command))

# environments
def dev():
    load_settings('dev')
    
def stage():
    load_settings('stage')

def live():
    load_settings('live')
    
# tasks
def update():
    cdrun('git pull origin master')

def buildout():
    cdrun('./bin/buildout -c %(buildout_cfg)s' % env)

def migrate():
    cdrun('./bin/django syncdb' % env)
    cdrun('./bin/django migrate' % env)

def symlinkmedia():
    cdrun('./bin/django symlinkmedia' % env)

def restart_django():
    run('touch %(path)s/bin/*.wsgi' % env)

def ls():
    cdrun('ls -lAF' % env)

def uname():
    print env.hosts
    from pprint import pprint
    pprint(env)
    is_same_server = env.host == settings['live'].all_hosts[0]
    run('uname -a')

def deploy():
    update()
    buildout()
    migrate()
    symlinkmedia()
    restart_django()
