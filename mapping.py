import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
from app.data.cities import CITIES
from app.data.coordinates import COORDINATES
from app.data.car_routes import CAR_ROUTES
from app.data.motorcycle_routes import MOTOR_ROUTES
from app.data.train_routes import TRAIN_ROUTES

def bfs_shortest_path(graph, start, finish):
    """
    BFS implementation to find path with minimum number of hops/cities
    Returns path and number of hops
    """
    if start == finish:
        return [start], 0
    
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current_node, path = queue.popleft()
        
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == finish:
                    return new_path, len(new_path) - 1
                
                queue.append((neighbor, new_path))
                visited.add(neighbor)
    
    return None, None  # No path found

def dfs_find_path(graph, start, finish, visited=None, path=None):
    """
    DFS implementation to find a path (not necessarily optimal)
    Returns first path found
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(start)
    path = path + [start]
    
    if start == finish:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs_find_path(graph, neighbor, finish, visited.copy(), path)
            if result:
                return result
    
    return None

def calculate_path_cost(graph, path):
    """
    Calculate total cost of a given path
    """
    if not path or len(path) < 2:
        return 0
    
    total_cost = 0
    for i in range(len(path) - 1):
        try:
            cost = graph[path[i]][path[i+1]]['weight']
            total_cost += cost
        except KeyError:
            return None  # Path doesn't exist
    
    return total_cost

def create_graphs():
    """
    Create and return the three transportation graphs
    """
    Gmotor = nx.Graph()
    Gcar = nx.Graph()
    Gtrain = nx.Graph()

    # Initialize vertices/nodes
    nodes = CITIES
    Gmotor.add_nodes_from(nodes)
    Gcar.add_nodes_from(nodes)
    Gtrain.add_nodes_from(nodes)

    # Add weighted edges for each transportation type
    Gmotor.add_weighted_edges_from(MOTOR_ROUTES)
    Gcar.add_weighted_edges_from(CAR_ROUTES)
    Gtrain.add_weighted_edges_from(TRAIN_ROUTES)
    
    return Gmotor, Gcar, Gtrain

def process_dijkstra(start, finish):
    """
    Process using Dijkstra algorithm only - for API endpoint
    Returns: {vehicle_type: {path, cost, hops}, ...}
    """
    Gmotor, Gcar, Gtrain = create_graphs()
    results = {}
    
    # Process each transportation type with Dijkstra
    for transport_name, graph in [("motorcycle", Gmotor), ("car", Gcar), ("train", Gtrain)]:
        try:
            dijkstra_cost = nx.shortest_path_length(graph, source=start, target=finish, weight="weight")
            dijkstra_path = nx.shortest_path(graph, source=start, target=finish, weight="weight")
            
            results[transport_name] = {
                'algorithm': 'dijkstra',
                'path': dijkstra_path,
                'path_string': " → ".join(dijkstra_path),
                'cost': dijkstra_cost,
                'hops': len(dijkstra_path) - 1,
                'status': 'success'            }
            
        except (nx.NetworkXNoPath, nx.NodeNotFound) as e:
            results[transport_name] = {
                'algorithm': 'dijkstra',
                'path': None,
                'path_string': "No path available",
                'cost': None,
                'hops': None,                'status': 'no_path',
                'error': str(e)
            }
    
    # Find best option
    best_option = min(results.items(), key=lambda x: x[1]['cost'] if x[1]['cost'] is not None else float('inf'))
    
    return {
        'results': results,
        'best_option': {
            'vehicle': best_option[0],
            'data': best_option[1]
        },
        'algorithm_used': 'dijkstra'
    }

def process_bfs(start, finish):
    """
    Process using BFS algorithm only - for API endpoint
    Returns: {vehicle_type: {path, cost, hops}, ...}
    """
    Gmotor, Gcar, Gtrain = create_graphs()
    results = {}
    
    # Process each transportation type with BFS
    for transport_name, graph in [("motorcycle", Gmotor), ("car", Gcar), ("train", Gtrain)]:
        try:
            bfs_path, bfs_hops = bfs_shortest_path(graph, start, finish)
            
            if bfs_path:
                bfs_cost = calculate_path_cost(graph, bfs_path)
                results[transport_name] = {
                    'algorithm': 'bfs',
                    'path': bfs_path,
                    'path_string': " → ".join(bfs_path),
                    'cost': bfs_cost,                    'hops': bfs_hops,
                    'status': 'success'
                }
            else:
                results[transport_name] = {
                    'algorithm': 'bfs',
                    'path': None,
                    'path_string': "No path available",
                    'cost': None,
                    'hops': None,
                    'status': 'no_path'
                }
                
        except Exception as e:
            results[transport_name] = {
                'algorithm': 'bfs',
                'path': None,
                'path_string': "No path available",
                'cost': None,
                'hops': None,
                'status': 'error',                'error': str(e)
            }
    
    # Find best option (minimum hops)
    best_option = min(results.items(), key=lambda x: x[1]['hops'] if x[1]['hops'] is not None else float('inf'))
    
    return {
        'results': results,
        'best_option': {
            'vehicle': best_option[0],
            'data': best_option[1]
        },
        'algorithm_used': 'bfs'
    }

def process_dfs(start, finish):
    """
    Process using DFS algorithm only - for API endpoint  
    Returns: {vehicle_type: {path, cost, hops}, ...}
    """
    Gmotor, Gcar, Gtrain = create_graphs()
    results = {}
      # Process each transportation type with DFS
    for transport_name, graph in [("motorcycle", Gmotor), ("car", Gcar), ("train", Gtrain)]:
        try:
            dfs_path = dfs_find_path(graph, start, finish)
            
            if dfs_path:
                dfs_cost = calculate_path_cost(graph, dfs_path)
                results[transport_name] = {
                    'algorithm': 'dfs',
                    'path': dfs_path,
                    'path_string': " → ".join(dfs_path),
                    'cost': dfs_cost,
                    'hops': len(dfs_path) - 1,
                    'status': 'success'
                }
            else:
                results[transport_name] = {
                    'algorithm': 'dfs',
                    'path': None,
                    'path_string': "No path available",
                    'cost': None,
                    'hops': None,
                    'status': 'no_path'
                }
                
        except Exception as e:
            results[transport_name] = {
                'algorithm': 'dfs',
                'path': None,
                'path_string': "No path available",
                'cost': None,
                'hops': None,
                'status': 'error',
                'error': str(e)
            }
    
    # For DFS, just pick first available path (since it's not optimized)
    available_options = [item for item in results.items() if item[1]['status'] == 'success']
    best_option = available_options[0] if available_options else list(results.items())[0]
    
    return {
        'results': results,
        'best_option': {
            'vehicle': best_option[0],
            'data': best_option[1]
        },
        'algorithm_used': 'dfs'
    }

def process_all_algorithms(start, finish):
    """
    Process using all algorithms - for comparison
    """
    dijkstra_result = process_dijkstra(start, finish)
    bfs_result = process_bfs(start, finish)
    dfs_result = process_dfs(start, finish)
    
    return {
        'dijkstra': dijkstra_result,
        'bfs': bfs_result,
        'dfs': dfs_result,
        'comparison': {
            'cheapest_route': dijkstra_result['best_option'],
            'fewest_hops': bfs_result['best_option'],
            'dfs_route': dfs_result['best_option']
        }
    }
