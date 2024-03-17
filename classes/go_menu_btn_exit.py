from pygame import image

from classes.go_menu_btn import GOMenuButton
from scripts.variables import CONTROLS, LOCAL_VARS, ERRORS


class GOMenuButtonExit(GOMenuButton):
    """
    """
    def update(self, *args) -> None:
        super().update(args)
        if self.rect.collidepoint(args[0]) and args[1] == 1:
            CONTROLS["env"].log.debug(f"В экземпляре {self.__class__.__name__} "\
                                      f"произошла коллизия: "\
                                      f"{args[0]}::{type(args[0])} "\
                                      f"{args[1]}::{type(args[1])} ")
            CONTROLS["st_mchn"].switch_game_state("ENDED")
        return None
