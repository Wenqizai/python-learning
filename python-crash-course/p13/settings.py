""" 
    存储游戏的所有设置
"""

class Settings:
    """ 存储游戏的所有设置 """
    def __init__(self):
        """ 初始化游戏的设置 """
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        # 速度
        self.ship_speed = 1.5
        self.ship_limit = 3 # 飞船数量
        # 子弹
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 8
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5 # 限制子弹数量 3
        # 外星人
        self.alien_speed = 2.0
        self.fleet_drop_speed = 5
        # fleet_direction 为 1 表示向右移，为 -1 表示向左移
        self.fleet_direction = 1
        