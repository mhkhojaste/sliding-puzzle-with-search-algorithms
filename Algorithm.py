from Problem import ProblemClass

class AlgorithmClass:

    def bfs(self):
        open_list = []
        close_list = []
        open_list_moves = []
        problem = ProblemClass()
        open_list.append(problem.get_init_state())
        if problem.check_goal(open_list[0]):
            return ''
        open_list_moves.append('')
        i = 0
        while True:
            if not open_list:
                return 'Error'
            my_matrix = open_list[0]
            moves = problem.get_moves(my_matrix)
            for move in moves:
                result_matrix = problem.do_move(my_matrix, move)
                if problem.check_goal(result_matrix):
                    return open_list_moves[0] + move
                elif result_matrix not in open_list and result_matrix not in close_list:
                    open_list.append(result_matrix)
                    open_list_moves.append(open_list_moves[0] + move)

            open_list.pop(0)
            open_list_moves.pop(0)
            close_list.append(my_matrix)
            i += 1

    def dfs(self):
        open_list = []
        close_list = []
        open_list_moves = []
        problem = ProblemClass()
        open_list.append(problem.get_init_state())
        if problem.check_goal(open_list[0]):
            print(open_list[0])
            return ''
        open_list_moves.append('')
        i = 0
        while True:
            if not open_list:
                return 'Error'
            my_matrix = open_list[0]
            moves = problem.get_moves(my_matrix)
            for move in moves:
                result_matrix = problem.do_move(my_matrix, move)
                if problem.check_goal(result_matrix):
                    return open_list_moves[0] + move
                elif result_matrix not in open_list and result_matrix not in close_list:
                    open_list.insert(1, result_matrix)
                    open_list_moves.insert(1, open_list_moves[0] + move)

            open_list_moves.pop(0)
            open_list.pop(0)
            close_list.append(my_matrix)
            i += 1

    def dls(self, limit):
        open_list = []
        close_list = []
        open_list_moves = []
        open_list_depth = []
        problem = ProblemClass()
        open_list.append(problem.get_init_state())
        if problem.check_goal(open_list[0]):
            return ''
        open_list_moves.append('')
        open_list_depth.append(0)
        i = 0
        while True:
            if not open_list:
                return 'Error'
            my_matrix = open_list[0]
            if open_list_depth[0] == limit:
                open_list_depth.pop(0)
                open_list_moves.pop(0)
                open_list.pop(0)
                close_list.append(my_matrix)
                continue
            moves = problem.get_moves(my_matrix)
            for move in moves:
                result_matrix = problem.do_move(my_matrix, move)
                if problem.check_goal(result_matrix):
                    return open_list_moves[0] + move
                elif result_matrix not in open_list and result_matrix not in close_list:
                    open_list.insert(1, result_matrix)
                    open_list_moves.insert(1, open_list_moves[0] + move)
                    open_list_depth.insert(1, open_list_depth[0] + 1)

            open_list_depth.pop(0)
            open_list_moves.pop(0)
            open_list.pop(0)
            close_list.append(my_matrix)
            i += 1

    def ids(self):
        old_close_list = []
        limit = 0
        while True:
            open_list = []
            close_list = []
            open_list_moves = []
            open_list_depth = []
            problem = ProblemClass()
            open_list.append(problem.get_init_state())
            if problem.check_goal(open_list[0]):
                print(open_list[0])
                return ''
            open_list_moves.append('')
            open_list_depth.append(0)
            i = 0
            while True:
                if not open_list:
                    break
                my_matrix = open_list[0]
                if open_list_depth[0] == limit:
                    open_list_depth.pop(0)
                    open_list_moves.pop(0)
                    open_list.pop(0)
                    close_list.append(my_matrix)
                    continue
                moves = problem.get_moves(my_matrix)
                for move in moves:
                    result_matrix = problem.do_move(my_matrix, move)
                    if problem.check_goal(result_matrix):
                        # print(result_matrix)
                        # print(open_list_depth[0])
                        # print(len(open_list_moves[0] + move))
                        # print(len(open_list + close_list))
                        return open_list_moves[0] + move
                    elif result_matrix not in open_list and result_matrix not in close_list:
                        open_list.insert(1, result_matrix)
                        open_list_moves.insert(1, open_list_moves[0] + move)
                        open_list_depth.insert(1, open_list_depth[0] + 1)

                open_list_depth.pop(0)
                open_list_moves.pop(0)
                open_list.pop(0)
                close_list.append(my_matrix)
                i += 1

            if close_list == old_close_list:
                return "Error"
            else:
                old_close_list = close_list
                limit += 1

    def bidirectional(self):
        open_list_start = []
        close_list_start = []
        open_list_moves_start = []
        open_list_goal = []
        close_list_goal = []
        open_list_moves_goal = []
        problem = ProblemClass()
        open_list_start.append(problem.get_init_state())
        open_list_moves_start.append('')
        open_list_goal.append([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        open_list_moves_goal.append('')
        i = 0
        while True:
            if not open_list_start:
                return 'Error'
            my_matrix_start = open_list_start[0]
            if my_matrix_start in open_list_goal:
                print("start")
                return open_list_moves_start[0] + open_list_moves_goal[open_list_goal.index(my_matrix_start)]
            moves = problem.get_moves(my_matrix_start)
            for move in moves:
                result_start = problem.do_move(my_matrix_start, move)
                if result_start not in open_list_start and result_start not in close_list_start:
                    open_list_start.append(result_start)
                    open_list_moves_start.append(open_list_moves_start[0] + move)

            open_list_moves_start.pop(0)
            open_list_start.pop(0)
            close_list_start.append(my_matrix_start)

            if not open_list_goal:
                return 'Error'
            my_matrix_goal = open_list_goal[0]
            if my_matrix_goal in open_list_start:
                return open_list_moves_goal[0] + open_list_moves_start[open_list_start.index(my_matrix_goal)]
            moves = problem.get_moves(my_matrix_goal)
            for move in moves:
                result_goal = problem.do_move(my_matrix_goal, move)
                if result_goal not in open_list_goal and result_goal not in close_list_goal:
                    open_list_goal.append(result_goal)
                    my_move = ''
                    if move == 'L':
                        my_move = 'R'
                    elif move == 'R':
                        my_move = 'L'
                    elif move == 'D':
                        my_move = 'U'
                    elif move == 'U':
                        my_move = 'D'
                    open_list_moves_goal.append(my_move + open_list_moves_goal[0])

            open_list_moves_goal.pop(0)
            open_list_goal.pop(0)
            close_list_goal.append(my_matrix_goal)

            i += 1

    def ucs(self):
        open_list = []
        close_list = []
        open_list_moves = []
        problem = ProblemClass()
        open_list.append(problem.get_init_state())
        if problem.check_goal(open_list[0]):
            return ''
        open_list_moves.append('')
        i = 0
        while True:
            if not open_list:
                print(problem.get_init_state())
                print("close list : ", close_list)
                return 'Error'
            my_matrix = open_list[0]
            if problem.check_goal(my_matrix):
                # print(my_matrix)
                # print(len(open_list_moves[0]) + 1)
                # print(len(open_list + close_list))
                return open_list_moves[0]
            moves = problem.get_moves(my_matrix)
            for move in moves:
                result_matrix = problem.do_move(my_matrix, move)
                if result_matrix not in close_list:
                    if result_matrix not in open_list:
                        open_list.append(result_matrix)
                        open_list_moves.append(open_list_moves[0] + move)
                    else:
                        old_move = open_list_moves[open_list.index(result_matrix)]
                        new_move = open_list_moves[0]
                        if len(new_move) + 1 < len(old_move):
                            open_list.insert(open_list.index(result_matrix), result_matrix)
                            open_list_moves.insert(open_list.index(result_matrix), open_list_moves[0] + move)
                            open_list_moves.pop(open_list.index(result_matrix))
                            open_list.pop(open_list.index(result_matrix))

            open_list.pop(0)
            open_list_moves.pop(0)
            close_list.append(my_matrix)
            i += 1

    def a_star(self):
        open_list = []
        close_list = []
        open_list_moves = []
        fn = []
        problem = ProblemClass()
        open_list.append(problem.get_init_state())
        open_list_moves.append('')
        fn.append(problem.find_h(open_list[0]))
        i = 0

        while True:
            if not open_list:
                print(problem.get_init_state())
                return 'Error'
            min_index = fn.index(min(fn))
            my_matrix = open_list[min_index]
            if problem.check_goal(my_matrix):
                # print(my_matrix)
                # print(len(open_list_moves[0]) + 1)
                # print(len(open_list + close_list))
                return open_list_moves[min_index]
            moves = problem.get_moves(my_matrix)
            for move in moves:
                result = problem.do_move(my_matrix, move)
                if result not in close_list:
                    if result not in open_list:
                        open_list.append(result)
                        open_list_moves.append(open_list_moves[min_index] + move)
                        fn.append(len(open_list_moves[min_index] + move) + problem.find_h(result))
                    elif len(open_list_moves[min_index] + move) + problem.find_h(result) < fn[open_list.index(result)]:
                        fn[open_list.index(result)] = len(open_list_moves[min_index] + move) + problem.find_h(result)
                        open_list_moves[open_list.index(result)] = open_list_moves[min_index] + move

            open_list.pop(min_index)
            open_list_moves.pop(min_index)
            fn.pop(min_index)
            close_list.append(my_matrix)

            i += 1






