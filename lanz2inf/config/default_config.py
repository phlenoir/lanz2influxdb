DEFAULT_CONFIG = {
    'lanz': {
        'host': '{somewhere]',
        'port': 50001,
        'reader': 'reader.lanz_reader',
        'reconnect_wait_time_ms': 1000
    },
    'influxdb': {
        'host': 'localhost',
        'port': 8086,
        'user': 'admin',
        'password': 'admin',
        'dbname': 'optiqv2',
        'use_ssl': False,
        'verify_ssl': False,
        'timeout': 5,
        'use_udp': False,
        'retention_policy': 'autogen',
        'time_precision': 'ns'
    },
    'encoder': 'encoder.encoder',
    'buffer_size': 1000,
    'buffer_timeout': False,
    'configfile': None,
    'log_in_file': False,
    'pidfile': 'lanz2inf.pid',
    'c': None,
    'statistics': True,
    's': False,
    'verbose': 0,
    'v': 0
}
