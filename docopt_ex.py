#! usr/bin/env python
#! coding:utf-8

"""docopt_ex
Usage:
    python docopt_ex.py -a <x> -b <y>

    Options:
        -h --help  show this screen
        -a
        -b
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__,version='docopt_ex 1.0')
    print(argument)
