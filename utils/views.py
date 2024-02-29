import inspect
from utils.models import ErrorsManage
import re

def handleError(name, error):
  stack = inspect.stack()
  function_call = stack[1].function
  try:    
    error = ErrorsManage.objects.get(name=name)
    raise ValueError(error.message) 
  except:
    message = str(function_call) + "-" +str(error)
    raise ValueError(message)
  

def validate_address(address):
    regex = r'^0x[a-fA-F0-9]{40}$'
        # Validar el formato del hash utilizando expresiones regulares
    return re.match(regex, address)