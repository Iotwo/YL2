from pygame import image, Rect, sprite
from pygame.math import Vector2

from classes.go_object import GOObject
from scripts.variables import CONTROLS, LOCAL_VARS, ERRORS


class GOUnit(GOObject):
    """
    """
    def __init__(self, pic_path, position:tuple, speed: int, *group) -> None:
        super().__init__(pic_path, position, *group)
        self.BASIC_W = 32
        self.BASIC_H = 32
        self.STRIKE_W = 40
        self.JUMP_POWER = 3.75
        
        self.vx = speed
        self.vy = speed / 10
        self.velocity = Vector2(0, 0)
        self.actions = ["ATTACK", "JUMP", "STOP"]
        self.directions = ["DOWN", "LEFT", "RIGHT", "STOP", "UP"]
        self.cur_act = "STOP"
        self.cur_dir = "RIGHT"
        self.cur_movement = "STOP"
        self.is_falling = False

        self.cur_frame_atk_left = 0
        self.cur_frame_atk_right = 0
        self.cur_frame_jump_right = 0
        self.cur_frame_jump_left = 0
        self.cur_frame_move_left = 0
        self.cur_frame_move_right = 0
        self.cur_frame_stand_left = 0
        self.cur_frame_stand_right = 0
        self.attack_left_frames = []
        self.attack_right_frames = []
        self.jump_left_frames = []
        self.jump_right_frames = []
        self.move_left_frames = []
        self.move_right_frames = []
        self.stand_left_frames = []
        self.stand_right_frames = []
        
        self.fill_frame_tapes()
        
        return None
    
    def __new__(cls, *args, **kwargs) -> object:
        instance = super().__new__(cls, *args, **kwargs)

        instance.BASIC_W = None
        instance.BASIC_H = None
        instance.STRIKE_W = None
        instance.JUMP_POWER = None

        instance.actions = None
        instance.directions = None
        instance.cur_act = None
        instance.cur_movement = None
        instance.vx = None
        instance.vy = None
        instance.velocity = None
        instance.is_falling = None

        instance.cur_frame_atk_left = None
        instance.cur_frame_atk_right = None
        instance.cur_frame_jump_right = None
        instance.cur_frame_jump_left = None
        instance.cur_frame_move_left = None
        instance.cur_frame_move_right = None
        instance.cur_frame_stand_left = None
        instance.cur_frame_stand_right = None
        instance.attack_left_frames = None
        instance.attack_right_frames = None
        instance.jump_left_frames = None
        instance.jump_right_frames = None
        instance.move_left_frames = None
        instance.move_right_frames = None
        instance.stand_left_frames = None
        instance.stand_right_frames = None
        
        return instance


    def act(self, action: str) -> None:
        self.rect.height = self.BASIC_H
        if action == "STOP":
            pass
        elif action == "JUMP":
            self.act_jump()
        elif action == "ATTACK":
            self.rect.width = self.STRIKE_W
            self.act_attack()

    def act_attack(self) -> None:
        return None

    def act_jump(self) -> None:
        if self.is_falling is False:
            self.rect.bottom -= 2
            self.set_falling(True)
            if self.velocity.y >= 0:
                self.velocity.y = -(self.vx) * self.JUMP_POWER
        self.cur_act= "STOP"
        
        return None

    def apply_gravity(self) -> None:
        if self.is_falling is True:
            self.velocity.y += self.vy
            self.rect.y += self.velocity.y
        
        return None

    def fill_frame_tapes(self) -> None:
        self.stand_left_frames = [self.image.subsurface(Rect(self.BASIC_W * i, self.BASIC_H * 1,
                                                             self.BASIC_W, self.BASIC_H))
                                  for i in range(1)]
        self.stand_right_frames = [self.image.subsurface(Rect(self.BASIC_W * i, self.BASIC_H * 0,
                                                              self.BASIC_W, self.BASIC_H))
                                   for i in range(1)]
        self.move_left_frames = [self.image.subsurface(Rect(self.BASIC_W * (i + 1), self.BASIC_H * 1,
                                                            self.BASIC_W, self.BASIC_H))
                                 for i in range(2)]
        self.move_right_frames = [self.image.subsurface(Rect(self.BASIC_W * (i + 1), self.BASIC_H * 0,
                                                             self.BASIC_W, self.BASIC_H))
                                  for i in range(2)]
        """
        self.attack_left_frames = []
        self.attack_right_frames = []
        self.jump_left_frames = []
        self.jump_right_frames = []
        """
        return None
    
    def move(self, direction: str) -> None:
        self.rect.width = self.BASIC_W
        self.rect.height = self.BASIC_H
        if direction == "STOP":
            if self.cur_dir == "LEFT":
                self.image = self.stand_left_frames[self.cur_frame_stand_left]
            elif self.cur_dir == "RIGHT":
                self.image = self.stand_right_frames[self.cur_frame_stand_right]
            self.cur_frame_move_left = 0
            self.cur_frame_move_right = 0
            self.cur_frame_jump_right = 0
            self.cur_frame_jump_left = 0
            self.cur_frame_atk_right = 0
            self.cur_frame_atk_left = 0
        elif direction == "LEFT":
            self.cur_dir = direction
            self.cur_frame_move_left = (self.cur_frame_move_left + 1) % len(self.move_left_frames)
            self.cur_frame_move_right = 0
            self.cur_frame_atk_right = 0
            self.cur_frame_atk_left = 0
            self.cur_frame_jump_right = 0
            self.cur_frame_jump_left = 0
            self.image = self.move_left_frames[self.cur_frame_move_left]
            self.move_left()  # move left
        elif direction == "RIGHT":
            self.cur_dir = direction
            self.cur_frame_move_right = (self.cur_frame_move_right + 1) % len(self.move_right_frames)
            self.cur_frame_move_left = 0
            self.cur_frame_atk_right = 0
            self.cur_frame_atk_left = 0
            self.cur_frame_jump_right = 0
            self.cur_frame_jump_left = 0
            self.image = self.move_right_frames[self.cur_frame_move_right]
            self.move_right()  # move right
        
        return None

    def move_left(self) -> None:
        self.rect = self.rect.move(-self.vx, 0)
        return None

    def move_right(self) -> None:
        self.rect = self.rect.move(self.vx, 0)
        return None

    def set_cur_action(self, act: str) -> None:
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод set_cur_action c аргументами: "\
                                  f"{act}::{type(act)}; ")
        if act in self.actions:
            self.cur_act = act
            CONTROLS["env"].log.debug(f"Error code: 0 - {ERRORS[0]}")
            LOCAL_VARS["last_err_code"] = 0
            CONTROLS["env"].log.info(f"Слово состояния action юнита {self.__class__.__name__} по адресу {id(self)} изменено на {act}")
        else:
            CONTROLS["env"].log.warn(f"Error code: 61 - {ERRORS[61]}")
            LOCAL_VARS["last_err_code"] = 61
            
        return None
    
    def set_cur_movement(self, move: str) -> None:
        CONTROLS["env"].log.debug(f"У Экземпляра {self.__class__.__name__} по адресу {id(self)} "\
                                  f"вызван метод set_cur_movement c аргументами: "\
                                  f"{move}::{type(move)}; ")
        if move in self.directions:
            self.cur_movement = move
            CONTROLS["env"].log.debug(f"Error code: 0 - {ERRORS[0]}")
            LOCAL_VARS["last_err_code"] = 0
            CONTROLS["env"].log.info(f"Слово состояния movement юнита {self.__class__.__name__} по адресу {id(self)} изменено на {move}")
        else:
            CONTROLS["env"].log.warn(f"Error code: 60 - {ERRORS[60]}")
            LOCAL_VARS["last_err_code"] = 60
        
        return None

    def set_falling(self, falling: bool) -> None:
        self.is_falling = falling

        return None

    def update(self, *args) -> None:
        """
        if self.rect.collidepoint():
            # if enemy - damage
            # if wall - stop
            pass
        else:
            self.move(self.cur_act)
        """
        self.apply_gravity()
        # the easiest way I found here
        # is to check any collison from inside the class
        # Game dev is surely not mine pros

        self.move(self.cur_movement)
        self.act(self.cur_act)
        return None
