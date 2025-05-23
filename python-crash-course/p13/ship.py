import pygame

class Ship:
    """ 管理飞船的类 """
    def __init__(self, ai_game):
        """ 初始化飞船并设置其初始位置 """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        # 移动标志（飞船一开始不移动）
        self.moving_right = False
        self.moving_left = False
        
        # 飞船的x坐标
        self.x = float(self.rect.x)
        
    def update(self):
        """ 根据移动标志调整飞船的位置 """
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
            
        # 根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """ 将飞船在屏幕上居中 """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
        
        