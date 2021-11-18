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
started = False
# I've added these variables to draw_text, without magical lists of text position
TEXT_POSITION = (50, 50)
SCORE_TEXT_POSITION = (50, 100)
SHIP_GUN_LENGTH = 30

rocks = set()
animation = set()
missiles = set()
cheat_str = ''


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

heart_info = ImageInfo([128, 128], [256, 256])
heart_image = simplegui.load_image("https://www.dropbox.com/s/dfb0cg9ftt147qb/678087%20%281%29.png?dl=1")

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
extra_life_sound = simplegui.load_sound(
    "https://www.myinstants.com/media/sounds/anime-wow-sound-effect.mp3")


# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
# soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# this function draws text information, such as lives and score
def lives_score_info(canvas):
    canvas.draw_text('Lives:' + (WIDTH // 11) * ' ' + 'Score:', TEXT_POSITION, 30, 'White', 'serif')
    for i in range(lives):
        canvas.draw_image(heart_image, heart_info.center, heart_info.size,
                          [SCORE_TEXT_POSITION[0] + (heart_info.size[0] // 4) * i, SCORE_TEXT_POSITION[1]],
                          [heart_info.size[0] // 4, heart_info.size[1] // 4])
    canvas.draw_text(str(score), [SCORE_TEXT_POSITION[0] * 13, SCORE_TEXT_POSITION[1]], 30, 'White', 'serif')


def new_game():
    global rocks, animation, missiles, started
    if started:
        rocks = set()
        missiles = set()
        animation = set()
        timer.stop()
        started = False
        if my_ship.thrust:
            my_ship.stop()
        soundtrack.rewind()
        soundtrack.play()
        my_ship.vel = [0, 0]
        my_ship.angle_vel = 0
    else:
        return


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
        self.cheat = False

    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        global rocks, timer
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        if self.thrust:
            vector = angle_to_vector(self.angle)
            self.vel[0] += vector[0] * .1
            self.vel[1] += vector[1] * .1
            if self.sound_played:
                ship_thrust_sound.play()
        self.vel[0] *= .99
        self.vel[1] *= .99

        # for rock in set(rocks):
        #     if dist(self.pos, rock.pos) <= self.radius + rock.radius:
        #         animation.add(Sprite(rock.pos, rock.vel, 0, 0, explosion_image, explosion_info, explosion_sound))
        #         rocks.remove(rock)

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
        temp = set()
        if self.cheat:
            for i in range(8):
                angle = self.angle + i * 0.79
                vector = angle_to_vector(angle)
                pos = [self.pos[0] + SHIP_GUN_LENGTH * vector[0], self.pos[1] + SHIP_GUN_LENGTH * vector[1]]
                vel = [vector[0] * 6 + self.vel[0], vector[1] * 6 + self.vel[1]]
                angle_vel = 0
                temp.add(Sprite(pos, vel, angle, angle_vel, missile_image, missile_info, missile_sound))
        else:
            angle = self.angle
            vector = angle_to_vector(angle)
            pos = [self.pos[0] + SHIP_GUN_LENGTH * vector[0], self.pos[1] + SHIP_GUN_LENGTH * vector[1]]
            vel = [vector[0] * 6 + self.vel[0], vector[1] * 6 + self.vel[1]]
            angle_vel = 0
            temp.add(Sprite(pos, vel, angle, angle_vel, missile_image, missile_info, missile_sound))
        return temp


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
        if self.animated and self.age <= 24:
            explosion_index = self.age % 24 // 1
            canvas.draw_image(explosion_image,
                              [explosion_info.center[0] + explosion_index * explosion_info.size[0],
                               explosion_info.center[1]],
                              explosion_info.size, self.pos, explosion_info.size)
            self.age += .8
        elif (self.age >= 24 and self.lifespan == None) or (self.age >= 24 and self.animated == True):
            self.animated = False
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.angle += self.angle_vel

        if not self.animated:
            self.age += 1

    def collide(self, object):
        return dist(self.pos, object.pos) <= self.radius + object.radius

    def lifespan_check(self):
        return self.age >= self.lifespan


def draw(canvas):
    global time, lives, score

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
    for a_rock in set(rocks):
        a_rock.draw(canvas)
    for anim in set(animation):
        if anim.animated:
            anim.draw(canvas)
        else:
            animation.remove(anim)
    for missile in set(missiles):
        missile.draw(canvas)

    # updating and checking lives and score info
    lives_score_info(canvas)
    if lives <= 0:
        new_game()
    if score > 0 and score % 1500 == 0:
        lives += 1
        score += 1
        extra_life_sound.play()

    # update ship and sprites
    my_ship.update()
    for rock in set(rocks):
        if rock.collide(my_ship):
            animation.add(Sprite(rock.pos, rock.vel, 0, 0, explosion_image, explosion_info, explosion_sound))
            rocks.remove(rock)
            lives -= 1
            score -= 500
        else:
            rock.update()
    for missile in set(missiles):
        for rock in set(rocks):
            if rock.collide(missile):
                animation.add(Sprite(rock.pos, rock.vel, 0, 0, explosion_image, explosion_info, explosion_sound))
                rocks.remove(rock)
                missiles.discard(missile)
                score += 100
        if not missile.lifespan_check():
            missile.update()
        else:
            missiles.discard(missile)
    # splash screen update
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())
    # soundtrack play-repeat
    soundtrack.play()


# timer handler that spawns a rock
# I just don't want to put this... piece of code in class, so random.functions is calling, only in here
def rock_spawner():
    global a_rock
    if len(rocks) < 12:
        radius = asteroid_info.radius
        pos = [random.randrange(radius, WIDTH - radius), random.randrange(radius, HEIGHT - radius)]
        # this code prevents spawning rock in ship position
        if dist(pos, my_ship.pos) <= my_ship.radius + radius:
            pos[0] += random.randrange(-radius, radius)
            pos[1] = math.sqrt((my_ship.radius + radius + 1) -
                               ((my_ship.radius + radius + 1) - pos[0] ** 2))
        vel = [random.randrange(-1, 1), random.randrange(-1, 1)]
        angle = 0
        angle_vel = random.random() * .2 - .1
        rocks.add(Sprite(pos, vel, angle, angle_vel, asteroid_image, asteroid_info))


def keydown(key):
    if started:
        if key == simplegui.KEY_MAP['left']:
            my_ship.turn(-1)
        elif key == simplegui.KEY_MAP['right']:
            my_ship.turn(1)
        elif key == simplegui.KEY_MAP['up']:
            my_ship.thrusting()
        elif key == simplegui.KEY_MAP['space']:
            missiles.update(my_ship.shoot())


def keyup(key):
    if started:
        if simplegui.KEY_MAP['left'] == key or simplegui.KEY_MAP['right'] == key:
            my_ship.turn(0)
        if simplegui.KEY_MAP['up'] == key:
            my_ship.stop()


def click(pos):
    global started, lives, score, my_ship
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
        timer.start()
        lives = 3
        score = 0


def cheat_handler(text_input):
    if text_input == 'noties' or text_input == 'NOTIES' or text_input == 'no ties':
        my_ship.cheat = not my_ship.cheat


# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)


# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
frame.add_input('Enter the cheat:', cheat_handler, 100)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
frame.start()
