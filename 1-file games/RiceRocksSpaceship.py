# program template for Spaceship
try:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
except:
    import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
# I've added these variables to draw_text, without magical lists of text position
TEXT_POSITION = (50, 50)
SCORE_TEXT_POSITION = (50, 100)
SHIP_GUN_LENGTH = 30


class ImageInfo:
    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5, 5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")


# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
# soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

#this function is called, when obj is going out of the border, it just inverts pos[i] value
def transition(pos):
    if pos[0] <= 0:
        pos[0] = WIDTH
    elif pos[0] >= WIDTH:
        pos[0] = 0
    elif pos[1] <= 0:
        pos[1] = HEIGHT
    elif pos[1] >= HEIGHT:
        pos[1] = 0
    return pos

#this function draws text information, such as lives and score
def text_info(canvas):
    canvas.draw_text('Lives:' + (WIDTH // 11) * ' ' + 'Score:', TEXT_POSITION, 30, 'White', 'serif')
    canvas.draw_text(str(lives) + (WIDTH // 10) * ' ' + str(score), SCORE_TEXT_POSITION, 30, 'White', 'serif')

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.sound_played = False

    def draw(self, canvas):
        canvas.draw_image(self.image,self.image_center ,self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.vel[0] *= 0.97
        self.vel[1] *= 0.97

        if self.thrust:
            vector = angle_to_vector(self.angle)
            self.vel[0] += vector[0] * .2
            self.vel[1] += vector[1] * .2
            if self.sound_played:
                ship_thrust_sound.play()


        if self.pos[0] <= 0 or self.pos[0] >= WIDTH or self.pos[1] <= 0 or self.pos[1] >= HEIGHT:
            self.pos = transition(self.pos)

    def turn(self, sign):
        self.angle_vel = .1 * sign

    def thrusting(self):
        self.thrust = True
        self.image_center[0] += self.image_size[0]
        ship_thrust_sound.rewind()
        ship_thrust_sound.play()
        self.sound_played = True

    def stop(self):
        self.thrust = False
        self.image_center[0] -= self.image_size[0]
        ship_thrust_sound.pause()
        self.sound_played = False

    def shoot(self):
        global a_missile
        angle = self.angle
        vector = angle_to_vector(angle)
        pos = [self.pos[0] + SHIP_GUN_LENGTH * vector[0], self.pos[1] + SHIP_GUN_LENGTH * vector[1]]
        vel = [vector[0] * 6 + self.vel[0], vector[1] * 6 + self.vel[1]]
        angle_vel = 0
        a_missile = Sprite(pos, vel, angle, angle_vel, missile_image, missile_info, missile_sound)


# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.angle += self.angle_vel

        if self.pos[0] <= 0 or self.pos[0] >= WIDTH or self.pos[1] <= 0 or self.pos[1] >= HEIGHT:
            self.pos = transition(self.pos)


def draw(canvas):
    global time

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                      [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    text_info(canvas)

    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()


# timer handler that spawns a rock
# I just don'rt want to put this... piece of code in class, so random.functions is calling, only in here
def rock_spawner():
    global a_rock
    radius = a_rock.radius
    pos = [random.randrange(radius, WIDTH - radius), random.randrange(radius, HEIGHT - radius)]
    vel = [random.randrange(-1, 1), random.randrange(-1, 1)]
    angle = 0
    angle_vel = random.randrange(-10, 10) * .01
    a_rock = Sprite(pos, vel, angle, angle_vel, asteroid_image, asteroid_info)


def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.turn(-1)
    elif key == simplegui.KEY_MAP['right']:
        my_ship.turn(1)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.thrusting()
    elif key == simplegui.KEY_MAP['w']:
        my_ship.shoot()


def keyup(key):
    if simplegui.KEY_MAP['left'] == key or simplegui.KEY_MAP['right'] == key:
        my_ship.turn(0)
    elif simplegui.KEY_MAP['space'] == key:
        my_ship.stop()


# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1, 1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
