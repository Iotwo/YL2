from pygame import image

from classes.go_basic import GOBasicIface
from scripts.variables import LOCAL_VARS


class GOObject(GOBasicIface):
    """
    """
    def __init__(self, pic_path, position:tuple, *group) -> None:
        super().__init__(*group)
        self.image = image.load(pic_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        return None
    
    def __new__(cls, *args, **kwargs) -> object:
        instance = super().__new__(cls)
        instance.center_x = None
        instance.center_y = None
        instance.left_x = None
        instance.left_y = None
        instance.is_visible = None
        return instance


    def update(self, *args) -> None:        
        return None
