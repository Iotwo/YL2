### x_pos += v * clock.tick() / 1000  # v * t в секундах


import logging
import sys
from os import (getcwd, path)

import pygame

from scripts.variables import CONTROLS, LOCAL_VARS, ERRORS
from scripts.supportive_vestments import load_game_sprites  # rewrite
from classes.environment import Environment
from classes.pg_gm_state_machine import PGGMStMachine
from classes.pg_gm_object_manager import PGObjMgr
from classes.pg_event_processor import PGEvProc
from classes.go_cursor import GOCursor
from classes.go_menu_btn_ng import GOMenuButtonNewGame
from classes.go_menu_btn_exit import GOMenuButtonExit
from classes.go_unit import GOUnit
from classes.pg_gm_camera import PGGMCamera


if __name__ == "__main__":
    CONTROLS["env"] = Environment()
    CONTROLS["env"].create_base_dirs()
    CONTROLS["env"].initiate_log_file()
    CONTROLS["env"].enumerate_errcodes()
    CONTROLS["env"].load_config_from_file()

    CONTROLS["env"].log.info("Инициализация PyGame...")
    LOCAL_VARS["pg_modules_init_ok_cnt"], LOCAL_VARS["pg_modules_init_err_cnt"] = pygame.init()
    if LOCAL_VARS["pg_modules_init_err_cnt"] != 0:
        CONTROLS["env"].log.debug(f"Error code: 5 - {ERRORS[5]}")
        CONTROLS["env"].log.critical("Не удалось корректно запустить все модули PyGame!")
        pygame.quit()
        sys.exit()
    scr_size = (LOCAL_VARS["pg_screen_width"], LOCAL_VARS["pg_screen_height"],)
    CONTROLS["game_screen"] = pygame.display.set_mode(scr_size)
    pygame.display.set_caption("Batya's going home")
    CONTROLS["global_clock"] = pygame.time.Clock()
    CONTROLS["st_mchn"] = PGGMStMachine()
    CONTROLS["obj_mgr"] = PGObjMgr()
    CONTROLS["ev_proc"] = PGEvProc()
    CONTROLS["gm_cam"] = PGGMCamera()
    CONTROLS["env"].log.info("Загрузка игровых ресурсов...")
    CONTROLS["ev_proc"].link_event_proc_to_object_mgr(CONTROLS["obj_mgr"])
    CONTROLS["ev_proc"].link_event_proc_to_state_machine(CONTROLS["st_mchn"])
    load_game_sprites(LOCAL_VARS["sprites_dir"])
    CONTROLS["obj_mgr"].list_sprite_groups()
    CONTROLS["obj_mgr"].list_objects()
    pygame.mouse.set_visible(False)
    CONTROLS["env"].log.debug("Курсор мыши скрыт.")
    
    
    CONTROLS["st_mchn"].switch_game_state("RUNNING")
    CONTROLS["env"].log.info("Запущен основной игровой цикл.")
    while CONTROLS["st_mchn"].get_current_state() in ["RUNNING", "PAUSED"]:
        if CONTROLS["st_mchn"].get_current_state() == "RUNNING":  # running
            CONTROLS["ev_proc"].process_event_queue_alt(pygame.event.get())
        else:  # paused
            pass

        # UPDATE STATES (collisions, etc)
        if CONTROLS["st_mchn"].get_active_scene() == "MENU":
            CONTROLS["obj_mgr"].update_mm_crusor()
        elif CONTROLS["st_mchn"].get_active_scene() == "GAME":
            CONTROLS["gm_cam"].follow(CONTROLS["obj_mgr"].objs["hero"])
            CONTROLS["obj_mgr"].exec_camera_follow(CONTROLS["gm_cam"])
            CONTROLS["obj_mgr"].detect_collision_hero_X_map()
            CONTROLS["obj_mgr"].objs["hero"].update()
            # also update camera position
        elif CONTROLS["st_mchn"].get_active_scene() == "SCORE":
            pass
        
        # GRAPHIC DRAWING
        if CONTROLS["st_mchn"].get_active_scene() == "MENU":
            # draw only menu things            
            CONTROLS["game_screen"].fill(pygame.Color("blue")) # chagne with bg sprite
            CONTROLS["obj_mgr"].exec_draw_all_mm_interface(CONTROLS["game_screen"])
        elif CONTROLS["st_mchn"].get_active_scene() == "GAME":  
            # draw only game things
            # CONTROLS["game_screen"].fill(pygame.Color("green"))
            CONTROLS["obj_mgr"].exec_draw_all_gm_interface(CONTROLS["game_screen"])
        elif CONTROLS["st_mchn"].get_active_scene() == "SCORE":
            # draw scores
            CONTROLS["game_screen"].fill(pygame.Color("yellow"))
        else:
            pass

        if pygame.mouse.get_focused():
            pass
        else:
            pass

        # FLIP'n'TICK
        CONTROLS["global_clock"].tick(LOCAL_VARS["pg_game_settings_global_fps"])
        pygame.display.flip()

    pygame.quit()
    CONTROLS["env"].log.info(f"Работа PyGame завершена, выход из приложения...")
    
    CONTROLS["env"].log.debug(f"LOCAL_VARS")
    CONTROLS["env"].log.debug(f"{';'.join(['='.join((str(key), str(val),)) for key, val in LOCAL_VARS.items()])}")
    CONTROLS["env"].log.info("Запись завершена. Освобождение ресурсов самописца.")
    CONTROLS["env"].stop_logging()
    sys.exit(LOCAL_VARS['last_err_code'])
