import sys 
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class AlienInvasion:
    """ 管理游戏资源和行为的类 """

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()
        # 设置游戏帧率
        self.clock = pygame.time.Clock()
        # 使用配置类来存储参数
        self.settings = Settings()
        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)
        
        # 游戏启动后处于活动状态
        self.game_active = True
        
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
        # 创建子弹
        self.bullets = pygame.sprite.Group()
        # 创建外星人
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """ 开始游戏的主循环 """
        while True:
            # 监听键盘和鼠标事件
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()           
            self._update_screen()
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
        # 绘制外星人
        self.aliens.draw(self.screen)
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
        # 检查是否有子弹击中了外星人
        self._check_bullet_alien_collisions()

    
    def _check_bullet_alien_collisions(self):
        """ 检查是否有子弹击中了外星人 """
        # 如果是这样，就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
                
    def _create_fleet(self):
        """ 创建外星人群 """
        # 创建一个外星人
        # 创建一个外星人，再不断添加，知道没有空间添加外星人为止
        # 外星人的间距为外星人宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x = alien_width
        current_y = alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # 移动到下一行
            current_x = alien_width # x 坐标重置到最左边
            current_y += 2 * alien_height # y 坐标增加外星人高度
    
    def _create_alien(self, x_position, y_position):
        """ 创建一个外星人并放在当前行 """
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
    def _update_aliens(self):
        """ 更新外星人群中所有外星人的位置 """
        self._check_fleet_edges()
        self.aliens.update()
        # 检查是否有外星人到达了屏幕底端（与飞船相撞）
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检查是否有外星人到达了屏幕底端
        self._check_aliens_bottom()
        
    def _check_fleet_edges(self):
        """ 检查是否有外星人到达了屏幕边缘 """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """ 在有外星人到达屏幕边缘时改变整群外星人的方向 """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
                
    def _ship_hit(self):
        """ 响应飞船被外星人撞到 """
        if self.stats.ships_left > 0:
            # 将ships_left减1
            self.stats.ships_left -= 1
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人，并将飞船放到屏幕底端中央
            self._create_fleet()
            self.ship.center_ship()
            # 暂停
            sleep(0.5)
        else:
            self.game_active = False
    
    def _check_aliens_bottom(self):
        """ 检查是否有外星人到达了屏幕底端 """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理
                self._ship_hit()
                break
    
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()