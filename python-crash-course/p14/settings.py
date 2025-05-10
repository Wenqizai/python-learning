""" 
    存储游戏的所有设置
"""

class Settings:
    """ 存储游戏的所有设置 """
    def __init__(self):
        """ 初始化游戏的设置 """
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 速度
        self.ship_limit = 2 # 飞船数量
        # 子弹
        self.bullet_width = 3
        self.bullet_height = 8
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5 # 限制子弹数量 3
        # 外星人
        self.fleet_drop_speed = 5
        
        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        
        # 外星人分数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """ 初始化随游戏进行而变化的设置 """
        self.ship_speed = 3
        self.bullet_speed = 2.5
        self.alien_speed = 2.0
        self.fleet_direction = 1 # fleet_direction 为 1 表示向右移，为 -1 表示向左移
        # 记分设置
        self.alien_points = 50

    def increase_speed(self):
        """ 提高速度设置 """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)