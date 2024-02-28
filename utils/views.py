import inspect
from utils.models import ErrorsManage

def handleError(name, error):
  stack = inspect.stack()
  function_call = stack[1].function
  try:    
    error = ErrorsManage.objects.get(name=name)
    raise ValueError(error.message) 
  except:
    message = str(function_call) + "-" +str(error)
    raise ValueError(message)
  
    