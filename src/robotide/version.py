# Automatically generated by 'package.py' script.

VERSION = '0.28'
RELEASE = 'final'
TIMESTAMP = '20100923-123313'

def get_version(sep=' '):
    if RELEASE == 'final':
        return VERSION
    return VERSION + sep + RELEASE

if __name__ == '__main__':
    import sys
    print get_version(*sys.argv[1:])
