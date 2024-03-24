from pygame.sprite import Group, GroupSingle, Sprite
from pygame import sprite
from pygame import Surface
from pygame import font
from scripts.variables import CONTROLS, LOCAL_VARS, ERRORS
from classes.pg_gm_camera import PGGMCamera


class PGObjMgr:
    """
        DESCR: PyGame game object manager
    """
    def __init__(self,) -> None:
        super().__init__()
        self.objs = {}
        self.sprt_grp = {}
        CONTROLS["env"].log.debug(f"Экземпляр {self.__class__.__name__} "\
                                  f"по адресу {id(self)} инициализирован.")
        return None

    def __new__(cls, *args, **kwargs) -> object:
        instance = super().__new__(cls)
        instance.cam = None
        instance.objs = None
        instance.sprt_grp = None
        CONTROLS["env"].log.debug(f"Создан экземпляр {instance.__class__.__name__} "\
                                  f"по адресу {id(instance)}.")
        return instance


    def add_new_gm_object(self, obj_name: str, obj_instance: Sprite, obj_group_name: str) -> int:
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод add_new_gm_object c аргументами: "\
                                  f"{obj_name}::{type(obj_name)}; "\
                                  f"{obj_instance}::{type(obj_instance)}; "\
                                  f"{obj_group_name}::{type(obj_group_name)}.")
        if obj_name in self.objs.keys():
            CONTROLS["env"].log.warn(f"Error code: 10 - {ERRORS[10]}")
            LOCAL_VARS["last_err_code"] = 10
            return 10
        if obj_group_name not in self.sprt_grp.keys():
            CONTROLS["env"].log.warn(f"Error code: 21 - {ERRORS[21]}")
            LOCAL_VARS["last_err_code"] = 21
            return 21
        self.objs[obj_name] = obj_instance

        CONTROLS["env"].log.debug(f"Error code: 0 - {ERRORS[0]}")
        LOCAL_VARS["last_err_code"] = 0
        CONTROLS["env"].log.info(f"Добавлен объект - {obj_name} - в группу спрайтов {obj_group_name}.")
        return 0
    
    def add_new_sprite_group(self, group_name: str, group: Group) -> int:
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод add_new_sprite_group c аргументами "\
                                  f"{group_name}::{type(group_name)};" \
                                  f"{group}::{type(group)}.")
        if group_name in self.sprt_grp:
            CONTROLS["env"].log.warn(f"Error code: 20 - {ERRORS[20]}")
            LOCAL_VARS["last_err_code"] = 20
            return 20
        self.sprt_grp[group_name] = group

        CONTROLS["env"].log.debug(f"Error code: 0 - {ERRORS[0]}")
        LOCAL_VARS["last_err_code"] = 0
        CONTROLS["env"].log.info(f"Добавлена группа спрайтов - {group_name}.")
        return 0


    def detect_collision_hero_X_map(self) -> None:
        """
            DESCR: detect collision between hero and map
                   change hero state according to collision result
        """
        clsn_map = sprite.spritecollideany(self.objs["hero"], self.sprt_grp["gm_ground"])
        if clsn_map is not None:
            self.objs["hero"].set_falling(False)
            self.objs["hero"].rect.bottom = clsn_map.rect.top + 1
        else:
            self.objs["hero"].set_falling(True)
        clsn_map = sprite.spritecollideany(self.objs["hero"], self.sprt_grp["gm_walls"])
        if clsn_map is not None:
            if self.objs["hero"].rect.bottom - clsn_map.rect.top <= 2:
                self.objs["hero"].set_falling(False)
            elif abs(clsn_map.rect.right - self.objs["hero"].rect.left) <= 2:
                self.objs["hero"].set_cur_movement("STOP")
                self.objs["hero"].move_right()
            elif abs(clsn_map.rect.left - self.objs["hero"].rect.right) <= 2:
                self.objs["hero"].set_cur_movement("STOP")
                self.objs["hero"].move_left()

        return None

    def detect_collision_hero_X_coins(self) -> None:
        """
        """
        clsn_map = sprite.spritecollideany(self.objs["hero"], self.sprt_grp["gm_coins"])
        if clsn_map is not None:
            LOCAL_VARS["scores_total"] += 10
            clsn_map.kill()
            CONTROLS["env"].log.debug(f"У Экземпляра {clsn_map.__class__.__name__} по адресу {id(clsn_map)} "\
                                      f"произошла коллизия.")
            CONTROLS["env"].log.debug(f"Значение счётчика очков - {LOCAL_VARS['scores_total']}.")

        return None

    def exec_camera_follow(self, camera: PGGMCamera) -> None:
        for obj in self.objs.keys():
            if (self.objs[obj] in self.sprt_grp["gm_ground"].sprites()
                or self.objs[obj] in self.sprt_grp["gm_walls"].sprites()
                or self.objs[obj] in self.sprt_grp["gm_hero"].sprites()
                or self.objs[obj] in self.sprt_grp["gm_foes"].sprites()
                or self.objs[obj] in self.sprt_grp["gm_coins"].sprites()
                or self.objs[obj] in self.sprt_grp["gm_projectiles_e"].sprites()
                or self.objs[obj] in self.sprt_grp["gm_projectiles_h"].sprites()):
                camera.update_pos(self.objs[obj])
                
        return None
        
    def exec_draw_all_gm_interface(self, screen: Surface) -> None:
        self.sprt_grp["gm_bg"].draw(screen)
        self.sprt_grp["gm_walls"].draw(screen)
        self.sprt_grp["gm_ground"].draw(screen)
        self.sprt_grp["gm_hero"].draw(screen)
        self.sprt_grp["gm_foes"].draw(screen)
        self.sprt_grp["gm_coins"].draw(screen)
        self.sprt_grp["gm_projectiles_e"].draw(screen)
        self.sprt_grp["gm_projectiles_h"].draw(screen)

        text_f = font.Font(None, 50)
        text = text_f.render(f"Очки: {LOCAL_VARS['scores_total']}", True, (100, 255, 100))
        screen.blit(text, (10, 10,))
        return None

    def exec_draw_all_mm_interface(self, screen: Surface) -> None:
        self.sprt_grp["mm_interface_bg"].draw(screen)
        self.sprt_grp["mm_interface_buttons"].draw(screen)
        self.sprt_grp["mm_interface_cursor"].draw(screen)
        return None

    def exec_draw_all_score_interface(self) -> None:
        return None

    def list_objects(self) -> None:
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод list_sprite_groups.")
        CONTROLS["env"].log.info(f"Перечисление объектов в менеджере {self.__class__.__name__}({id(self)}): "\
                                 f"{';'.join([key + '=' + str(val) for key, val in self.objs.items()])}") 
        return None

    def list_sprite_groups(self) -> None:
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод list_sprite_groups.")
        CONTROLS["env"].log.info(f"Перечисление групп спрайтов в менеджере {self.__class__.__name__}({id(self)}): "\
                                 f"{';'.join([key + '=' + str(val) for key, val in self.sprt_grp.items()])}")
        return None

    def redraw_all_active_objects(self, game_screen) -> None:
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод switch_game_state c аргументами "\
                                  f"{game_screen}::{type(game_screen)}.")
        for obj in self.objs.values():
            obj.draw(game_screen)

        return None

    def update_all_gm_objects(self, *args) -> None:
        
        return None

    def update_all_mm_buttons(self, *args) -> None:
        self.sprt_grp["mm_interface_buttons"].update(*args)
        
        return None

    def update_mm_crusor(self, *args) -> None:
        self.sprt_grp["mm_interface_cursor"].update(*args)

        return None

    def update_all_score_buttons(self) -> None:
        return None
