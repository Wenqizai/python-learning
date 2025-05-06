import sys 
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """ 管理游戏资源和行为的类 """

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()
        # 设置游戏帧率
        self.clock = pygame.time.Clock()
        # 使用配置类来存储参数
        self.settings = Settings()
        # 设置背景色
        self.bg_color = self.settings.bg_color
        # 设置全屏幕
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        # 设置屏幕
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        # 设置标题
        pygame.display.set_caption("Alien Invasion")
        # 创建一艘飞船
        self.ship = Ship(self)
        
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ 开始游戏的主循环 """
        while True:
            # 监听键盘和鼠标事件
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()            
            
            # 游戏帧率
            self.clock.tick(60)
            
    def _check_events(self):
        """ 响应按键和鼠标事件 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: # 按键按下
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: # 按键松开
                self._check_keyup_events(event)
                
    def _update_screen(self):
        """ 更新屏幕上的图像，并切换到新屏幕 """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
        
    def _check_keydown_events(self, event):
        """ 响应按键 """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q: # 按q键退出游戏
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """ 响应松开 """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """ 创建一颗子弹, 并将其加入编组bullets中 """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """ 更新子弹的位置，并删除消失的子弹 """
        # 删除消失的子弹, 子弹只是在屏幕外，但是对象为消失回收，会耗尽内存
        # for 循环中不能边遍历边删除，需要遍历副本如 .copy() 方法
        # 更新子弹的位置
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()