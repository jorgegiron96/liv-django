from .base import *
import os


try:
    if os.environ['ENV'] == 'dev':
        from .local import *
        print('está no LOCAL')
        print('DEBUG:', DEBUG)
except:
    
    from .production import *
    print('está no PROD')
    print('DEBUG: ', DEBUG)
    


