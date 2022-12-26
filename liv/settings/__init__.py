from .base import *
import os


try:
    if os.environ['ENV'] == 'dev':
        from .local import *
        from .local import DEBUG
        print('está no LOCAL')
        print('DEBUG:', DEBUG)
except:
    
    from .production import *
    from .production import DEBUG
    print('está no PROD')
    print('DEBUG: ', DEBUG)
    


