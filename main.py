from pygame import *
from random import randint
import os

init()
font.init()
mixer.init()

# розміри вікна
WIDTH, HEIGHT = 1200, 700

# картинка фону
bg1 = transform.scale(image.load("IMAGES/background2.jpg"), (WIDTH, HEIGHT))
bg2 = transform.scale(image.load("IMAGES/background2.jpg"), (WIDTH, HEIGHT))

bg1_y =0
bg2_y =-700
max_speed = 20
bg_speed = 4
#картинки для спрайтів
player_image = image.load("IMAGES/carplayer1234.png")
enemy1_image = image.load("IMAGES/car123.png")
enemy2_image = image.load("IMAGES/car12345.png")
#enemy_image = image.load("")

# фонова музика
#mixer.music.load('musictheme.ogg')
#mixer.music.set_volume(0.2)
#mixer.music.play(-1)
# класи
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x, y, speed = 4):
        super().__init__()
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.mask = mask.from_surface(self.image)  

    def draw(self): #відрисовуємо спрайт у вікні
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update(self): #рух спрайту
        global bg_speed
        global max_speed
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < WIDTH - 70:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and bg_speed<max_speed:
            bg_speed = bg_speed+0.5 
        if keys_pressed[K_DOWN] and self.rect.y < HEIGHT - 70:
            bg_speed = bg_speed-3

    
    class Enemy(GameSprite):
        def update(self):
            if self.rect.y < HEIGHT:
                self.rect.y+=self.speed
            else:
                self.rect.y = randint(-500, -100)
                self.rect.x = randint(0, WIDTH-70)
                self.speed = randint(3, 5)

        
class Text(sprite.Sprite):
    def __init__(self, text, x, y, font_size=22, font_name="Impact", color=(255,255,255)):
        self.font = font.SysFont(font_name, font_size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        
    def draw(self): #відрисовуємо спрайт у вікні
        window.blit(self.image, self.rect)
    
    def set_text(self, new_text): #змінюємо текст напису
        self.image = self.font.render(new_text, True, self.color)


# створення вікна
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("CAR RACES")

# написи для лічильників очок
score_text = Text("Рахунок: 0", 20, 50)
# напис з результатом гри 
result_text = Text("Перемога!", 350, 250, font_size = 50)

#додавання фону
bg = transform.scale(bg1, (WIDTH, HEIGHT))

# створення спрайтів
player = Player(player_image, width = 100, height = 200, x = 500, y = 500)
enemy1 = GameSprite(enemy1_image, width = 100, height = 200, x = 700, y = 200)
enemy2 = GameSprite(enemy2_image, width = 100, height = 200, x = 400, y = 100)
# основні змінні для гри
run = True
finish = False
clock = time.Clock()
FPS = 60
score = 0
lost = 0

# ігровий цикл
while run:
    # перевірка подій
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish: # поки гра триває
        # рух спрайтів
        window.blit(bg, (0, bg1_y))
        window.blit(bg2, (0, bg2_y))
        bg1_y +=bg_speed
        bg2_y +=bg_speed
        if bg1_y > 700:
            bg1_y = -700
        if bg2_y > 700:
            bg2_y = -700
        if bg_speed > 7:
            bg_speed -= 0.10
        player.draw()
        #enemy1.draw()
        #enemy2.draw()
        player.update() #рух гравця
    display.update()
    clock.tick(FPS)