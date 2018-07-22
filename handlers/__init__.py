from os import listdir
__all__ = [fn[:-3] for fn in listdir('handlers') if fn.endswith('.py') and fn != '__init__.py' and fn[0] not in '#.']
