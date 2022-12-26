from .base import *
import os

if os.environ['ENV'] == 'dev':
    from .local import *
    print('startando local')
 
    DEBUG = True

else:
    print('está no PROD')

    DEBUG = False
    from .production import *


