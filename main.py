# imports the State class
# and our BFS algorithm
from state import State
from searchAlgorithms import BFS

def getParents(solution):
    path = []
    path.append(solution)
    state = solution.parent
    while state:
        path.insert(0, state)
        state = state.parent
    return path

def __main__():
    head = State(3, 3, True, None)
    solution = BFS(head)
    path = getParents(solution)

    if path is not None:
        print('Number of moves:', len(path) - 1)
        for state in path:
            state.printState()
    else:
        print('No solution found')
        
if __name__ == "__main__":
    __main__()