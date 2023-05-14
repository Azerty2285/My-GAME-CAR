from pygame import *
from random import randint
import os

init()
font.init()
mixer.init()
mixer.music.load("SOUND\music321.mp3")
mixer.music.set_volume(1000)
mixer.music.play(loops=-1)


# розміри вікна
WIDTH, HEIGHT = 1200, 700
total_time = 30
# картинка фону
bg1 = transform.scale(image.load("IMAGES/background2.jpg"), (WIDTH, HEIGHT))
bg2 = transform.scale(image.load("IMAGES/background2.jpg"), (WIDTH, HEIGHT))


bg1_y =0
bg2_y =-700
max_speed = 30
bg_speed = 4
#картинки для спрайтів
player_image = image.load("IMAGES/carplayer1234.png")
enemy1_image = image.load("IMAGES/car123.png")
enemy2_image = image.load("IMAGES/car12345.png")
enemy3_image = image.load("IMAGES/car1235678.png")
stop_image = image.load("IMAGES/stop.png")
pills_image = image.load("IMAGES/pills.png")
#enemy_image = image.load("")

# фонова музика
#mixer.music.load('musictheme.ogg')   
#mixer.music.set_volume(0.2)
#mixer.music.play(-1)
# класи
path =os.getcwd()
exp_images = os.listdir(path+"/explotion")
images_list = []
#for img in exp_images:
    #images_list.append(transform.scale(image.load("explotion/"+img), (150, 150)))


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
        if keys_pressed[K_LEFT] and self.rect.x > 280:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.right < 905:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and bg_speed<max_speed:
            bg_speed = bg_speed+0.3
        #if keys_pressed[K_DOWN] and self.rect.y < HEIGHT - 70:
            #bg_speed = bg_speed-3

    
class Enemy(GameSprite):
    def update(self):
        if self.rect.y < HEIGHT:
            self.rect.y+=self.speed
        else:
            self.get_random_pos()

    def get_random_pos(self):
        rand_num = randint(1, 4)
        if rand_num == 1:
            self.rect.x = 280
            self.rect.y = -300
        if rand_num == 2:
            self.rect.x = 445
            self.rect.y = -500
        if rand_num == 3:
            self.rect.x = 630
            self.rect.y = -700
        if rand_num == 4:
            self.rect.x = 805
            self.rect.y = -150
        collide_list = sprite.spritecollide(self, enemyies, False)
        for collide in collide_list:
            if collide!= self:
                self.get_random_pos()

class Tree(Enemy):
    def update(self):
        if self.rect.y < HEIGHT:
            self.rect.y+=self.speed
        else:
            self.kill()

class Pill(Enemy):
    def update(self):
        if self.rect.y < HEIGHT:
            self.rect.y+=self.speed
        else:
            self.kill()

    def get_random_pos1(self):
        rand_num = randint(1, 4)
        if rand_num == 1:
            self.rect.x = 280
            self.rect.y = -300
        if rand_num == 2:
            self.rect.x = 445
            self.rect.y = -500
        if rand_num == 3:
            self.rect.x = 630
            self.rect.y = -700
        if rand_num == 4:
            self.rect.x = 805
            self.rect.y = -150
        collide_list = sprite.spritecollide(self, enemyies, False)
        for collide in collide_list:
            if collide!= self:
                self.get_random_pos1()

        

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
result_text = Text("LOSE!", 360, 250, font_size = 150)
#додавання фону
bg = transform.scale(bg1, (WIDTH, HEIGHT))

# створення спрайтів
player = Player(player_image, width = 100, height = 200, x = 500, y = 500)
tree = GameSprite(stop_image, width = 100, height = 200, x = 400, y = 100)
pill = GameSprite(pills_image, width =100, height=200, x = 400, y =  200)
#enemy2 = GameSprite(enemy2_image, width = 100, height = 200, x = 400, y = 100)
# основні змінні для гри
run = True
finish = False
clock = time.Clock()
FPS = 60
score = 0
lost = 0
enemyies = sprite.Group()
trees = sprite.Group()

for i in range(1):
    rand_y = randint(-500, -100)
    rand_x = randint(200, 1000)
    rand_speed = randint(3, 5)
    enemy1= Enemy(enemy1_image , width= 100, height=200, y = rand_y, x = rand_x, speed = rand_speed)
    enemy1.get_random_pos()
    enemy2= Enemy(enemy2_image , width= 100, height=200, y = rand_y, x = rand_x, speed = rand_speed)
    enemy2.get_random_pos()
    enemy3= Enemy(enemy3_image , width= 100, height=200, y = rand_y, x = rand_x, speed = rand_speed)
    enemy3.get_random_pos()
    enemyies.add(enemy1, enemy2, enemy3)    


# ігровий цикл

time_text = Text("Time:", WIDTH - 150, 25, font_size = 40)
distance_text = Text("Distance:", WIDTH-250, 80, font_size = 40)
distance = 10000
pills = sprite.Group()
while run:
    # перевірка подій
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
         # поки гра триває
        # рух спрайтів
        now = time.get_ticks()/1000
        time_left = int(total_time - now)
        time_text.set_text("Time:" + str(time_left))
        distance_text.set_text("Distance: " + str(distance))
        if time_left <= 0:
            result_text.set_text("LOSE!!!")
            finish = True
        
        bg1_y +=bg_speed
        bg2_y +=bg_speed
        if bg1_y > 700:
            bg1_y = -700
        if bg2_y > 700:
            bg2_y = -700
        if bg_speed > 7:
            bg_speed -= 0.1

        if randint(0, 400) == 100:
            rand_y = randint(-500, -100)
            rand_x = randint(200, 1000)
            #rand_speed = randint(3, 5)
            tree = Tree(stop_image, width=150, height = 100, y = rand_y, x = rand_x, speed = rand_speed)
            tree.get_random_pos()
            trees.add(tree)
        
        if randint(0, 1) == 1:
            rand_y = randint(-500, -100)
            rand_x = randint(200, 1000)
            #rand_speed = randint(3, 5)
            pill = Pill(pills_image, width=150, height = 100, y = rand_y, x = rand_x, speed = rand_speed)
            pill.get_random_pos()    
            pills.add(pill)

        player.update() #рух гравця
        enemyies.update() #ру
        trees.update()
        distance -= int(bg_speed*0.40)
        
        if distance <= 0:
            result_text.set_text("WIN!!!")
            finish = True
        spritelist = sprite.spritecollide(player, enemyies, False, sprite.collide_mask)   
        for collide in spritelist:
            #explosions.add(Explosion(collide.rect.x, collide.rect.y, images_list))
            result_text.set_text("LOSE!!!")
            finish = True 

        spritelist = sprite.spritecollide(player, trees, False, sprite.collide_mask)   
        for collide in spritelist:
            #explosions.add(Explosion(collide.rect.x, collide.rect.y, images_list))
            result_text.set_text("LOSE!!!")
            finish = True

        spritelist = sprite.spritecollide(player, pills, True, sprite.collide_mask)   
        for collide in spritelist:
            bg_speed = bg_speed + 3

    window.blit(bg, (0, bg1_y))
    window.blit(bg2, (0, bg2_y))
    player.draw()
    trees.draw(window)
    pills.draw(window)
    time_text.draw()  
    enemyies.draw(window)
    distance_text.draw()  
    if finish:
        result_text.draw()

    display.update()
    clock.tick(FPS)