#############################################
# File with constants and control parameters.
#############################################

LOCAL_VARS = {
    "conf_path": "./config.cfg",
    "last_err_code": 0,
    "level_patterns_dir": "",
    "log_dir": "./logs/",
    "pg_game_settings_global_fps": 30,
    "pg_game_settings_global_velocity": 1,
    "pg_modules_init_ok_cnt": 0,
    "pg_modules_init_err_cnt": 0,
    "pg_level_height": 0,
    "pg_level_width": 0,
    "pg_screen_height": 0,
    "pg_screen_width": 0,
    "scores_total": 0,
    "sprites_dir": "",
    }

CONTROLS = {
    "env": None,
    "ev_proc": None,
    "game_screen": None,
    "global_clock": None,
    "gm_cam": None,
    "obj_mgr": None,
    "object_sprites": None,
    "st_mchn": None,
}

ERRORS = {
    0: "OK",
    1: "File not found.",
    2: "Not enough permissions in file system.",
    4: "Incorrect config value.",
    5: "Cannot ininitate PyGame properly",
    10: "Object already exist in object manager",
    20: "Sprite group already exist in object manager",
    21: "No such sprite group in object manager",
    50: "Game already in desired state",
    51: "State does not exist",
    55: "Scene already loaded",
    56: "Scene does not exist",
    60: "No such movement variant available",
    61: "No such action variant available",
    
    255: "General error."
}
