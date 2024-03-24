from scripts.variables import CONTROLS, LOCAL_VARS, ERRORS


class PGGMStMachine:
    """
        DESCR: PyGame game state machine
    """
    def __init__(self,) -> None:
        super().__init__()
        self.av_scenes = ["MENU", "GAME", "SCORE"]
        self.curr_scene = "MENU"
        self.gm_curr_state = "NOT_SET"
        self.gm_states = ["NOT SET", "RUNNING", "PAUSED", "ENDED"]
        
        CONTROLS["env"].log.debug(f"Экземпляр {self.__class__.__name__} "\
                                  f"по адресу {id(self)} инициализирован.")
        CONTROLS["env"].log.info(f"Текущее состояние игры: {self.gm_curr_state}; текущая сцена: {self.curr_scene}")
        return None

    def __new__(cls, *args, **kwargs) -> object:
        instance = super().__new__(cls)
        instance.gm_states = None
        instance.gm_curr_state = None
        instance.av_scenes = None
        instance.curr_scene = None
        CONTROLS["env"].log.debug(f"Создан экземпляр {instance.__class__.__name__} "\
                                  f"по адресу {id(instance)}.")
        return instance


    def get_active_scene(self) -> str:
        return self.curr_scene

    def get_current_state(self) -> str:
        return self.gm_curr_state
    
    def switch_game_state(self, new_state: str) -> int:
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод switch_game_state c аргументами "\
                                  f"{new_state}::{type(new_state)}.")
        if new_state == self.gm_curr_state:
            CONTROLS["env"].log.warn(f"Error code: 50 - {ERRORS[50]}")
            LOCAL_VARS["last_err_code"] = 50
            return 50
        if new_state not in self.gm_states:
            CONTROLS["env"].log.warn(f"Error code: 51 - {ERRORS[51]}")
            LOCAL_VARS["last_err_code"] = 51
            return 51
        self.gm_curr_state = new_state
        
        CONTROLS["env"].log.debug(f"Error code: 0 - {ERRORS[0]}")
        LOCAL_VARS["last_err_code"] = 0
        CONTROLS["env"].log.info(f"Текущее состояние изменено на {new_state}.")
        return 0

    def switch_scene(self, new_scene: str) -> int:
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод switch_scene c аргументами "\
                                  f"{new_scene}::{type(new_scene)}.")
        if new_scene == self.curr_scene:
            CONTROLS["env"].log.warn(f"Error code: 55 - {ERRORS[55]}")
            LOCAL_VARS["last_err_code"] = 55
            return 55
        if new_scene not in self.av_scenes:
            CONTROLS["env"].log.warn(f"Error code: 56 - {ERRORS[56]}")
            LOCAL_VARS["last_err_code"] = 56
            return 56
        self.curr_scene = new_scene
        if self.curr_scene == "GAME":
            LOCAL_VARS["scores_total"] = 0
        
        CONTROLS["env"].log.debug(f"Error code: 0 - {ERRORS[0]}")
        LOCAL_VARS["last_err_code"] = 0
        CONTROLS["env"].log.info(f"Текущая сцена изменена на {new_scene}.")
        return 0
        
