project_name = 'ydjango'
defaults = {
    'repo': 'git://github.com/ojii/ydjango.git',
}
settings = {
    'dev': {
        'hosts': ['ydjango.ojii.ch'],
        'path': '/home/jonas/apps/ydjango/',
        'user': 'jonas',
        'buildout_cfg': 'server_dev.cfg',
        'backup_dir': '/home/jonas/bk/ydjango/',
    },
}
for key, value in settings.items():
    for k,v in defaults.items():
        if k not in value:
            value[k] = v
    value['identifier'] = key
