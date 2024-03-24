import datetime
from functools import wraps
import logging
from os import getcwd, mkdir, path


from scripts.variables import LOCAL_VARS, CONTROLS, ERRORS


class Environment(object):
    """
    DESCR: this class describes interaction between the main program and files in OS
    """

    def __new__(cls, *args, **kwargs) -> object:
        instance = super().__new__(cls)
        instance.log = None
        
        return instance

    def __init__(self) -> None:
        return None


    def create_base_dirs(self,) -> None:
        """
        DESCR: Create base working directories (for dynamic files)
        """
        if path.exists(getcwd() + "\\logs") is False:
            mkdir(getcwd() + "\\logs")

        return None

    def enumerate_errcodes(self) -> None:
        CONTROLS["env"].log.debug(f"Перечисление кодов ошибок:")
        CONTROLS["env"].log.debug(f"{';'.join(['='.join((str(key), str(val),)) for key, val in ERRORS.items()])}")
        return None
    
    def initiate_log_file(self) -> None:
        """
        DESCR: Initiate logger and log-file to write program progress 
        """
        logger_name = f"Y2_{datetime.datetime.now().date()}_app.log"
        with open(file=f"{LOCAL_VARS['log_dir']}{logger_name}", mode='a', encoding="utf-8") as f:
            f.write("")
            f.flush()
        
        logging.basicConfig(filename=f".\\logs\\Y2_{datetime.datetime.now().date()}_app.log",
                            filemode='a', level=logging.DEBUG,datefmt="%H:%M:%S", 
                            format="%(asctime)s.%(msecs)d %(name)s %(levelname)s %(message)s",)
        self.log = logging.getLogger("general_logger")

        CONTROLS["env"].log.info("===========================================")
        CONTROLS["env"].log.info("Запись начата.")
        CONTROLS["env"].log.info("===========================================")

        return None
 
    def initiate_default_config(self) -> None:
        return None

    def load_and_place_mm_sprites(self, res_dir:str) -> int:
        """
            DESCR: load sprites for main menu and place them in order
            ARGS:
                * res_dir: directory of sprites
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

    def load_and_place_level_1(self, res_dir:str, lvl_map_path: str) -> int:
        """
            DECR: Temprorary method for level loading. Env class must ONLY load resources
        """
        STEP = 32
        LVL_WIDTH = 1280
        LVL_HEIGHT = 480
        CONTROLS["env"].log.debug(f"Шаг компоновки уровня - {STEP} пикселя.")
        lvl_mapping = ['*', 'P', 'G', 'B', 'C', 'F', 'H']
        level = None
        CONTROLS["env"].log.info(f"Загрузка паттерна уровня из директории - {lvl_map_path}...")
        try:
            lvl = open(file=f"", mode='r', encoding="utf-8")
        except Exception as ex:
            CONTROLS["env"].log.debug(f"Error code: 1 - {ERRORS[1]}")
            LOCAL_VARS["last_err_code"] = 1
            CONTROLS["env"].log.error("Не удалось загрузить паттерн уровня.")
            CONTROLS["env"].log.debug(f"Raw exception data: {ex.__str__()}")
            return 2
        CONTROLS["env"].log.info(f"Файл паттерна открыт, загрузка уровня.")
        level = [line.strip() for line in lvl.read().split('\n')]
        CONTROLS["env"].log.debug(f"Состав паттерна: \n{'\n\t\t'.join([''.join(line) for line in level])}")
        lvl.close()
        #level building
        CONTROLS["obj_mgr"].add_new_gm_object("bg",
                                              GOObstacle(f"{res_dir}/levels/level_bg.png",
                                                         (0, 0),
                                                         CONTROLS["obj_mgr"].sprt_grp["gm_bg"]),
                                              "gm_bg")
        for i in range(len(level)):
            for j in range(len(level[i])):
                if level[i][j] == '*':  # free space
                    pass
                elif level[i][j] == 'B':  # palce box
                    CONTROLS["obj_mgr"].add_new_gm_object(f"box_{i * len(level[i]) + j}",
                                                          GOObstacle(f"{res_dir}/levels/box.bmp",
                                                                     (LVL_WIDTH - STEP * j, LVL_HEIGHT - STEP * i),
                                                                     CONTROLS["obj_mgr"].sprt_grp["gm_walls"]),
                                                          "gm_walls")
                elif level[i][j] == 'C':  # place coin
                    pass
                elif level[i][j] == 'H':  # place Hero
                    CONTROLS["obj_mgr"].add_new_gm_object("hero",
                                          GOUnit(f"{res_dir}/hero/hero_full_tile.png",
                                                 (LVL_WIDTH - STEP * j, LVL_HEIGHT - STEP * i),
                                                 LOCAL_VARS["pg_game_settings_global_velocity"],
                                                 CONTROLS["obj_mgr"].sprt_grp["gm_hero"],),
                                          "gm_hero",)
                elif level[i][j] == 'P':  # place plant - special
                    CONTROLS["obj_mgr"].add_new_gm_object("plant",
                                                          GOObstacle(f"{res_dir}/levels/plant_big.png",
                                                                     (0, 224),
                                                                     CONTROLS["obj_mgr"].sprt_grp["gm_walls"]),
                                                          "gm_walls")
                elif level[i][j] == 'G':  # place ground - special
                    CONTROLS["obj_mgr"].add_new_gm_object("ground",
                                                          GOObstacle(f"{res_dir}/levels/ground2.png",
                                                                     (192, 464),
                                                                     CONTROLS["obj_mgr"].sprt_grp["gm_ground"]),
                                                          "gm_ground")
                elif level[i][j] == 'F':  # place finish - special
                    pass
                else:
                    CONTROLS["env"].log.warning(f"В паттерне уровня обнаружен недопустимый символ - {line[i]}.")
                
        return None
    

    def load_config_from_file(self) -> int:
        """
        DESCR: Import configuration from cfg-file
        """
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод load_config_from_file")
        CONTROLS["env"].log.info("Загрузка конфигурации...")
        try:
            buffer = open(file=LOCAL_VARS["conf_path"], mode='r', encoding="utf-8").readlines()
        except Exception as ex:
            CONTROLS["env"].log.debug(f"Error code: 2 - {ERRORS[2]}")
            LOCAL_VARS["last_err_code"] = 2
            CONTROLS["env"].log.error("Не удалось загрузить файл конфигурации.")
            CONTROLS["env"].log.debug(f"Raw exception data: {ex.__str__()}")
            
            return 2
        CONTROLS["env"].log.debug("Файл конфигурации загружен.")
        CONTROLS["env"].log.debug("Чтение конфигурации...")
        try:
            for line in buffer:
                conf_line = line.split('=')
                if conf_line[0] in LOCAL_VARS.keys():
                    LOCAL_VARS[conf_line[0]] = int(conf_line[1][:-1]) if conf_line[1][:-1].isdigit() else conf_line[1][:-1]
                else:
                    CONTROLS["env"].log.debug(f"Error code: 3 - {ERRORS[3]}")
                    CONTROLS["env"].log.error("Файл конфигурации имеет неверный формат.")
                    return 3
        except Exception as ex:
            CONTROLS["env"].log.debug(f"Error code: 3 - {ERRORS[3]}")
            LOCAL_VARS["last_err_code"] = 3
            CONTROLS["env"].log.error("Файл конфигурации имеет неверный формат.")
            CONTROLS["env"].log.debug(f"Raw exception data: {ex.__str__()}")
            return 3
        CONTROLS["env"].log.debug(f"Error code: 0 - {ERRORS[0]}")
        CONTROLS["env"].log.info("Конфигурация загружена.")
        return 0

    def save_config_to_file(self) -> int:
        """
        DESCR: Export configuration to cfg-file
        """
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод save_config_to_file.")
        CONTROLS["env"].log.info("Сохранение значений конфигурации в файл...")
        try:
            with open(file=LOCAL_VARS["conf_path"], mode='w', encoding='utf-8') as dst:
                for key, value in CONFIG.items():
                    dst.write(f"{key}={value}\n")
                dst.flush()  
        except Exception as ex:
            CONTROLS["env"].log.debug(f"Error code: 2 - {ERRORS[2]}")
            LOCAL_VARS["last_err_code"] = 2
            CONTROLS["env"].log.error("Не удалось сохранить значения конфигурации в файл.")
            CONTROLS["env"].log.debug(f"Raw exception data: {ex.__str__()}")

            return 2
        CONTROLS["env"].log.debug(f"Error code: 0 - {ERRORS[0]}")
        LOCAL_VARS["last_err_code"] = 0
        CONTROLS["env"].log.info("Конфигурация успешно записана в файл.")
        return 0

    def stop_logging(self) -> None:
        CONTROLS["env"].log.debug(f"Последний зарегистрированный код ошибки: {LOCAL_VARS['last_err_code']}")
        CONTROLS["env"].log.info("===========================================")
        CONTROLS["env"].log.info("Запись завершена!")
        CONTROLS["env"].log.info("===========================================")
        logging.shutdown()
        return None
