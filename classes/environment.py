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
