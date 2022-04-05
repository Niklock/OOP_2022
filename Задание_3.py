import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 530))


def bird(x, y, size):
    right = []
    left = []
    for i in range(x, x + 15 * size, 1):
        right.append((i, (0.05 / size) * (i - x - 10 * size) ** 2 + y - 15 * size))
        left.append((2 * x - i, (0.05 / size) * (i - x - 10 * size) ** 2 + y - 15 * size))
    polygon(screen, (64, 27, 3), right)
    polygon(screen, (64, 27, 3), left)



rect(screen, (254, 214, 163), (0, 0, 800, 530))# фон солнца
rect(screen, (254, 214, 197), (0, 110, 800, 230))# фон между первой и второй горой
rect(screen, (254, 214, 140), (0, 226, 800, 230))# Второй фон между первой и второй горой
circle(screen, (252, 239, 27), (400, 100), 40)

polygon(screen, (252, 153, 45), [(165, 108), (196, 119), (205, 140), (307, 204), (360, 195), (387, 209), (165, 230)])# Вторая часть первая гора
polygon(screen, (252, 153, 45), [(387, 209), (429, 157), (463, 189), (480, 167), (480, 200)])# Третья часть первая гора

fourth_part_mountain1=[]# Четвертая часть первая гора
for i in range(480, 580, 1):
    fourth_part_mountain1.append((i, (-25 / 4000) * (i - 480) ** 2 + 168))
fourth_part_mountain1.append((600, 189))
fourth_part_mountain1.append((480, 200))
polygon(screen, (252, 153, 45), fourth_part_mountain1)

first_part_mountain1 = []# Первая часть первая гора
for i in range(0, 165, 1):
    first_part_mountain1.append((i, (-109 / 21904) * (i - 17) ** 2 + 217))
first_part_mountain1.append((165, 230))
first_part_mountain1.append((0, 245))
polygon(screen, (252, 153, 45), first_part_mountain1)

polygon(screen, (252, 153, 45), [(579, 105), (634, 134), (666, 127), (718, 155), (750, 140), (800, 170), (600, 189)])# Пятая часть первая гора

polygon(screen, (173, 65, 49),[(800, 190), (800, 340), (655, 344), (655, 284), (688, 240), (720, 263), (740, 235), (770, 240)])# Пятая часть вторая гора
polygon(screen, (173, 65, 49), [(459, 284), (459, 350), (140, 360), (140, 340), (175, 282), (231, 311), (260, 240), (325, 255), (385, 300)])# Вторая часть вторая гора

first_part_mountain2 = []# Первая часть вторая гора
for i in range(25, 155, 1):
    first_part_mountain2.append((i, (18 / 841) * (i - 73) ** 2 + 214))
first_part_mountain2.append((140, 360))
first_part_mountain2.append((25, 360))
polygon(screen, (173, 65, 49), first_part_mountain2)

third_part_mountain2 = []# Третья часть вторая гора
for i in range(450, 565, 1):
    third_part_mountain2 .append((i, (1 / 125) * (i - 550) ** 2 + 220))
third_part_mountain2 .append((565, 360))
third_part_mountain2 .append((450, 360))
polygon(screen, (173, 65, 49), third_part_mountain2 )

fourth_part_mountain2 = []# Четвертая часть вторая гора
for i in range(565, 655, 1):
    fourth_part_mountain2.append((i, (-59 / 7921) * (i - 655) ** 2 + 285))
fourth_part_mountain2.append((655, 360))
fourth_part_mountain2.append((565, 360))
polygon(screen, (173, 65, 49), fourth_part_mountain2)

polygon(screen, (178, 125, 135), [(0, 358), (800, 340), (800, 530), (0, 530)])# фон между второй и третьей горой

bird(622, 460, 3)
bird(545, 410, 2)
bird(636, 390, 2)
bird(500, 376, 2)

bird(320, 270, 2)
bird(380, 245, 2)
bird(380, 220, 2)
bird(310, 210, 2)

polygon(screen, (44, 7, 33), [(0, 265), (95, 300), (175, 400), (175, 530), (0, 530)])# Первая часть третья гора
polygon(screen, (44, 7, 33), [(315, 523), (380, 515), (510, 446), (545, 470), (545, 530), (315, 530)])# Третья часть третья гора

second_part_mountain3 = []# Вторая часть третья гора
for i in range(175, 315, 1):
    second_part_mountain3.append((i, (-5 / 785) * (i - 315) ** 2 + 525))
second_part_mountain3.append((315, 530))
second_part_mountain3.append((175, 530))
polygon(screen, (44, 7, 33), second_part_mountain3)

fourth_part_mountain3 = []# Четвертая часть третья гора
for i in range(511, 800, 1):
    fourth_part_mountain3.append((i, (-10 / 3000) * (i - 580) ** 2 + 460))
fourth_part_mountain3.append((800, 530))
fourth_part_mountain3.append((345, 530))
polygon(screen, (44, 7, 33), fourth_part_mountain3)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()