from functools import wraps
from scripts.variables import CONTROLS

# I cannot use wrapper that adresses objects unfortunatelly
def execution_wrapper(method):
    if CONTROLS is not None:
        CONTROLS["env"].log.debug(f"Вызван метод {method.__name__} по адресу {id(method)}.")
        @wraps(method)
        def wrapper(*args, **kwargs):
            CONTROLS["env"].log.debug(f"В метод переданы аргументы: {args}, {kwargs} .")
            result = method(*args, **kwargs)
            CONTROLS["env"].log.debug(f"Метод вернул результат: {result} по адресу {id(result)}.")
            return result
        return wrapper
