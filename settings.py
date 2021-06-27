# Dimensions
WIDTH = 612 # Width of game surface
HEIGHT = 612 # height of game surface
ROWS = 17
SQUARE_SIZE = WIDTH // ROWS
GAP_SIZE = 2 # gap between adjacent SQUARE_SIZE

# Music and shit
def background_music():
    pygame.mixer.music.load('assets/phonk.wav')
    pygame.mixer.music.play(-1)


# colors
SURFACE_CLR = (15, 15, 15)
GRID_CLR = (20, 20, 20)
SNAKE_CLR = (50, 255, 50)
APPLE_CLR = (255, 255, 0)
HEAD_CLR = (0, 150, 0)
VIRTUAL_SNAKE_CLR = (255, 0, 0)

# game settings
FPS = 30 #frames per second
INITIAL_SNAKE_LENGTH = 3
WAIT_SECONDS_AFTER_WIN = 15 # time before snake restarts after winning
MAX_MOVES_WITHOUT_EATING = ROWS * ROWS * ROWS* 2 # snake dies after this number moves without eating
SNAKE_MAX_LENGTH = ROWS * ROWS - INITIAL_SNAKE_LENGTH # max snake length

# VARIABLES USED IN BFS ALGORIDDIM
GRID = [[i, j] for i in range(ROWS) for j in range(ROWS)]


# helper functions
def get_neighbors(position):
    neighbors = [[position[0] + 1, position[1]],
                 [position[0] - 1, position[1]],
                 [position[0], position[1] + 1],
                 [position[0], position[1] - 1]]
    in_grid_neighbors = []
    for pos in neighbors:
        if pos in GRID:
            in_grid_neighbors.append(pos)
    return in_grid_neighbors

def distance(pos1, pos2):
    x1, x2 = pos1[0], pos2[0]
    y1, y2 = pos1[1], pos2[1]
    return abs(x2 - x1) + abs(y2 -y1)


# POSITIONS ARE IN TUPLES
ADJACENCY_DICT = {tuple(pos): get_neighbors(pos) for pos in GRID}
