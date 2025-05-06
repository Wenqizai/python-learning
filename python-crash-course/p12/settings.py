""" 
    存储游戏的所有设置
"""

class Settings:
    """ 存储游戏的所有设置 """
    def __init__(self):
        """ 初始化游戏的设置 """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 速度
        self.ship_speed = 1.5
        # 子弹
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 8
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5 # 限制子弹数量 3
        