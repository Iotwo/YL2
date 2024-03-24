from pygame import image

from classes.go_basic import GOBasicIface
from scripts.variables import LOCAL_VARS, CONTROLS


class GOLevelFinish(GOBasicIface):
    """
    """
    def __init__(self, pic_path, position:tuple, *group) -> None:
        super().__init__(*group)
        self.image = image.load(pic_path).convert_alpha()
        self.is_touched = False
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
        instance.is_touched = None
        return instance


    def set_touched(self,touch: bool) -> None:
        self.is_touched = touch
        return None

    def update(self, *args) -> None:
        if self.is_touched is True:
            CONTROLS["st_mchn"].switch_scene("SCORE")
        return None
