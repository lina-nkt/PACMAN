import pygame
import sys
from .draw_walls import rect_1, fig_1, fig_2, fig_2_2, fig_3, fig_4, fig_5, fig_6, angle_1, angle_2, angle_3, angle_4, \
     angle_5, angle_6, angle_7


z = int(14)
# z равна половине ширины коридора между стенами
# Размер Pacman и привидений = 2 * z
# size = width, height = определяется как размер загруженного поля
black = 0, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
red = 255, 0, 0
yellow = 255, 255, 153

# 0 - поля, по которым ходят герои
# 3 - поля, по которым ходят герои, где находятся повороты
# 2 - поле для очков, количества жизней
# 1 - стены
# 4 - спавн привидений

# матрицу pole_xy можно использовать для размещения фигур на поле
# Если pole_xy[i][j] == 0, то в эту ячейку можно поместить зерно , Pacman , Привидений.

# Если помещаем фигуру и ее центр должен совпадать с центром клеточки,
# ее координаты должна быть:
# если круг, то центр круга - ((j * z  + z // 2; i * z + z // 2)
# Если фигура прямоугольник, (x , y - ширина, высота )
# то координаты ее левого верхнего угла должны быть
# Координаты:  (j * z  + (z-x)// 2; i * z + (z-y) // 2)

pole_xy = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 1, 1, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 3, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 3, 0, 0, 0, 0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0, 0, 0, 0, 3, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 4, 4, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 4, 4, 4, 4, 4, 4, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [8, 0, 0, 0, 0, 0, 3, 0, 0, 3, 1, 4, 4, 4, 4, 4, 4, 1, 3, 0, 0, 3, 0, 0, 0, 0, 0, 9],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 4, 4, 4, 4, 4, 4, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 3, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 3, 0, 3, 1, 1, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 1, 1, 3, 0, 3, 1],
           [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
           [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
           [1, 3, 0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0, 3, 1],
           [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
           ]



size = width, height = z * len(pole_xy[0]), z * len(pole_xy)


def show_walls(screen, z=int(14), color=(0, 0, 255), color_2=(155, 0, 0), d=int(3), r=int(3)):
    rect_1(screen, color, 2 * z + z // 2, 5 * z + z // 2, 3 * z, 2 * z, r, d)
    rect_1(screen, color, 7 * z + z // 2, 5 * z + z // 2, 4 * z, 2 * z, r, d)
    rect_1(screen, color, 16 * z + z // 2, 5 * z + z // 2, 4 * z, 2 * z, r, d)
    rect_1(screen, color, 22 * z + z // 2, 5 * z + z // 2, 3 * z, 2 * z, r, d)
    rect_1(screen, color, 2 * z + z // 2, 9 * z + z // 2, 3 * z, 1 * z, r, d)
    #
    fig_1(screen, color, 10 * z + z // 2, 9 * z + z // 2, 7 * z, 4 * z, 1 * z, r, d)
    fig_1(screen, color, 10 * z + z // 2, 21 * z + z // 2, 7 * z, 4 * z, 1 * z, r, d)
    fig_1(screen, color, 10 * z + z // 2, 27 * z + z // 2, 7 * z, 4 * z, 1 * z, r, d)
    #
    rect_1(screen, color, 22 * z + z // 2, 9 * z + z // 2, 3 * z, 1 * z, r, d)
    rect_1(screen, color, 7 * z + z // 2, 18 * z + z // 2, 1 * z, 4 * z, r, d)
    rect_1(screen, color, 19 * z + z // 2, 18 * z + z // 2, 1 * z, 4 * z, r, d)
    rect_1(screen, color, 7 * z + z // 2, 24 * z + z // 2, 4 * z, 1 * z , r, d)
    rect_1(screen, color, 16 * z + z // 2, 24 * z + z // 2, 4 * z, 1 * z, r, d)
    #
    fig_2_2(screen, color, 2 * z + z // 2, 27 * z + z // 2, 9 * z, 5 * z + z // 2, 4 * z, 1 * z, r, d)
    fig_2_2(screen, color, 16 * z + z // 2, 27 * z + z // 2, 9 * z, 3 * z + z // 2, 4 * z, 1 * z, r, d)
    fig_3(screen, color, 7 * z + z // 2, 9 * z + z // 2, 4 * z, 7 * z, 1 * z, r, d)
    fig_4(screen, color, 16 * z + z // 2, 9 * z + z // 2, 4 * z, 7 * z, 1 * z, r, d)
    fig_5(screen, color, 2 * z + z // 2, 24 * z + z // 2, 3 * z, 4 * z, 1 * z, r, d)
    fig_6(screen, color, 22 * z + z // 2, 24 * z + z // 2, 3 * z, 4 * z, 1 * z, r, d)
    #
    angle_1(screen, color, 0, 3 * z, 13 * z, 8 * z, z // 3, r, d)
    angle_3(screen, color, 0 * z, 11 * z, 4 * z, 2 * z, z // 3, r, d)
    angle_2(screen, color, 4 * z - z // 3, 13 * z - z // 3, 2 * z - z // 3, 1 * z, z // 3, r, d)
    angle_4(screen, color, 0 * z, 13 * z, 6 * z - z // 3 * 2, 3 * z + z // 3, z // 3, r, d)
    angle_2(screen, color, 0 * z, 19 * z - z // 3, 5 * z + z // 3, 3 * z + z // 3, z // 3, r, d)
    angle_4(screen, color, 2 * z, 22 * z, 3 * z + z // 3, z // 3, z // 3, r, d)
    angle_1(screen, color, 0, 22 * z, 3 * z, 5 * z, z // 3, r, d)
    angle_3(screen, color, 0 * z, 29 * z, 14 * z, 5 * z, z // 3, r, d)
    #
    angle_2(screen, color, 15 * z, 3 * z, 13 * z, 8 * z, z // 3, r, d)
    angle_4(screen, color, 24 * z, 10 * z, 4 * z, 3 * z, z // 3, r, d)
    angle_1(screen, color, 23 * z - z // 3, 13 * z - z // 3, 2 * z, 1 * z, z // 3, r, d)
    angle_3(screen, color, 23 * z - z // 3, 14 * z - z // 3, 5 * z + z // 3, 3 * z - z // 3, z // 3, r, d)
    angle_1(screen, color, 23 * z - z // 3, 19 * z - z // 3, 5 * z + z // 3, 1 * z, z // 3, r, d)
    angle_3(screen, color, 23 * z - z // 3, 20 * z - z // 3, 3 * z, 2 * z + z // 3 * 2, z // 3, r, d)
    angle_2(screen, color, 26 * z - z // 3, 22 * z, 2 * z + z // 3, 5 * z + z // 3, z // 3, r, d)
    angle_4(screen, color, 14 * z, 29 * z, 14 * z, 5 * z, z // 3, r, d)
    #
    angle_1(screen, color, 11 * z - z // 3, 16 * z - z // 3, 2 * z + z // 3, 2 * z, z // 3, r, d, 1, 14)
    angle_2(screen, color, 15 * z, 16 * z - z // 3, 3 * z - z // 3 * 2, 2 * z, z // 3, r, d, 1, 14)
    angle_3(screen, color, 11 * z - z // 3, 17 * z - z // 3, 4 * z, 3 * z - z // 3, z // 3, r, d)
    angle_4(screen, color, 15 * z - z // 3, 18 * z - z // 3, 3 * z - z // 3, 2 * z - z // 3, z // 3, r, d)
    pygame.draw.line(screen, (155, 0, 0), [13 * z, 16 * z - z // 3], [15 * z, 16 * z - z // 3], d)
    pygame.draw.line(screen, color, [12 * z, 16 * z - z // 3], [12 * z, 16 * z], d)
    pygame.draw.line(screen, color, [16 * z, 16 * z - z // 3], [16 * z, 16 * z], d)
    pygame.draw.line(screen, color_2, [13 * z - z, 16 * z - z // 3], [15 * z + z, 16 * z - z // 3], d)
    #
    angle_5(screen, color, 25 * z + z // 3 + z % 3, 25 * z + z // 2, 3 * z - z * 2 // 3 - z % 3, 5 * z, z, r, d)
    pygame.draw.line(screen, color, [28 * z, 27 * z], [28 * z, 29 * z], d)
    angle_6(screen, color, 0 * z + z // 3, 25 * z + z // 2, 3 * z - z * 2 // 3, 5 * z, z, r, d)
    pygame.draw.line(screen, color, [0 * z, 27 * z], [0 * z, 29 * z], d)
    angle_7(screen, color, 12 * z - z // 3 + 4, 3 * z + z // 3, 5 * z - z * 2 // 3 - 2, 4 * z + z // 3 - 2, z, r, d)
    pygame.draw.line(screen, color, [5 * z, 3 * z], [15 * z, 3 * z], d)


def show_ways(screen, color_f=(0, 0, 255)):
    for yy in range((len(pole_xy))):
        for xx in range(len(pole_xy[yy])):
            if int(pole_xy[yy][xx]) == 0:
                pygame.draw.rect(screen, color_f, (z * xx, z * yy, z, z), 0)
            elif int(pole_xy[yy][xx]) == 3:
                pygame.draw.rect(screen, color_f, (z * xx, z * yy, z, z), 0)
            else:
                pass


def show_field(screen, z=int(14), color=(0, 0, 255), color_2=(155, 0, 0), d=int(3), r=int(3)):
    show_walls(screen, z, color, color_2, d, r)


def field():
    """
    демо отрисовка поля
    """
    pygame.init()
    screen = pygame.display.set_mode(size)
    gameover = False

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
        screen.fill(black)
        show_field(screen, z)
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


def get_pos_in_field(x, y):
    """
    Функция возвращает кортеж  индексов
    клетки в которой находиться точка

    """
    xx, yy = 0, 0
    if x % z != 0:
        xx = x // z              # индекс с 0
    else:
        xx = x // z - 1
    if y % z != 0:
        yy = y // z              # индекс с 0
    else:
        yy = y // z - 1
    return xx, yy


def is_cell_centre(x, y):
    flag = False
    if z % 2 == 0:
        if((x % z == z//2) or (x % z == z//2 + 1)) and \
          ((y % z == z//2) or (y % z == z//2 + 1)):
            flag = True
    else:
        if(x % z == (z//2+1)) and (y % z == (z//2+1)):
            flag = True
    return flag


if __name__ == '__main__':
    field()
