from .base import *
import os

if os.environ['ENV'] == 'dev':
    from .local import *
    print('está no LOCAL')
    print('DEBUG: ', DEBUG)

else:
    print('está no PROD')
    print('DEBUG: ', DEBUG)
    from .production import *


