"""
Cookie Clicker Simulator
"""
import math
import random
import SimpleGUICS2Pygame.simpleplot as simpleplot

# Used to increase the timeout, if necessary
import SimpleGUICS2Pygame.codeskulptor as codeskulptor

codeskulptor.set_timeout(20)

from temp_parts.ext_lib import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self, current_cookies=0):
        self._current_cookies = current_cookies
        self._total_cookies = 0.0
        self._cookies_inc = 1.0
        self._time_count = 0.0
        self._items_history = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        return ('Time: ' + str(self.get_time()) +
                ' Current cookies: ' + str(self.get_cookies()) +
                ' CPS: ' + str(self.get_cps()) +
                ' Total cookies: ' + str(self.get_total_cookies()) +
                ' History: ' + str(self._items_history))

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return float(round(self._current_cookies, 2))

    def get_total_cookies(self):
        """
        Return total amount of cookies
        """
        return float(math.ceil(self._total_cookies))

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return float(round(self._cookies_inc, 2))

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time_count

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._items_history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies > self._current_cookies:
            return float(math.ceil((cookies - self._current_cookies) / self._cookies_inc))
        else:
            return 0.0

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time <= 0.0:
            return
        else:
            self._current_cookies += self._cookies_inc * time
            self._total_cookies += self._cookies_inc * time
            self._time_count += time

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost > self._current_cookies:
            return
        else:
            self._current_cookies -= cost
            self._cookies_inc += additional_cps
            self._items_history.append((self._time_count, item_name, cost, self._total_cookies))

    def set_current_cookies_sim(self, cookies):
        """
        Sets new meaning to current cookies, for simulation run
        """
        self._current_cookies = cookies

    def set_cps_sim(self, cps):
        """
        Sets new meaning to cps, for simulation run
        """
        self._cookies_inc = cps

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    build_info = build_info.clone()
    clicker_state = ClickerState()
    while clicker_state.get_time() <= duration:
        item = strategy(clicker_state.get_cookies(), clicker_state.get_cps(), clicker_state.get_history(),
                        duration - clicker_state.get_time(), build_info)
        # if item == None:
        #     end_time_wait = duration - clicker_state.get_time()
        #     clicker_state.wait(end_time_wait)
        # else:
        if item is None:
            time_to_end = duration - clicker_state.get_time()
            clicker_state.wait(time_to_end)
            return clicker_state
        elif type(item) is list or type(item) is tuple:
            for curr_item in item[1:]:
                curr_item = curr_item[1]
                time_until = clicker_state.time_until(build_info.get_cost(curr_item))
                clicker_state.wait(time_until)
                clicker_state.buy_item(curr_item, build_info.get_cost(curr_item), build_info.get_cps(curr_item))
                build_info.update_item(curr_item)
        else:
            time_until = clicker_state.time_until(build_info.get_cost(item))
            if time_until > duration - clicker_state.get_time():
                time_to_end = duration - clicker_state.get_time()
                clicker_state.wait(time_to_end)
                return clicker_state
            else:
                clicker_state.wait(time_until)
                while clicker_state.get_cookies() >= build_info.get_cost(item):
                    clicker_state.buy_item(item, build_info.get_cost(item), build_info.get_cps(item))
                    build_info.update_item(item)
    return clicker_state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"


def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None


def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    item_list = build_info.build_items()
    cheapest_item = item_list[0]
    cookies_expected = cookies + (cps * time_left)
    for item in item_list[1:]:
        if build_info.get_cost(item) < build_info.get_cost(cheapest_item):
            cheapest_item = item
        else:
            continue
    if build_info.get_cost(cheapest_item) > cookies_expected:
        return None
    else:
        return cheapest_item


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    item_list = build_info.build_items()
    dearest_item = ''
    dearest_val = float('-inf')
    cookies_expected = cookies + (cps * time_left)
    for item in item_list:
        if dearest_val < build_info.get_cost(item) and build_info.get_cost(item) <= cookies_expected:
            dearest_item = item
            dearest_val = build_info.get_cost(item)
        else:
            continue
    if dearest_item == '':
        return None
    else:
        return dearest_item


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    num_of_tries = 0
    sim_time = 1000 + ((len(history) - 1) * 280000)
    max_try = (0, '')
    while num_of_tries < 4500:
        new_clicker_state = ClickerState()
        build_info = build_info.clone()
        sim_obj = clicker_sim_exp(new_clicker_state, build_info, sim_time, cookies, cps)
        sim_result = (sim_obj.get_total_cookies() + sim_obj.get_cookies()) * (sim_obj.get_cps() - cps)
        if len(sim_obj.get_history()) > 1 and sim_result > max_try[0]:
            max_try = (sim_result, sim_obj.get_history())
            num_of_tries += 1
        else:
            num_of_tries += 1
            continue
    if max_try[1] == '':
        return strategy_expensive(cookies, cps, history, time_left, build_info)
    else:
        return max_try[1]

def clicker_sim_exp(clicker_obj, build_info, sim_time, current_cookies, current_cps):
    item_seq = build_info.build_items()
    clicker_obj.set_current_cookies_sim(current_cookies)
    clicker_obj.set_cps_sim(current_cps)
    while clicker_obj.get_time() < sim_time:
        item = random.choice(item_seq)
        time_until = clicker_obj.time_until(build_info.get_cost(item))
        if time_until > sim_time - clicker_obj.get_time():
            time_to_end = sim_time - clicker_obj.get_time()
            clicker_obj.wait(time_to_end)
            return clicker_obj
        else:
            clicker_obj.wait(time_until)
            clicker_obj.buy_item(item, build_info.get_cost(item), build_info.get_cps(item))
            build_info.update_item(item)
    return clicker_obj


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print(strategy_name, ":", state)

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    history = [(item[0], item[3]) for item in history]
    simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)


def run():
    """
    Run the simulator.
    """
    # run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)


run()

test_class = ClickerState()
# print(test_class)
# print(test_class.get_time())
# print(test_class.get_cookies())
# print(test_class.get_cps())
# print(test_class.get_history())
#
#
#
# test_class.wait(10)
# test_class.buy_item('Sidor', 10, 10)
build_info = provided.BuildInfo()
build_info = build_info.clone()

# print(simulate_clicker(provided.BuildInfo(
#     {'Cursor': [15.0, 0.1], 'Portal': [1666666.0, 6666.0], 'Shipment': [40000.0, 100.0], 'Grandma': [100.0, 0.5],
#      'Farm': [500.0, 4.0], 'Time Machine': [123456789.0, 98765.0], 'Alchemy Lab': [200000.0, 400.0],
#      'Factory': [3000.0, 10.0], 'Antimatter Condenser': [3999999999.0, 999999.0], 'Mine': [10000.0, 40.0]}, 1.15),
#     10000000000.0, strategy_expensive))

# print(simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 0.1]}, 1.15), 10.0, strategy_cursor_broken))

print(strategy_best(1000, 2.0, [(0.0, None, 0.0, 0.0)], 0, build_info))