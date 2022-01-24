"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._human_list = []
        self._zombie_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited_grid = poc_grid.Grid(self.get_grid_height(), self.get_grid_width())
        visited_grid.clear()
        distance_grid = [[self.get_grid_height() * self.get_grid_width() for row in range(self.get_grid_width())]
                         for col in range(self.get_grid_height())]
        entity_queue = poc_queue.Queue()
        if entity_type == ZOMBIE:
            for zombie in self.zombies():
                entity_queue.enqueue(zombie)
        else:
            for human in self.humans():
                entity_queue.enqueue(human)
        for entity in entity_queue:
            visited_grid.set_full(entity[0], entity[1])
            distance_grid[entity[0]][entity[1]] = 0
        while entity_queue:
            cell = entity_queue.dequeue()
            neighbour_cells = poc_grid.Grid.four_neighbors(self, cell[0], cell[1])
            for ncell in neighbour_cells:
                if visited_grid.is_empty(ncell[0], ncell[1]) and poc_grid.Grid.is_empty(self, ncell[0], ncell[1]):
                    visited_grid.set_full(ncell[0], ncell[1])
                    distance_grid[ncell[0]][ncell[1]] = distance_grid[cell[0]][cell[1]] + 1
                    entity_queue.enqueue(ncell)
        return distance_grid

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for human in self._human_list:
            neighbour_cells = poc_grid.Grid.eight_neighbors(self, human[0], human[1])
            max_cell = [()]
            max_cell_val = float('-inf')
            for cell in neighbour_cells:
                if max_cell_val < \
                        zombie_distance_field[cell[0]][cell[1]] < self.get_grid_width() * self.get_grid_height():
                    max_cell = [cell]
                    max_cell_val = zombie_distance_field[cell[0]][cell[1]]
                elif zombie_distance_field[cell[0]][cell[1]] == max_cell_val:
                    max_cell.append(cell)
                else:
                    continue
        return random.choice(max_cell)

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for zombie in self._zombie_list:
            neighbour_cells = poc_grid.Grid.four_neighbors(self, zombie[0], zombie[1])
            min_cell = [()]
            min_cell_val = float('inf')
            for cell in neighbour_cells:
                if human_distance_field[cell[0]][cell[1]] < min_cell_val and \
                        human_distance_field[cell[0]][cell[1]] < self.get_grid_width() * self.get_grid_height():
                    min_cell = [cell]
                    min_cell_val = human_distance_field[cell[0]][cell[1]]
                elif human_distance_field[cell[0]][cell[1]] == min_cell_val:
                    min_cell.append(cell)
                else:
                    continue
        return random.choice(min_cell)


# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))

# def test_of_zombie():
#
#     suite = poc_simpletest.TestSuite()
#
#     test_class = Apocalypse(30, 40, obstacle_list=[(2,4),(3,7),(29,39)])
#     test_class.add_zombie(1, 1)
#     test_class.add_human(1, 3)
#     test_class.add_zombie(1, 7)
#
#     suite.run_test(test_class.num_zombies(),2, 'TEST # 1')
#     suite.run_test(test_class.num_humans(),1, 'TEST # 2')
#
#     suite.report_results()
#
# test_of_zombie()
#
test_class = Apocalypse(3, 3, [], [(2, 2)], [(1, 1)])
#
# test_class.add_human(2,3)
# test_class.add_human(1,10)
#
# for human in test_class.humans():
#     print(human)

# test_class.add_zombie(1, 1)
# test_class.add_zombie(3,3)
# test_class.add_human(3,0)
# test_class.add_human(2,8)

dist_z = test_class.compute_distance_field(ZOMBIE)
print(test_class.move_humans(dist_z))

test_class = Apocalypse(20, 30, [(4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (15, 10)], [(12, 12), (7, 12)], [(18, 14), (18, 20), (14, 24), (7, 24), (2, 22)])
dist_h = test_class.compute_distance_field(HUMAN)
print(test_class.move_zombies(dist_h))
