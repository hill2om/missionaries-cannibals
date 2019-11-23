# breadth first search implementation
# we are only passing it a node instead of the entire
# graph, because we'll be generating the graph as we go
def BFS(head):
    # a queue, list of visited states, and a path to
    # the goal state when one is found
    queue = []
    visited = []
    
    queue.append(head)
    visited.append([head.m, head.c, head.boat])
    
    while queue:
        cur = queue.pop(0)
        
        if cur.isGoal():
            return cur
        # my addition to the normal algorithm so that we can
        # grow the graph as needed
        cur.createChildren()
        for child in cur.children:
            tmp = [child.m, child.c, child.boat]
            if tmp not in visited:
                queue.append(child)
                visited.append(tmp)