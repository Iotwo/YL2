from pygame import image

from classes.go_object import GOObject
from scripts.variables import LOCAL_VARS


class GOObstacle(GOObject):
    """
    """
    def __init__(self, pic_path, position:tuple, *group) -> None:
        super().__init__(pic_path, position, *group)
        self.is_solid_touched = False
        
        return None
    
    def __new__(cls, *args, **kwargs) -> object:
        instance = super().__new__(cls, *args, **kwargs)
        instance.is_solid_touched = None
        return instance


    def update(self, *args) -> None:
        
        return None
