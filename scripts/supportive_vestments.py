from pygame.sprite import Group, GroupSingle, Sprite

from scripts.variables import CONTROLS, LOCAL_VARS, ERRORS
from classes.pg_gm_state_machine import PGGMStMachine
from classes.pg_gm_object_manager import PGObjMgr
from classes.pg_event_processor import PGEvProc
from classes.go_cursor import GOCursor
from classes.go_menu_btn_ng import GOMenuButtonNewGame
from classes.go_menu_btn_exit import GOMenuButtonExit
from classes.go_unit import GOUnit
from classes.go_obstacle import GOObstacle


def load_game_resources(res_dir: str) -> None:
    """
    """
    CONTROLS["obj_mgr"].add_new_sprite_group("mm_interface_cursor", GroupSingle())
    CONTROLS["obj_mgr"].add_new_sprite_group("mm_interface_buttons", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("mm_interface_bg", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_bg", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_ground", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_walls", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_hero", GroupSingle())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_foes", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_projectiles_e", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_projectiles_h", Group())
    
    CONTROLS["obj_mgr"].add_new_gm_object("menu_bg",
                                          GOCursor(f"{res_dir}/interface/mm_bg.bmp",
                                                   CONTROLS["obj_mgr"].sprt_grp["mm_interface_bg"]),
                                          "mm_interface_bg")
    CONTROLS["obj_mgr"].add_new_gm_object("menu_cursor",
                                          GOCursor(f"{res_dir}/interface/cursor.png",
                                                   CONTROLS["obj_mgr"].sprt_grp["mm_interface_cursor"]),
                                          "mm_interface_cursor")
    CONTROLS["obj_mgr"].add_new_gm_object("ng_btn",
                                          GOMenuButtonNewGame(f"{res_dir}/interface/newgame.bmp",
                                                              (175, 50,),
                                                              CONTROLS["obj_mgr"].sprt_grp["mm_interface_buttons"]),
                                          "mm_interface_buttons")
    CONTROLS["obj_mgr"].add_new_gm_object("exit_btn",
                                          GOMenuButtonExit(f"{res_dir}/interface/exitgame.bmp",
                                                              (175, 150,),
                                                              CONTROLS["obj_mgr"].sprt_grp["mm_interface_buttons"]),
                                          "mm_interface_buttons")
    CONTROLS["obj_mgr"].add_new_gm_object("bg",
                                          GOObstacle(f"{res_dir}/levels/level_bg.png",
                                                     (0, 0),
                                                     CONTROLS["obj_mgr"].sprt_grp["gm_bg"]),
                                          "gm_bg")
    CONTROLS["obj_mgr"].add_new_gm_object("plant",
                                          GOObstacle(f"{res_dir}/levels/plant_big.png",
                                                     (0, 224),
                                                     CONTROLS["obj_mgr"].sprt_grp["gm_walls"]),
                                          "gm_walls")
    CONTROLS["obj_mgr"].add_new_gm_object("ground",
                                          GOObstacle(f"{res_dir}/levels/ground2.png",
                                                     (192, 464),
                                                     CONTROLS["obj_mgr"].sprt_grp["gm_ground"]),
                                          "gm_ground")
    CONTROLS["obj_mgr"].add_new_gm_object("hero",
                                          GOUnit(f"{res_dir}/hero/hero_full_tile.png",
                                                 (256, 460,),
                                                 LOCAL_VARS["pg_game_settings_global_velocity"],
                                                 CONTROLS["obj_mgr"].sprt_grp["gm_hero"],),
                                          "gm_hero",)
    
    return None
