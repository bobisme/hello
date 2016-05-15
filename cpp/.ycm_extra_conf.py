def FlagsForFile(filename, **kwargs):
    flags = [
        '-Wall',
        '-Wextra',
        '-Werror',
        '-pedantic',
        '-xc++',
        '-std=c++14',
    ]

    return {
        'flags': flags,
        'do_cache': True
    }
