'''
https://www.hackerearth.com/problem/algorithm/connected-components-in-a-graph/
'''

# parse input in vars "n" and "edges"
n, num_edges = input().split()
edges = []
for i in range(int(num_edges)):
    edges.append(input().split())
    
# setup a hashmap with maps each node to it's connected component
node_to_connected_componenet_map = dict()
for i in range(int(n)):
    node_to_connected_componenet_map[i+1] = None

connected_components = []
for edge in edges:
    # print(node_to_connected_componenet_map)
    x, y = map(int, edge)
    # we haven't encountered x nor y yet. Create a new connected component containing just the edge, update x and y.
    if node_to_connected_componenet_map[x] is None and node_to_connected_componenet_map[y] is None:
        new_connected_component = set([x, y])
        connected_components.append(new_connected_component)
        # print("created new connected component: ", new_connected_component)
        node_to_connected_componenet_map[x] = new_connected_component
        node_to_connected_componenet_map[y] = new_connected_component
    # If one of them is None and the other isn't, we need to add the element to the component and update the map
    elif node_to_connected_componenet_map[x] is None:
        # print("found existing connccted component for: ", x)
        node_to_connected_componenet_map[y].add(x)
        node_to_connected_componenet_map[x] = node_to_connected_componenet_map[y]
    elif node_to_connected_componenet_map[y] is None:
        # print("found existing connccted component for: ", y)
        node_to_connected_componenet_map[x].add(y)
        node_to_connected_componenet_map[y] = node_to_connected_componenet_map[x]
    # If neither is None, we need to merge the components if they aren't already merged
    else:
        # print("unionizing components for: ", x, " and: ", y)
        node_to_connected_componenet_map[x].update(node_to_connected_componenet_map[y])

# don't forget to add all the singletons
for n, connected_component in node_to_connected_componenet_map.items():
    if connected_component is None:
        connected_components.append(set([n]))

# print(connected_components)
print(len(connected_components))



