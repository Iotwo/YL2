from pygame.sprite import Sprite
from pygame import image

from scripts.variables import CONTROLS, LOCAL_VARS, ERRORS


class GOBasicIface(Sprite):
    """
        DESCR: basic game object class for this game
    """
    def __init__(self, *group) -> None:
        super().__init__(*group)
        CONTROLS["env"].log.debug(f"Экземпляр {self.__class__.__name__} "\
                                  f"по адресу {id(self)} инициализирован.")
        return None

    def __new__(cls, *args, **kwargs) -> object:
        instance = super().__new__(cls)
        CONTROLS["env"].log.debug(f"Создан экземпляр {instance.__class__.__name__} "\
                                  f"по адресу {id(instance)}.")
        return instance

    def __del__(self) -> None:
        CONTROLS["env"].log.debug(f"Экземпляр {self.__class__.__name__} "\
                                  f"по адресу {id(self)} помечен на удаление.")
        #super().__del__()
        return None


    def load_image(pic_path, colorkey=None):
        pic = image.load(pic_path)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = pic.get_at((0, 0))
            pic.set_colorkey(colorkey)
        else:
            pic = pic.convert_alpha()
            
        return pic

    def update(self, *args) -> None:
        return None
