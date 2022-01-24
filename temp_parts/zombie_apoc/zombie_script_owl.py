"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui
import poc_simpletest

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
        distance_grid = [[(row + 1) * (col + 1) for row in range(self.get_grid_width())]
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
        cell = entity_queue.dequeue()
        neighbour_cells = poc_grid.Grid.four_neighbors(self, cell[0], cell[1])
        for ncell in neighbour_cells:
            if visited_grid.is_empty(ncell[0], ncell[1]):
                visited_grid.set_full(ncell[0], ncell[1])
                distance_grid[ncell[0]][ncell[1]] = distance_grid[cell[0]][cell[1]] + 1
                entity_queue.enqueue(ncell)
                return distance_grid

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        pass

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        pass