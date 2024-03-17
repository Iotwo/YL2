from pygame import event
from scripts.variables import CONTROLS, LOCAL_VARS, ERRORS
from classes.pg_gm_state_machine import PGGMStMachine
from classes.pg_gm_object_manager import PGObjMgr


class PGEvProc:
    """
        DESCR: PyGame event processor
    """
    def __init__(self,) -> None:
        super().__init__()
        CONTROLS["env"].log.debug(f"Экземпляр {self.__class__.__name__} "\
                                  f"по адресу {id(self)} инициализирован.")
        return None

    def __new__(cls, *args, **kwargs) -> object:
        instance = super().__new__(cls)
        instance.obj_mgr = None  # link to game object manager
        instance.gm_st_mn = None  # link to game state machine
        CONTROLS["env"].log.debug(f"Создан экземпляр {instance.__class__.__name__} "\
                                  f"по адресу {id(instance)}.")
        return instance


    def link_event_proc_to_object_mgr(self, obj_mgr_instance: PGObjMgr) -> int:
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод link_event_proc_to_object_mgr c аргументами: "\
                                  f"{obj_mgr_instance}::{type(obj_mgr_instance)}; ")
        self.obj_mgr = obj_mgr_instance

        CONTROLS["env"].log.debug(f"Error code: 0 - {ERRORS[0]}")
        LOCAL_VARS["last_err_code"] = 0
        CONTROLS["env"].log.info(f"Менеджер объектов {obj_mgr_instance}({id(obj_mgr_instance)}) привязан к экземпляру {self}.")
        return 0

    def link_event_proc_to_state_machine(self, st_machine_instance: PGGMStMachine) -> int:
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод link_event_proc_to_state_machine c аргументами: "\
                                  f"{st_machine_instance}::{type(st_machine_instance)}; ")
        self.gm_st_mn = st_machine_instance
        
        CONTROLS["env"].log.debug(f"Error code: 0 - {ERRORS[0]}")
        LOCAL_VARS["last_err_code"] = 0
        CONTROLS["env"].log.info(f"Машина состояний {st_machine_instance}({id(st_machine_instance)}) привязана к экземпляру {self}.")
        return 0

    def process_event_queue(self, events: list) -> None:
        for game_event in events:
            #CONTROLS["env"].log.debug(f"Случилось событие {game_event.type} -> {event.event_name(game_event.type)}.")
            if game_event.type == 1024:  # pygame.MOUSEMOTION
                # move cursor via iface manager
                self.obj_mgr.objs["menu_cursor"].update(game_event.pos)
            elif game_event.type == 768:  # pygame.KEYDOWN
                # can read: key, mod, unicode, scancode
                CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}: {game_event.key}, {game_event.mod}, \'{game_event.unicode}\', {game_event.scancode}.") 
                if game_event.scancode == 19:  # letter p, pause
                    CONTROLS["env"].log.info(f"|=>Letter p key pressed ({game_event.scancode}),")
                elif game_event.scancode == 41:  # if Esc key pressed, go back to main menu or exit
                    CONTROLS["env"].log.info(f"|=>Escape key pressed ({game_event.scancode}),")
                    if self.gm_st_mn.get_active_scene() == "MENU":
                        self.gm_st_mn.switch_game_state("ENDED")
                    elif self.gm_st_mn.get_active_scene() == "GAME":
                        self.gm_st_mn.switch_scene("MENU")
                elif game_event.scancode == 80:  # arrow left, move hero left
                    CONTROLS["env"].log.info(f"|=>Arrow left key pressed ({game_event.scancode}),")
                    self.obj_mgr.objs["hero"].set_cur_movement("LEFT")
                elif game_event.scancode == 82:  # arrow up
                    CONTROLS["env"].log.info(f"|=>Arrow up key pressed ({game_event.scancode}),")
                elif game_event.scancode == 79:  # arrow right, move hero right
                    CONTROLS["env"].log.info(f"|=>Arrow right key pressed ({game_event.scancode}),")
                    self.obj_mgr.objs["hero"].set_cur_movement("RIGHT")
                elif game_event.scancode == 81:  # arrow down
                    CONTROLS["env"].log.info(f"|=>Arrow down key pressed ({game_event.scancode}),")
                elif game_event.scancode == 44:  # space, move up and down
                    CONTROLS["env"].log.info(f"|=>Space key pressed ({game_event.scancode}),")
                    self.obj_mgr.objs["hero"].set_cur_action("JUMP")
                elif game_event.scancode == 224:  # left ctrl, make hero attac
                    CONTROLS["env"].log.info(f"|=>Left Ctrl key pressed ({game_event.scancode}),")
                    self.obj_mgr.objs["hero"].set_cur_action("ATTACK")
                else:
                    pass
            elif game_event.type == 769:  # pygame.KEYUP
                CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}: {game_event.key}, {game_event.mod}, \'{game_event.unicode}\', {game_event.scancode}.")
                if game_event.scancode == 19:  # letter p, pause
                    CONTROLS["env"].log.info(f"|=>Letter p key released ({game_event.scancode}),")
                elif game_event.scancode == 41:  # if Esc key pressed, go back to main menu
                    CONTROLS["env"].log.info(f"|=>Escape key released ({game_event.scancode}),")
                elif game_event.scancode == 80:  # arrow left, move hero left
                    CONTROLS["env"].log.info(f"|=>Arrow left key released ({game_event.scancode}),")
                    self.obj_mgr.objs["hero"].set_cur_movement("STOP")
                elif game_event.scancode == 82:  # arrow up
                    CONTROLS["env"].log.info(f"|=>Arrow up key released ({game_event.scancode}),")
                elif game_event.scancode == 79:  # arrow right, move hero right
                    CONTROLS["env"].log.info(f"|=>Arrow right key released ({game_event.scancode}),")
                    self.obj_mgr.objs["hero"].set_cur_movement("STOP")
                elif game_event.scancode == 81:  # arrow down
                    CONTROLS["env"].log.info(f"|=>Arrow down key released ({game_event.scancode}),")
                elif game_event.scancode == 44:  # space, move up and down
                    CONTROLS["env"].log.info(f"|=>Space key released ({game_event.scancode}),")
                    self.obj_mgr.objs["hero"].set_cur_action("STOP")
                elif game_event.scancode == 224:  # left ctrl, make hero attac
                    CONTROLS["env"].log.info(f"|>>Left Ctrl key released ({game_event.scancode}),")
                    self.obj_mgr.objs["hero"].set_cur_action("STOP")
                else:
                    pass
            elif game_event.type == 1025:  # pygame.MOUSEBUTTONDOWN
                # can read: pos, button, touch
                CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}: {game_event.button}, {game_event.pos}, {game_event.touch}")
                if self.gm_st_mn.get_active_scene() == "MENU":
                    self.obj_mgr.update_all_mm_buttons(game_event.pos, game_event.button)
                elif self.gm_st_mn.get_active_scene() == "SCORE":
                    pass
            elif game_event.type == 256:  # pygame.QUIT
                CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}.")
                self.gm_st_mn.switch_game_state("ENDED")
            elif game_event.type == 32787:  # pygame.WINDOWCLOSE
                CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}.")
                self.gm_st_mn.switch_game_state("ENDED")
        return None


    def process_event_queue_alt(self, events: list) -> None:
        """
            NOTE: might be faster than original
        """
        for game_event in events:
            if self.gm_st_mn.get_active_scene() == "MENU":
                if game_event.type == 1024:  # pygame.MOUSEMOTION
                    self.obj_mgr.objs["menu_cursor"].change_position(*game_event.pos)
                elif game_event.type == 768:  # pygame.KEYDOWN
                    CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}: {game_event.key}, {game_event.mod}, \'{game_event.unicode}\', {game_event.scancode}.") 
                    if game_event.scancode == 41:
                        self.gm_st_mn.switch_game_state("ENDED")
                elif game_event.type == 1025:  # pygame.MOUSEBUTTONDOWN
                    CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}: {game_event.button}, {game_event.pos}, {game_event.touch}")
                    self.obj_mgr.update_all_mm_buttons(game_event.pos, game_event.button)
            elif self.gm_st_mn.get_active_scene() == "GAME":
                if game_event.type == 768:  # pygame.KEYDOWN
                    CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}: {game_event.key}, {game_event.mod}, \'{game_event.unicode}\', {game_event.scancode}.") 
                    if game_event.scancode == 19:  # letter p, pause
                        CONTROLS["env"].log.info(f"|=>Letter p key pressed ({game_event.scancode}),")
                    elif game_event.scancode == 41:  # if Esc key pressed, go back to main menu or exit
                        CONTROLS["env"].log.info(f"|=>Escape key pressed ({game_event.scancode}),")
                        self.gm_st_mn.switch_scene("MENU")
                    elif game_event.scancode == 80:  # arrow left, move hero left
                        CONTROLS["env"].log.info(f"|=>Arrow left key pressed ({game_event.scancode}),")
                        self.obj_mgr.objs["hero"].set_cur_movement("LEFT")
                    elif game_event.scancode == 82:  # arrow up
                        CONTROLS["env"].log.info(f"|=>Arrow up key pressed ({game_event.scancode}),")
                    elif game_event.scancode == 79:  # arrow right, move hero right
                        CONTROLS["env"].log.info(f"|=>Arrow right key pressed ({game_event.scancode}),")
                        self.obj_mgr.objs["hero"].set_cur_movement("RIGHT")
                    elif game_event.scancode == 81:  # arrow down
                        CONTROLS["env"].log.info(f"|=>Arrow down key pressed ({game_event.scancode}),")
                    elif game_event.scancode == 44:  # space, move up and down
                        CONTROLS["env"].log.info(f"|=>Space key pressed ({game_event.scancode}),")
                        self.obj_mgr.objs["hero"].set_cur_action("JUMP")
                    elif game_event.scancode == 224:  # left ctrl, make hero attac
                        CONTROLS["env"].log.info(f"|=>Left Ctrl key pressed ({game_event.scancode}),")
                        self.obj_mgr.objs["hero"].set_cur_action("ATTACK")
                    else:
                        pass
                elif game_event.type == 769:  # pygame.KEYUP
                    CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}: {game_event.key}, {game_event.mod}, \'{game_event.unicode}\', {game_event.scancode}.") 
                    if game_event.scancode == 80:  # arrow left, move hero left
                        CONTROLS["env"].log.info(f"|=>Arrow left key released ({game_event.scancode}),")
                        self.obj_mgr.objs["hero"].set_cur_movement("STOP")
                    elif game_event.scancode == 82:  # arrow up
                        CONTROLS["env"].log.info(f"|=>Arrow up key released ({game_event.scancode}),")
                    elif game_event.scancode == 79:  # arrow right, move hero right
                        CONTROLS["env"].log.info(f"|=>Arrow right key released ({game_event.scancode}),")
                        self.obj_mgr.objs["hero"].set_cur_movement("STOP")
                    elif game_event.scancode == 81:  # arrow down
                        CONTROLS["env"].log.info(f"|=>Arrow down key released ({game_event.scancode}),")
                    elif game_event.scancode == 44:  # space, move up and down
                        CONTROLS["env"].log.info(f"|=>Space key released ({game_event.scancode}),")
                        self.obj_mgr.objs["hero"].set_cur_action("STOP")
                    elif game_event.scancode == 224:  # left ctrl, make hero attac
                        CONTROLS["env"].log.info(f"|>>Left Ctrl key released ({game_event.scancode}),")
                        self.obj_mgr.objs["hero"].set_cur_action("STOP")
                    else:
                        pass
            elif self.gm_st_mn.get_current_state() == "PAUSE":
                if game_event.type == 1024:  # pygame.MOUSEMOTION
                    self.obj_mgr.objs["menu_cursor"].change_position(*game_event.pos)
                elif game_event.type == 768:  # pygame.KEYDOWN
                    CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}: {game_event.key}, {game_event.mod}, \'{game_event.unicode}\', {game_event.scancode}.") 
                    if game_event.scancode == 41:
                        self.gm_st_mn.switch_game_state("ENDED")
                elif game_event.type == 1025:  # pygame.MOUSEBUTTONDOWN
                    CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}: {game_event.button}, {game_event.pos}, {game_event.touch}")
            elif self.gm_st_mn.get_active_scene() == "SCORE":
                if game_event.type == 1024:  # pygame.MOUSEMOTION
                    self.obj_mgr.objs["menu_cursor"].change_position(*game_event.pos)
                elif game_event.type == 768:  # pygame.KEYDOWN
                    CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}: {game_event.key}, {game_event.mod}, \'{game_event.unicode}\', {game_event.scancode}.") 
                    if game_event.scancode == 41:
                        CONTROLS["env"].log.info(f"|=>Escape key pressed ({game_event.scancode}),")
                        self.gm_st_mn.switch_game_state("ENDED")
                elif game_event.type == 1025:  # pygame.MOUSEBUTTONDOWN
                    CONTROLS["env"].log.info(f"|>{event.event_name(game_event.type)}: {game_event.button}, {game_event.pos}, {game_event.touch}")
            else:
                pass

        return None
        
