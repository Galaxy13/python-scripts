"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
# import codeskulptor
#
# codeskulptor.set_timeout(20)



def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    die_sum = []
    for dummy_var in range(max(hand) + 1):
        die_sum.append(0)
    for die in hand:
        die_sum[die] += die
    return max(die_sum)




def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    propability = 1.0 / (num_die_sides ** num_free_dice)
    all_scores = []
    for sequence in gen_all_sequences(range(1, num_die_sides + 1), num_free_dice):
        sequence_score = score(sequence + held_dice)
        all_scores.append(sequence_score)
    exp_value = sum(all_scores) * propability
    return exp_value


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    count_of_values = {dice: 0 for dice in hand}
    for dice in hand:
        count_of_values[dice] += 1

    answer_set = [()]
    for index in range(len(hand)):
        answer_set.extend(gen_all_sequences(hand, index + 1))

    temp_list = []
    for sequence_idx, dummy_value in enumerate(answer_set):
        answer_set[sequence_idx] = tuple(sorted(list(answer_set[sequence_idx])))
        for element in answer_set[sequence_idx]:
            if answer_set[sequence_idx].count(element) > count_of_values[element]:
                temp_list.append(answer_set[sequence_idx])
                break
            else:
                continue

    for sequence in temp_list:
        answer_set.remove(sequence)

    return set(answer_set)


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    possible_hold_hands = gen_all_holds(hand)
    max_value = 0
    max_seq_held = ()
    for hand_held in possible_hold_hands:
        exp_value = expected_value(hand_held, num_die_sides, len(hand) - len(hand_held))
        if exp_value >= max_value:
            max_value = exp_value
            max_seq_held = hand_held

    return (max_value, max_seq_held)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (2, 2, 2, 5, 2)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)


run_example()

# import poc_holds_testsuite
# poc_holds_testsuite.run_suite(gen_all_holds)