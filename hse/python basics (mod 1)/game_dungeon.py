import random
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


WEAPONS = {'fists': {'attack': 1,
                     'level': 1},
           'knife': {'attack': 3,
                     'level': 3},
           'sword': {'attack': 6,
                     'level': 4},
           'sekiro': {'attack': 5,
                      'level': 4}}

WEAPONS_ICONS = {'sword': '''
     #
O%%%%#============--
     #
''',
'knife': '[]++++||=======>',
'axe': '''
             +-+
=============| |
            `:_;'
''',
                 'fists': 'fists'}

ITEM_SYMBOLS = {'knife': '/',
                'sword': "+",
                'sekiro': 'c',
                'key': 'k'}

END_COORDINATES = (0, 9)

MOVE_COMMANDS = {'w': (-1, 0),
                 's': (1, 0),
                 'd': (0, 1),
                 'a': (0, -1)}

GRID = [['#', '#', '#', '#', '#', '.', '.', '.', '#', 'x'],
        ['#', '#', '#', '.', '.', '.', '#', '.', '#', '.'],
        ['#', '#', '#', '.', '#', '#', '#', '.', '.', '.'],
        ['#', '#', '#', '.', '.', '.', '.', '#', '#', '#'],
        ['#', '#', '#', '#', '.', '.', '.', '#', '.', '#'],
        ['#', '#', '#', '#', '.', '.', '.', '#', '.', '#'],
        ['#', '#', '#', '.', '.', '.', '.', '#', '.', '#'],
        ['#', '#', '.', '.', '#', '#', '.', '.', '.', '#'],
        ['#', '#', '.', '#', '#', '#', '#', '#', '.', '.'],
        ['.', '.', '.', '#', '#', '#', '#', '#', '#', '#']]


class Grid:
    def __init__(self, width, height, grid):
        self.width = width
        self.height = height
        self.grid = [[(grid[row][col], 0) for col in range(len(grid[0]))] for row in range(len(grid))]

    def draw_grid(self):
        cls()
        for x in range(self.width):
            for y in range(self.height):
                print('%%-%ds' % 2 % self.grid[x][y][0], end='') \
                    # if self.grid[x][y][1] else print(' ', end='')
            print()

    def get_allowed_cells(self):
        return_list = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col][0] == '.':
                    return_list.append([row, col])
        return return_list

    def place_items(self, items):
        allowed_cells = self.get_allowed_cells()
        for item in items:
            choosed_cell = random.choice(allowed_cells)
            allowed_cells.remove(choosed_cell)
            item.set_coordinates(choosed_cell)
            self.grid[choosed_cell[0]][choosed_cell[1]] = (item.get_symbol(), 0)

    def update_player(self, direction, new_coordinates):
        self.grid[new_coordinates[0] - direction[0]][new_coordinates[1] - direction[1]] = ('.', 1)
        self.grid[new_coordinates[0]][new_coordinates[1]] = ('@', 1)

    def get_element_symbol(self, coordinates):
        return self.grid[coordinates[0]][coordinates[1]][0]


class Entity:
    def __init__(self, name, coordinates, hitpoints, attack=0, defence=0):
        self.name = name
        self.level = 0
        self.inventory = []
        self.hitpoints = hitpoints
        self.current_weapon = 0
        self.attack, self.defence = attack, defence
        self.coordinates = coordinates

    def base_attack(self):
        return random.uniform(0.5, 1) * self.attack * self.current_weapon.base_attack()

    def attack_entity(self, entity):
        entity.hitpoints -= self.base_attack()

    def get_coordinates(self):
        return self.coordinates

    def add_weapon(self, weapon):
        self.inventory.append(weapon)


class Player(Entity):
    def move(self, direction):
        self.coordinates[0] += direction[0]
        self.coordinates[1] += direction[1]

    def collect_item(self, item):
        self.inventory.append(item)

    def select_weapon(self):
        self.current_weapon = (1 + self.current_weapon) // 4

    def draw_inventory(self):
        print()
        for item_index in range(len(self.inventory)):
            if self.current_weapon == item_index:
                print(self.inventory[item_index].get_symbol(), '     ', '<<<')


class Item:
    def __init__(self, name):
        self.coordinates = ()
        self.name = name

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def get_symbol(self):
        return ITEM_SYMBOLS[self.name]


class Weapon(Item):
    def __init__(self, weapon_name):
        self.name = weapon_name
        self.attack = WEAPONS[weapon_name]['attack']
        self.level = WEAPONS[weapon_name]['level']

    def base_attack(self):
        return self.attack

    def required_level(self):
        return self.required_level()

    def get_name(self):
        return self.name

    def get_symbol(self):
        return WEAPONS_ICONS[self.name]

def game_handler(player, grid, items):
    while player.get_coordinates() != END_COORDINATES:
        player_choise = input('Enter your move: ')
        if player_choise in MOVE_COMMANDS.keys() and \
                is_allowed_move(grid, (MOVE_COMMANDS[player_choise][0] + player.get_coordinates()[0],
                                       MOVE_COMMANDS[player_choise][1] + player.get_coordinates()[1])):
            player.move(MOVE_COMMANDS[player_choise])
            grid.update_player(MOVE_COMMANDS[player_choise], player.get_coordinates())
            grid.draw_grid()
            player.draw_inventory()
        else:
            grid.draw_grid()
            player.draw_inventory()
            print('Wrong input')
            continue


def game_start():
    player = Player('Gennadiy', [9, 0], 30, attack=1, defence=2)
    game_board = Grid(10, 10, GRID)
    game_board.update_player(player.coordinates, player.coordinates)
    game_items = [Item('knife'), Item('sword'), Item('sekiro'), Item('key')]
    game_board.place_items(game_items)
    game_board.draw_grid()
    player.add_weapon(Weapon('fists'))
    player.draw_inventory()
    game_handler(player, game_board, game_items)


def is_allowed_move(grid, new_coord):
    return 0 <= new_coord[0] < grid.width and 0 <= new_coord[1] < grid.height and grid.get_element_symbol(
        new_coord) != '#'


game_start()
