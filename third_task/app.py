from app_initializer import AppInitializer
from search import BreadthFirstSearch

app_initializer = AppInitializer()
total_map = app_initializer.initialize()

search = BreadthFirstSearch()
shortest_path = search.search_for_shortest_distance(total_map)

if shortest_path:
    print("The shortest path from raft to place of destination is:")
    for x, y in shortest_path:
        print(f"({x+1},{y+1})", end=" -> ")#Adding 1 because list starts with zero, but users usually count from 1
    print("End")
    print(f"Length of the path: {len(shortest_path)}")
else:
    print("No path exists from raft to place of destination.")