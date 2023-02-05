import random
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


WEAPONS = {'fists': {'attack': 2,
                     'level': 1},
           'knife': {'attack': 3,
                     'level': 3},
           'sword': {'attack': 6,
                     'level': 4},
           'axe': {'attack': 5,
                   'level': 4},
           'monster_weapon': {'attack': 3,
                              'level': 1}}

WEAPONS_ICONS = {'sword':
                     ['     #             ',
                      'O%%%%#============--       sword',
                      '     #               '
                      ],
                 'knife': ['[]++++||=======>    knife'],
                 'axe': [
                     '             +-+',
                     '=============| |      axe',
                     '            `:_;'],
                 'fists': ['fists']}

GRID_SYMBOLS = {'knife': '/',
                'sword': "+",
                'axe': 'c',
                'key': 'k',
                'fists': None}

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
        ['@', '.', '.', '#', '#', '#', '#', '#', '#', '#']]

MONSTER_NAMES = ['Big HSE Guy', 'Combination of Permutation', 'None', 'Lord of Variables', 'Rick Decart']

MONSTER_IMAGE = """
                 ||
                 ||
   ____ (((+))) _||_
  /.--.\  .-.  /.||.
  /.,   \(0.0)// || 
 /;`";/\ \|m|//  ||  ;
|:   \ \__`:`____||__:|
|:    \__ \T/ (@~)(~@)|
|:    _/|     |\_\/  :|
|:   /  |     |  \   :|
|'  /   |     |   \  '|
 \_/    |     |    \_/
        |     |
        |_____|
        |_____|
"""

EIGHT_DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


class Grid:
    def __init__(self, width, height, monsters_number=3):
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height
        self.start_coordinates = ()
        self.end_coordinates = (0, 9)
        self.monsters_number = monsters_number
        self.monsters = []
        self.path_cells = []

    def draw_grid(self):
        cls()
        for x in range(self.width):
            for y in range(self.height):
                print('%%-%ds' % 2 % self.grid[x][y][0], end='') if self.grid[x][y][1] else \
                    print('%%-%ds' % 2 % '.', end='')
            print()

    def get_allowed_cells(self):
        return_list = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col][0] == '.':
                    return_list.append([row, col])
        return return_list

    def set_predefined_grid(self, grid):
        self.grid = [[(grid[row][col], 0) for col in range(len(grid[0]))] for row in range(len(grid))]
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if grid[row][col][0] == 'x':
                    self.end_coordinates = [row, col]
                elif grid[row][col][0] == '@':
                    self.start_coordinates = [row, col]

    def place_items(self, items):
        allowed_cells = self.get_allowed_cells()
        for item in items:
            choosed_cell = random.choice(allowed_cells)
            allowed_cells.remove(choosed_cell)
            item.set_coordinates(choosed_cell)
            self.grid[choosed_cell[0]][choosed_cell[1]] = [item.get_symbol(), 0]

    def place_monsters(self):
        allowed_cells = self.get_allowed_cells()
        for _ in range(self.monsters_number):
            new_monster = Entity(name=random.choice(MONSTER_NAMES),
                                 coordinates=random.choice(allowed_cells),
                                 hitpoints=random.choice(range(10, 31)),
                                 attack=random.choice(range(1, 4)),
                                 defence=random.choice(range(1, 5)))
            allowed_cells.remove(new_monster.get_coordinates())
            new_monster.add_weapon(Weapon('monster_weapon'))
            self.monsters.append(new_monster)

    def isValid(self, row, col):
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])

    def random_generator(self):
        """
        In the final step, I thought about, maybe some potential player
        wants to play some random levels, with own size of it
        So, my idea, is that we can build random walls with p = 1/2 (or less)
        and on ready example see, that there is existing path between start and finish
        I've thinking about DFS ot BFS attempt on this, but actually 've used DFS
        :return:
        """
        for row in range(self.height):
            for col in range(self.width):
                if random.random() < 0.8:
                    self.grid[row][col] = ['.', 0]
                else:
                    self.grid[row][col] = ["#", 0]

        allowed_cells = self.get_allowed_cells()
        self.start_coordinates = random.choice(allowed_cells)
        self.grid[self.start_coordinates[0]][self.start_coordinates[1]] = ['@', 0]

        allowed_cells.remove(self.start_coordinates)
        self.end_coordinates = random.choice(allowed_cells)
        self.grid[self.end_coordinates[0]][self.end_coordinates[1]] = ['x', 0]
        allowed_cells.remove(self.end_coordinates)

        queue = [self.start_coordinates]
        visited_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        path_found = False
        while queue:
            cell = queue.pop()
            self.path_cells.append(cell)
            if cell == self.end_coordinates:
                print('Grid generated\n')
                input('Press Enter to continue... ')
                path_found = True
            for x, y in (0, 1), (1, 0), (0, -1), (-1, 0):
                if self.isValid(new_x := self.start_coordinates[0] + x, new_y := self.start_coordinates[1] + y) and \
                        not visited_grid[new_x][new_y] and self.grid[row][col][0] != '#':
                    queue.append([new_x, new_y])
                    visited_grid[new_x][new_y] = 1
        print('Re-generating grid\nPlease wait...')
        if not path_found:
            self.path_cells = []
            self.random_generator()

    def update_player(self, direction, new_coordinates):
        self.grid[new_coordinates[0] - direction[0]][new_coordinates[1] - direction[1]] = ['.', 1]
        self.grid[new_coordinates[0]][new_coordinates[1]] = ['@', 1]

    def get_element_symbol(self, coordinates):
        return self.grid[coordinates[0]][coordinates[1]][0]

    def get_monsters_list(self):
        return self.monsters

    def remove_monster(self, monster):
        self.monsters.remove(monster)

    def get_start_coordinates(self):
        return self.start_coordinates

    def make_cells_visible(self, player_coordinates):
        for x, y in EIGHT_DIRECTIONS:
            if self.isValid(new_x := player_coordinates[0] + x, new_y := player_coordinates[1] + y):
                self.grid[new_x][new_y][1] = 1



class Entity:
    def __init__(self, name, coordinates, hitpoints, attack=3, defence=1):
        self.name = name
        self.level = 1
        self.inventory = []
        self.hitpoints = hitpoints
        self.current_weapon = 0
        self.attack, self.defence = attack, defence
        self.coordinates = coordinates

    def base_attack(self):
        return round(random.uniform(0.9, 2) * self.attack * self.inventory[self.current_weapon].base_attack())

    def attack_entity(self, entity):
        entity.hitpoints -= self.base_attack()

    def get_coordinates(self):
        return self.coordinates

    def add_weapon(self, weapon):
        self.inventory.append(weapon)

    def get_hit(self, hit):
        self.hitpoints -= (hit - self.defence) if hit - self.defence >= 0 else self.hitpoints

    def get_defence(self):
        return self.defence

    def get_health(self):
        return self.hitpoints

    def levelup(self):
        self.level += 1

    def get_name(self):
        return self.name


class Player(Entity):
    def move(self, direction):
        self.coordinates[0] += direction[0]
        self.coordinates[1] += direction[1]

    def collect_item(self, item):
        self.inventory.append(item)

    def select_weapon(self):
        self.current_weapon = (1 + self.current_weapon) % len(self.inventory)
        if self.inventory[self.current_weapon].get_name() == 'key':
            self.select_weapon()

    def draw_inventory(self):
        print()
        for item_index in range(len(self.inventory)):
            if (weapon_name := self.inventory[item_index].get_name()) != 'key':
                if self.current_weapon == item_index:
                    marker = len(WEAPONS_ICONS[weapon_name]) // 2
                    for line_index in range(len(weapon_icon := WEAPONS_ICONS[weapon_name])):
                        if line_index == marker:
                            print(weapon_icon[line_index], '    ', '<<<')
                        else:
                            print(weapon_icon[line_index])
                else:
                    for line in WEAPONS_ICONS[weapon_name]:
                        print(line)
            print()

    def has_key(self):
        for item in self.inventory:
            if item.get_symbol() == GRID_SYMBOLS['key']:
                return True


class Item:
    def __init__(self, name):
        self.coordinates = []
        self.name = name

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def get_symbol(self):
        return GRID_SYMBOLS[self.name]

    def get_coordinates(self):
        return self.coordinates

    def get_name(self):
        return self.name


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

    def get_icon(self):
        return WEAPONS_ICONS[self.name]


class Fight:
    def __init__(self, monster, player):
        self.monster = monster
        self.player = player

    def monster_attack(self):
        attack_monster = self.monster.base_attack()
        self.player.get_hit(attack_monster)
        return attack_monster

    def player_attack(self):
        player_attack = self.player.base_attack()
        self.monster.get_hit(player_attack)
        return player_attack

    def draw_monster_and_inventory(self):
        cls()
        print(self.monster.get_name())
        print(MONSTER_IMAGE)
        print()
        print("'a' - Attack, 'c' - Change weapon")
        print()
        print('Monster HP: ', self.monster.hitpoints)
        print()
        print("Player's HP", self.player.hitpoints)
        self.player.draw_inventory()

    def draw_damage(self, player_damage, monster_damage):
        self.draw_monster_and_inventory()
        print()
        print('Your damage:', player_damage)
        print()
        print('Monster damage:', monster_damage)


def check_player_item(player_position, items):
    for item in items:
        if item.get_coordinates() == player_position:
            return item
        else:
            continue


def check_player_monster(player, monsters, grid):
    for monster in monsters:
        if monster.get_coordinates() == player.get_coordinates():
            fight_handler(player, monster, grid)
            break


def fight_handler(player, monster, grid):
    fight = Fight(monster, player)
    fight.draw_monster_and_inventory()
    while 1:
        player_choice = input('Enter command: ')
        if player_choice == 'a':
            player_attack = fight.player_attack()
            if monster.get_health() <= 0:
                print('Monster is defeated!\nLevel Up!')
                grid.remove_monster(monster)
                input('Press Enter to continue: ')
                return
            monster_attack = fight.monster_attack()
            fight.draw_damage(player_attack, monster_attack)
            if player.get_health() <= 0:
                print('Game Over!')
                input('Press Enter to restart: ')
                game_start()
        elif player_choice == 'c':
            player.select_weapon()
            fight.draw_monster_and_inventory()
        else:
            print('\nWrong command!')
            fight.draw_monster_and_inventory()


def game_handler(player, grid, items):
    while player.get_coordinates() != END_COORDINATES:
        grid.make_cells_visible(player.get_coordinates())
        grid.draw_grid()
        player_choise = input('Enter your move: ')
        if player_choise in MOVE_COMMANDS.keys() and \
                is_allowed_move(grid, (MOVE_COMMANDS[player_choise][0] + player.get_coordinates()[0],
                                       MOVE_COMMANDS[player_choise][1] + player.get_coordinates()[1])):
            player.move(MOVE_COMMANDS[player_choise])
            if player.get_coordinates() == list(grid.end_coordinates):
                if player.has_key():
                    cls()
                    print("Congratulations! You've completed demo dungeon")
                    return
                else:
                    player.move((-MOVE_COMMANDS[player_choise][0], -MOVE_COMMANDS[player_choise][1]))
                    print('No key')
                    continue
            grid.update_player(MOVE_COMMANDS[player_choise], player.get_coordinates())
            if item := check_player_item(player.get_coordinates(), items):
                player.add_weapon(item)
            check_player_monster(player, grid.get_monsters_list(), grid)
            grid.draw_grid()
        else:
            grid.draw_grid()
            print('Wrong move')
            continue


def game_start():
    game_board = Grid(10, 10)
    game_board.random_generator()
    player = Player('Gennadiy', game_board.get_start_coordinates(), 30, attack=1, defence=2)
    game_board.update_player(player.coordinates, player.coordinates)
    game_items = [Weapon('knife'), Weapon('sword'), Weapon('axe'), Item('key')]
    game_board.place_items(game_items)
    player.add_weapon(Weapon('fists'))
    game_board.place_monsters()
    game_handler(player, game_board, game_items)
    print('Game Over!')
    return


def is_allowed_move(grid, new_coord):
    return 0 <= new_coord[0] < grid.width and 0 <= new_coord[1] < grid.height and grid.get_element_symbol(
        new_coord) != '#'


game_start()
