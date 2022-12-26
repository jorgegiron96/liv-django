from .base import *
import os

try:
    if os.environ['ENV'] == 'dev':
        from .local import *
        print('está no LOCAL')
        print('DEBUG: ', DEBUG)
except:
    print('está no PROD')
    print('DEBUG: ', DEBUG)
    from .production import *


