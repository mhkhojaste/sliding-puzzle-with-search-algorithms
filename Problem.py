from copy import deepcopy
from math import sqrt

class ProblemClass:
    def __init__(self):
        self.state = []
        self.state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

    def get_init_state(self):
        return self.state

    def get_moves(self, my_state):
        if my_state[0][0] == 0:
            return ['R', 'D']
        elif my_state[0][1] == 0:
            return ['L', 'R', 'D']
        elif my_state[0][2] == 0:
            return ['L', 'D']
        elif my_state[1][0] == 0:
            return ['R', 'D', 'U']
        elif my_state[1][1] == 0:
            return ['L', 'R', 'D', 'U']
        elif my_state[1][2] == 0:
            return ['L', 'D', 'U']
        elif my_state[2][0] == 0:
            return ['R', 'U']
        elif my_state[2][1] == 0:
            return ['L', 'R', 'U']
        elif my_state[2][2] == 0:
            return ['L', 'U']

    def do_move(self, states, transaction):
        my_state = deepcopy(states)
        indexes = [(ix, iy) for ix, row in enumerate(my_state) for iy, i in enumerate(row) if i == 0]
        i_index = indexes[0][0]
        j_index = indexes[0][1]
        if transaction == 'R':
            my_state[i_index][j_index] = my_state[i_index][j_index + 1]
            my_state[i_index][j_index + 1] = 0
        elif transaction == 'L':
            my_state[i_index][j_index] = my_state[i_index][j_index - 1]
            my_state[i_index][j_index - 1] = 0
        elif transaction == 'U':
            my_state[i_index][j_index] = my_state[i_index - 1][j_index]
            my_state[i_index - 1][j_index] = 0
        elif transaction == 'D':
            my_state[i_index][j_index] = my_state[i_index + 1][j_index]
            my_state[i_index + 1][j_index] = 0
        return my_state

    def check_goal(self, my_state):
        if my_state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return True
        else:
            return False

    def find_h(self, my_matrix):
        sum = 0
        for i in range(3):
            for j in range(3):
                number = (i * 3 + j + 1) % 9
                indexes = [(ix, iy) for ix, row in enumerate(my_matrix) for iy, i in enumerate(row) if i == number]
                sum += sqrt((i - indexes[0][0]) ** 2 + (j - indexes[0][1]) ** 2)

        return round(sum, 2)



