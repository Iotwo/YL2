from pygame import image

from classes.go_basic import GOBasicIface
from scripts.variables import CONTROLS, LOCAL_VARS, ERRORS


class GOCursor(GOBasicIface):
    """
    """
    def __init__(self, pic_path, *group) -> None:
        super().__init__(*group)
        self.image = image.load(pic_path).convert_alpha()
        self.rect = self.image.get_rect()
        return None
    
    def __new__(cls, *args, **kwargs) -> object:
        instance = super().__new__(cls)
        instance.center_x = None
        instance.center_y = None
        instance.left_x = None
        instance.left_y = None
        return instance


    def change_position(self, new_x, new_y) -> None:
        self.rect.x, self.rect.y = new_x, new_y
    
    def update(self, *args) -> None:
        return None
