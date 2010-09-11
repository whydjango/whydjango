project_name = 'ydjango'
defaults = {
    'repo': 'git://github.com/whydjango/whydjango.git',
}
settings = {
    'dev': {
        'hosts': ['ydjango.ojii.ch'],
        'path': '/home/jonas/apps/ydjango/',
        'user': 'jonas',
        'buildout_cfg': 'server_dev.cfg',
        'backup_dir': '/home/jonas/bk/ydjango/',
    },
    'live': {
        'hosts': ['whydjango.com'],
        'path': '/home/whydjango/apps/ydjango/',
        'user': 'whydjango',
        'buildout_cfg': 'server_live.cfg',
        'backup_dir': '/home/whydjango/bk/ydjango/',
    },
}
for key, value in settings.items():
    for k,v in defaults.items():
        if k not in value:
            value[k] = v
    value['identifier'] = key
