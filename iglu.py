import pygame
import math
from pygame.draw import *

def fun_iglu(x, y, size): # Функция рисования иглу
    '''
      x - координата от верхнего левого угла
      y - координата от верхнего левого угла
      size - размер
    '''
    circle(screen, (0, 0, 0), (x + 10 * size, y + 10 * size), 10.35 * size, 1, draw_top_left=True, draw_top_right=True)
    line(screen, (0, 0, 0), (x, y + 10 * size), (x + 20 * size, y + 10 * size), 1)
    circle(screen, (165, 165, 165), (x + 10 * size, y + 10 * size), 10.19 * size, draw_top_left=True, draw_top_right=True)
    arc(screen, (0, 0, 0), (x + 4 * size, y + 1 * size, 12 * size, 2 * size), math.pi, 0)# Четвертая линия снизу
    arc(screen, (0, 0, 0), (x + 2 * size, y + 2 * size, 16 * size, 4 * size), math.pi, 0)# Третья линия снизу
    arc(screen, (0, 0, 0), (x + 0.5 * size, y + 4 * size, 19 * size, 5 * size), math.pi, 0)# Вторая линия снизу
    line(screen, (0, 0, 0), (x, y + 10 * size), (x + 20 * size, y + 10 * size), 1)# Нижняя линия
    line(screen, (0, 0, 0), (x + 1 * size, y + 7.5 * size), (x + 1 * size, y + 10 * size), 1)
    line(screen, (0, 0, 0), (x + 5 * size, y + 5.5 * size), (x + 5 * size, y + 8.5 * size), 1)
    line(screen, (0, 0, 0), (x + 8 * size, y + 3 * size), (x + 8 * size, y + 6 * size), 1)
    line(screen, (0, 0, 0), (x + 9 * size, y + 9 * size), (x + 9 * size, y + 10 * size), 1)
    line(screen, (0, 0, 0), (x + 10 * size, y), (x + 10 * size, y + 3 * size), 1)
    line(screen, (0, 0, 0), (x + 15 * size, y + 2.5 * size), (x + 15 * size, y + 5.5 * size), 1)
    line(screen, (0, 0, 0), (x + 17 * size, y + 5 * size), (x + 17 * size, y + 8 * size), 1)
    line(screen, (0, 0, 0), (x + 18 * size, y + 8 * size), (x + 18 * size, y + 10 * size), 1)


def fun_iskimos(x, y, size): # Функция рисования эскимосов
    '''
      x - координата от верхнего левого угла
      y - координата от верхнего левого угла
      size - размер
    '''
    ellipse(screen, (227, 222, 219), (x, y, 8 * size, 4 * size))
    ellipse(screen, (145, 124, 111), (x - 1 * size, y + 2 * size, 10 * size, 15 * size))
    rect(screen, (255, 255, 255), (x - 1 * size, y + 9.5 * size, 10 * size, 8.5 * size))
    ellipse(screen, (145, 124, 111), (x - 2 * size, y + 3 * size, 3 * size, 2 * size))
    ellipse(screen, (145, 124, 111), (x + 7 * size, y + 3 * size, 3 * size, 2 * size))
    ellipse(screen, (145, 124, 111), (x + 1 * size, y + 9 * size, 2 * size, 3 * size))
    ellipse(screen, (145, 124, 111), (x + 5 * size, y + 9 * size, 2 * size, 3 * size))
    rect(screen, (108, 93, 83), (x + 3 * size, y + 2.5 * size, 2 * size, 7 * size))
    rect(screen, (108, 93, 83), (x - 1 * size, y + 8.5 * size, 10 * size, 2 * size))
    ellipse(screen, (172, 157, 147), (x + 1 * size, y + 0.5 * size, 6 * size, 3 * size))
    ellipse(screen, (227, 219, 219), (x + 1.5 * size, y + 1 * size, 5 * size, 2 * size))
    arc(screen, (0, 0, 0), (x + 3.5 * size, y + 2.5 * size, 1 * size, 0.5 * size), 0, math.pi)
    line(screen, (0, 0, 0), (x + 2.5 * size, y + 1.5 * size), (x + 3.5 * size, y + 2 * size), 1)
    line(screen, (0, 0, 0), (x + 5.5 * size, y + 1.5 * size), (x + 4.5 * size, y + 2 * size), 1)
    line(screen, (0, 0, 0), (x - 0.5 * size, y), (x - 0.5 * size, y + 12 * size), 1)


def fun_cat_with_fish(x, y, size): # Функция рисования котов
    '''
    x - координата от верхнего левого угла
    y - координата от верхнего левого угла
    size - размер
    '''
    ellipse(screen, (204, 204, 204), (x, y, 8 * size, 3 * size))
    draw_ellipse_angle(screen, (204, 204, 204), (x, y + 3 * size, 4 * size, 1 * size), 80, 0)
    draw_ellipse_angle(screen, (204, 204, 204), (x - 1 * size, y + 3 * size, 4 * size, 1 * size), 60, 0)
    draw_ellipse_angle(screen, (204, 204, 204), (x + 5 * size, y + 3 * size, 4 * size, 1 * size), 110, 0)
    draw_ellipse_angle(screen, (204, 204, 204), (x + 6 * size, y + 3 * size, 4 * size, 1 * size), 120, 0)
    draw_ellipse_angle(screen, (204, 204, 204), (x + 7 * size, y, 4 * size, 0.5 * size), 210, 0)

    draw_ellipse_angle(screen, (204, 4, 204), (x - 0.8 * size, y + 1.2 * size, 2 * size, 1 * size), 170, 0)
    draw_ellipse_angle(screen, (4, 4, 204), (x + 1 * size, y + 1.6 * size, 1 * size, 0.3 * size), 210, 0)
    draw_ellipse_angle(screen, (4, 4, 204), (x + 1 * size, y + 2.1 * size, 1 * size, 0.3 * size), 130, 0)
    draw_ellipse_angle(screen, (0, 0, 0), (x - 0.3 * size, y + 1.4 * size, 0.3 * size, 0.3 * size), 0, 0)

    draw_ellipse_angle(screen, (204, 204, 204), (x - 1 * size, y - 1 * size, 3 * size, 2.5 * size), 10, 0)
    polygon(screen, (204, 204, 204),
            ((x - 0.5 * size, y - 0.8 * size), (x, y - 1.6 * size), (x + 0.5 * size, y - 0.8 * size), (x - 0.5 * size, y - 0.8 * size)))
    polygon(screen, (204, 204, 204),
            ((x + 1 * size, y - 0.6 * size), (x + 1.5 * size, y - 1.4 * size), (x + 2 * size, y - 0.4 * size), (x + 1 * size, y - 0.6 * size)))
    circle(screen, (255, 255, 255), (x - 0.1 * size, y - 0.1 * size), 0.5 * size)
    circle(screen, (0, 0, 0), (x - 0.1 * size, y - 0.1 * size), 0.2 * size)
    circle(screen, (255, 255, 255), (x + 1.3 * size, y + 0.1 * size), 0.5 * size)
    circle(screen, (0, 0, 0), (x + 1.3 * size, y + 0.1 * size), 0.2 * size)
    polygon(screen, (0, 0, 0), (
        (x + 0.3 * size, y + 0.7 * size), (x + 0.5 * size, y + 1 * size), (x + 0.7 * size, y + 0.8 * size), (x + 0.3 * size, y + 0.7 * size)))


def draw_ellipse_angle(surface, color, rect, angle, width=0): # Функция поворота эллипса
    '''
    Рисует ногу зайца.
    surface - объект pygame.Surface
    rect - прямоугольник
    angel - угол поворота
    width - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''

    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

#поле
screen.fill('grey')
rect(screen, (255, 255, 255), (0, 240, 500, 260))

fun_iglu(30, 220, 8)
fun_iglu(110, 240, 9)
fun_iglu(20, 260, 10)
fun_iglu(40, 300, 11)
fun_iskimos(300, 220, 8)
fun_iskimos(360, 240, 9)
fun_iskimos(300, 260, 10)
fun_cat_with_fish(280, 360, 8)
fun_cat_with_fish(320, 420, 9)
fun_cat_with_fish(200, 430, 10)
fun_cat_with_fish(30, 430, 11)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()