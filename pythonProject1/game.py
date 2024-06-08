import pygame
import random
import requests
import sys

# Инициализация PyGame
pygame.init()

# Настройки экрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Угадай слово")
font = pygame.font.Font(None, 36)

# Цвета
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)

# Словарь сложности и соответствующих списков слов
difficulty_levels = {
    'легкая': ["банан", "слива", "ананас"],
    'средняя': ["гранат", "мандарин", "персик"],
    'сложная': ["киви", "папайя", "манго"]
}

# Выбор уровня сложности
difficulty = 'средняя'  # Можно изменить на 'легкая' или 'сложная'

# Список слов для выбранной сложности
words = difficulty_levels[difficulty]

# Функция для запроса подсказки у сервера
def get_hint(guessed_letters):
    response = requests.post('http://localhost:5000/get_hint', json={'guessed_letters': guessed_letters})
    return response.json()['hint']

# Основной игровой цикл
running = True
guessed_letters = []
while running:
    screen.fill(PURPLE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение подсказки от сервера
    hint_word = get_hint(guessed_letters)
    text = font.render(f"Подсказка: {hint_word}", True, YELLOW)
    screen.blit(text, (300, 250))

    pygame.display.flip()

pygame.quit()


