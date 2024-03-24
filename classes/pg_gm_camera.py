from scripts.variables import CONTROLS, LOCAL_VARS, ERRORS


class PGGMCamera():
    """
        DESCR: basic game object class for this game
    """
    def __init__(self,) -> None:

        self.dx = 0
        self.dy = 0
        CONTROLS["env"].log.debug(f"Экземпляр {self.__class__.__name__} "\
                                  f"по адресу {id(self)} инициализирован.")
        return None

    def __new__(cls, *args, **kwargs) -> object:
        instance = super().__new__(cls)
        instance.dx = None
        instance.dy = None
        CONTROLS["env"].log.debug(f"Создан экземпляр {instance.__class__.__name__} "\
                                  f"по адресу {id(instance)}.")
        return instance

    def __del__(self) -> None:
        CONTROLS["env"].log.debug(f"Экземпляр {self.__class__.__name__} "\
                                  f"по адресу {id(instance)} помечен на удаление.")
        super().__del__()
        return None
    

    def update_pos(self, obj) -> None:
        obj.rect.x += self.dx
        #obj.rect.y += self.dy
        
        return None
    
    def follow(self, target) -> None:
        self.dx = -(target.rect.x + target.rect.w // 2 - LOCAL_VARS["pg_screen_width"] // 2)
        #self.dy = -(target.rect.y + target.rect.h // 2 - LOCAL_VARS["pg_screen_height"] // 2)
        
        return None
