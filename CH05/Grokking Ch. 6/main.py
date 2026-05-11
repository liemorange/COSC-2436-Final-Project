def bfs(adjacency_list, target):
    # Initialize the queue and visited set
    if adjacency_list is None:
        return None
    
    queue = [adjacency_list[0]]  # start with first node
    visited = set()
    while queue:                          # keep going until empty
        obj = queue.pop(0)                # grab first item
        if obj not in visited:
            if obj == target:             # found it?
                return True
            visited.add(obj)              # mark as visited
            for neighbor in adjacency_list[obj]:  # add neighbors
                queue.append(neighbor)
    
    return False  # never found it