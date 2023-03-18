import ctypes, pygame, pymunk

TITLE_STRING = 'Plinko Ripoff'
FPS = 60

# Maintain resolution regardless of Windows scaling settings
ctypes.windll.user32.SetProcessDPIAware()

WIDTH = 1920
HEIGHT = 1080

# Plinko config
BG_COLOR = (16, 32, 45)
MULTI_HEIGHT = int(HEIGHT / 19) # 56 on 1920x1080
MULTI_COLLISION = HEIGHT - (MULTI_HEIGHT * 2) # 968 on 1920x1080

SCORE_RECT = int(WIDTH / 16) # 120 on 1920x1080

OBSTACLE_COLOR = "White"
OBSTACLE_RAD = int(WIDTH / 240) # 8 on 1920x1080
OBSTACLE_PAD = int(HEIGHT / 19) # 56 on 1920x1080
OBSTACLE_START = (int((WIDTH / 2) - OBSTACLE_PAD), int((HEIGHT - (HEIGHT * .9)))) # (904, 108) on 1920x1080
segmentA_2 = OBSTACLE_START

BALL_RAD = 16

# Dictionary to keep track of scores
multipliers = {
    "1000": 0,
    "130": 0,
    "26": 0,
    "9": 0,
    "4": 0,
    "2": 0,
    "0.2": 0
}

# RGB Values for multipliers
multi_rgb = {
    (0, 1000): (255, 0, 0),
    (1, 130): (255, 30, 0),
    (2, 26): (255, 60, 0),
    (3, 9): (255, 90, 0),
    (4, 4): (255, 120, 0),
    (5, 2): (255, 150, 0),
    (6, 0.2): (255, 180, 0),
    (7, 0.2): (255, 210, 0),
    (8, 0.2): (255, 240, 0),
    (9, 0.2): (255, 210, 0),
    (10, 0.2): (255, 180, 0),
    (11, 2): (255, 150, 0),
    (12, 4): (255, 120, 0),
    (13, 9): (255, 90, 0),
    (14, 26): (255, 60, 0),
    (15, 130): (255, 30, 0),
    (16, 1000): (255, 0, 0),
}

# Number of multipliers shown underneath obstacles
NUM_MULTIS = 17

# Pymunk settings (prevent same class collisions)
BALL_CATEGORY = 1
OBSTACLE_CATEGORY = 2
BALL_MASK = pymunk.ShapeFilter.ALL_MASKS() ^ BALL_CATEGORY
OBSTACLE_MASK = pymunk.ShapeFilter.ALL_MASKS()

# Audio stuff
pygame.mixer.init()
click = pygame.mixer.Sound("audio/click.mp3")
sound01 = pygame.mixer.Sound("audio/001.mp3")
sound01.set_volume(0.2)
sound02 = pygame.mixer.Sound("audio/002.mp3")
sound02.set_volume(0.3)
sound03 = pygame.mixer.Sound("audio/003.mp3")
sound03.set_volume(0.4)
sound04 = pygame.mixer.Sound("audio/004.mp3")
sound04.set_volume(0.5)
sound05 = pygame.mixer.Sound("audio/005.mp3")
sound05.set_volume(0.6)
sound06 = pygame.mixer.Sound("audio/006.mp3")
sound06.set_volume(0.7)
sound07 = pygame.mixer.Sound("audio/007.mp3")
sound07.set_volume(0.8)