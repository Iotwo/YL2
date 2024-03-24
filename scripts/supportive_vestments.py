from pygame.sprite import Group, GroupSingle, Sprite

from scripts.variables import CONTROLS, LOCAL_VARS, ERRORS


def create_sprite_groups() -> None:
    """
    """
    
    CONTROLS["obj_mgr"].add_new_sprite_group("mm_interface_cursor", GroupSingle())
    CONTROLS["obj_mgr"].add_new_sprite_group("mm_interface_buttons", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("mm_interface_bg", GroupSingle())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_bg", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_ground", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_walls", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_finish", GroupSingle())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_hero", GroupSingle())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_foes", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_projectiles_e", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_projectiles_h", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("gm_coins", Group())
    CONTROLS["obj_mgr"].add_new_sprite_group("sc_bg", GroupSingle())
    return None


def load_and_place_mm_sprites(res_dir:str) -> None:
    """
    """

    
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
    return None
