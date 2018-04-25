import os

DATABASE = {
    'cloud': {
        'host': os.environ.get('TRASHPANDA_HOST'),
        'user': os.environ.get('TRASHPANDA_LOGIN'),
        'pass': os.environ.get('TRASHPANDA_PASSWD'),
        'name': "cloud",
    },
    'test_cloud': {
        'host': os.environ.get('TRASHPANDA_HOST'),
        'user': os.environ.get('TRASHPANDA_LOGIN'),
        'pass': os.environ.get('TRASHPANDA_PASSWD'),
        'name': "test_cloud"
    },
    'system_logs': {
        'host': os.environ.get('TRASHPANDA_HOST'),
        'user': os.environ.get('TRASHPANDA_LOGIN'),
        'pass': os.environ.get('TRASHPANDA_PASSWD'),
        'name': "system_logs",
    },
    'pipeline': {
        'host': os.environ.get('TRASHPANDA_HOST'),
        'user': os.environ.get('TRASHPANDA_LOGIN'),
        'pass': os.environ.get('TRASHPANDA_PASSWD'),
        'name': "pipeline",
    }
}
