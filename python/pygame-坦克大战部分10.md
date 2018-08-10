```Python
from enum import Enum, unique
from time import sleep

import pygame

green_color = (0, 255, 0)
black_color = (0, 0, 0)
gray_color = (242, 242, 242)


# pygame.sprite
# 经验: 符号常量优于字面常量 枚举是定义符号常量的最佳选择
@unique
class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Tank(object):

    def __init__(self, x, y, speed=5, tdir=Direction.UP):
        self.x = x
        self.y = y
        self.speed = speed
        self.tdir = tdir

    def move(self):
        if self.tdir == Direction.UP:
            self.y -= self.speed
        elif self.tdir == Direction.RIGHT:
            self.x += self.speed
        elif self.tdir == Direction.DOWN:
            self.y += self.speed
        else:
            self.x -= self.speed

    def fire(self):
        pass

    def draw(self, screen):
        # 绘制坦克的主体
        pygame.draw.rect(screen, green_color, (self.x, self.y, 50, 50), 0)
        # 绘制坦克的履带
        if self.tdir == Direction.UP or self.tdir == Direction.DOWN:
            pygame.draw.rect(screen, black_color, (self.x - 15, self.y - 5, 15, 60), 0)
            pygame.draw.rect(screen, black_color, (self.x + 50, self.y - 5, 15, 60), 0)
        else:
            pygame.draw.rect(screen, black_color, (self.x - 5, self.y - 15, 60, 15), 0)
            pygame.draw.rect(screen, black_color, (self.x - 5, self.y + 50, 60, 15), 0)
        # 绘制坦克的炮管
        if self.tdir == Direction.UP:
            pygame.draw.line(screen, black_color, (self.x + 25, self.y + 25), (self.x + 25, self.y - 15), 8)
        elif self.tdir == Direction.RIGHT:
            pygame.draw.line(screen, black_color, (self.x + 25, self.y + 25), (self.x + 65, self.y + 25), 8)
        elif self.tdir == Direction.DOWN:
            pygame.draw.line(screen, black_color, (self.x + 25, self.y + 25), (self.x + 25, self.y + 65), 8)
        else:
            pygame.draw.line(screen, black_color, (self.x + 25, self.y + 25), (self.x - 15, self.y + 25), 8)


# Python搜索一个变量的方式是LEGB方式
# Local(局部) --> Embedded(嵌套) --> Global(全局) --> Built-in(内置)
def main():

    def refresh_screen():
        pygame.draw.rect(screen, gray_color, (0, 0, 800, 600), 0)
        tank.draw(screen)
        pygame.display.flip()

    tank = Tank(300, 500)
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('坦克大战')
    refresh_screen()
    running = True
    while running:
        tank.move()
        refresh_screen()
        sleep(0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    tank.tdir = Direction.UP
                elif event.key == pygame.K_a:
                    tank.tdir = Direction.LEFT
                elif event.key == pygame.K_s:
                    tank.tdir = Direction.DOWN
                elif event.key == pygame.K_d:
                    tank.tdir = Direction.RIGHT
    pygame.quit()
```

