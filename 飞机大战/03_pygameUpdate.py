from plane_sprites import *

# 游戏初始化
pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0, 0))
# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150,300))
# 可以在所有绘制工作完成之后,统一调用update方法
pygame.display.update()
# 创建时钟对象
clock = pygame.time.Clock()
# 定义rect记录飞机的位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)

# 游戏循环 → 游戏正式开始
while True:
    # 指定循环体内部的代码的执行频率
    clock.tick(60)
    # 捕获事件
    # event_list = pygame.event.get()
    # if len(event_list) > 0:
    #     print(event_list)
    # 事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            # 卸载所有的模块
            pygame.quit()
            # 终止当前执行的程序
            exit()

    # 修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y < 0:
        hero_rect.y = 700

    # 调用blit方法的绘制
    screen.blit(bg, (0, 0))
    screen.blit(hero,hero_rect)

    # 让精灵组调用2个方法
    # update - 让组中的所有精灵更新位置
    enemy_group.update()
    # draw - 在screen上绘制所有的精灵
    enemy_group.draw(screen)

    # 调用update方法的更新提示
    pygame.display.update()

pygame.quit()