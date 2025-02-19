import os 

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
TIME = 60
TITLE = 'Rocketship Shooting Game'

#PLAYER SETTINGS
PLAYER_SPEED = 300 

BASE_DIR = os.path.dirname(__file__)

# Image Paths
PLAYER_IMAGE = os.path.join(BASE_DIR, 'images', 'player.png')
STAR_IMAGE = os.path.join(BASE_DIR, 'images', 'star.png')
METEOR_IMAGE = os.path.join(BASE_DIR, 'images', 'meteor.png')
LASER_IMAGE = os.path.join(BASE_DIR, 'images', 'laser.png')