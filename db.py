import os
import sqlite3
import sys

import pygame

from objects.draw_walls import black
from objects.ghost import resource_path

# Подключение к базе данных (если её нет, она будет создана)
db = sqlite3.connect('pacman_scores.db')

# Создание курсора для выполнения SQL-запросов
cursor = db.cursor()

# Создание таблицы для хранения пользователей и их результатов игры
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacman_scores (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        score INTEGER
    )
''')

db.commit()

# Функция для регистрации нового пользователя
def register_user(screen):
    # Подключение к базе данных
    conn = sqlite3.connect('pacman_scores.db')
    cursor = conn.cursor()

    font = pygame.font.Font(None, 36)

    input_box = pygame.Rect(100, 250, 200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    game_over = False
    game_quit = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        # Запись в БД
                        cursor.execute("INSERT INTO pacman_scores (username) VALUES (?)", (text,))
                        username = text
                        conn.commit()
                        text = ''
                        running = False
                        game_over = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                else:
                    if event.type == pygame.KEYDOWN:
                        if chr(event.key) == 'q':
                            game_over = True

        # Отрисовка окна
        screen.fill((30, 30, 30))
        name_surface = font.render(text, True, (255, 255, 255))
        width = max(200, name_surface.get_width() + 10)
        input_box.w = width
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(name_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        pygame.time.wait(20)
        pygame.display.update()

    print('Пользователь успешно зарегистрирован')
    if game_quit:
        sys.exit(0)
    res = username
    username = None
    return res


# Функция для сохранения результата игры Пакмана
def add_new_score(score, username):
    db = sqlite3.connect('pacman_scores.db')
    cursor = db.cursor()
    if username != None:
        cursor.execute('SELECT id FROM pacman_scores WHERE username = ?', (username,))
        user_id = cursor.fetchone()[0]
        cursor.execute('UPDATE pacman_scores SET score = ? WHERE id = ? and username = ?', (score, user_id, username))
        db.commit()
        print('Результат игры сохранен')


def draw(screen):
    db = sqlite3.connect('pacman_scores.db')
    cursor = db.cursor()

    cursor.execute("SELECT * FROM pacman_scores ORDER BY score DESC LIMIT 10")

    data = cursor.fetchall()
    row_height = 50

    for i, row in enumerate(data):
        if i < len(data):
            text = f"            {i+1}            {row[1]}            {row[2]}"
            font = pygame.font.SysFont(None, 30)
            text_obj = font.render(text, True, (255, 255, 255))
            screen.blit(text_obj, (10, i * row_height + 10))

    cursor.close()
    db.close()

path = resource_path(os.path.join('img', '2.png'))
fon = pygame.image.load(path)
def highscore_table(screen):
    db = sqlite3.connect('pacman_scores.db')

    photo = fon

    game_over = False
    game_quit = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == 'q':
                    game_over = True

        screen.fill(black)
        screen.blit(photo, (-70, 100))
        draw(screen)

        pygame.display.flip()
        pygame.time.wait(20)
        pygame.display.update()
    if game_quit:
        sys.exit(0)

