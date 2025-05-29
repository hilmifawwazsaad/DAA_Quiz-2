from flask import Flask, render_template, url_for, request, redirect, jsonify
import os
from mapping import process_dijkstra, process_bfs, process_dfs, process_all_algorithms

app = Flask(__name__, template_folder="app/templates", static_folder="static")

# routing untuk halaman awal
@app.route('/')
def index():
    return render_template('index.html')

# routing untuk halaman home
@app.route('/home')
def home():
    return render_template('home.html')

# routing untuk halaman menu
@app.route('/menu') 
def menu():
    return render_template('menu.html')

# routing untuk halaman about
@app.route('/about')
def about():
    return render_template('about.html')

# ================ DIJKSTRA ALGORITHM API ================
@app.route('/api/dijkstra', methods=['POST'])
def dijkstra_route():
    """
    API endpoint specifically for Dijkstra algorithm
    Returns detailed results for all transportation types using Dijkstra
    """
    try:
        data = request.get_json()
        start = data.get('start')
        finish = data.get('finish')

        if not start or not finish:
            return jsonify({'error': 'Start and finish locations are required'}), 400

        result = process_dijkstra(start, finish)
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 500

# ================ BFS ALGORITHM API ================
@app.route('/api/bfs', methods=['POST'])
def bfs_route():
    """
    API endpoint specifically for BFS algorithm
    Returns detailed results for all transportation types using BFS
    """
    try:
        data = request.get_json()
        start = data.get('start')
        finish = data.get('finish')

        if not start or not finish:
            return jsonify({'error': 'Start and finish locations are required'}), 400

        result = process_bfs(start, finish)
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 500

# ================ DFS ALGORITHM API ================
@app.route('/api/dfs', methods=['POST'])
def dfs_route():
    """
    API endpoint specifically for DFS algorithm
    Returns detailed results for all transportation types using DFS
    """
    try:
        data = request.get_json()
        start = data.get('start')
        finish = data.get('finish')

        if not start or not finish:
            return jsonify({'error': 'Start and finish locations are required'}), 400

        result = process_dfs(start, finish)
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 500

# ================ ALL ALGORITHMS COMPARISON API ================
@app.route('/api/compare', methods=['POST'])
def compare_algorithms():
    """
    API endpoint to compare all algorithms
    Returns results from Dijkstra, BFS, and DFS for comparison
    """
    try:
        data = request.get_json()
        start = data.get('start')
        finish = data.get('finish')

        if not start or not finish:
            return jsonify({'error': 'Start and finish locations are required'}), 400

        result = process_all_algorithms(start, finish)
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 500

# ================ GET AVAILABLE CITIES API ================
@app.route('/api/cities', methods=['GET'])
def get_cities():
    """
    API endpoint to get list of available cities
    """
    try:
        from app.data.cities import CITIES
        return jsonify({
            'cities': CITIES,
            'count': len(CITIES),
            'status': 'success'
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 500

# ================ ALGORITHM INFO API ================
@app.route('/api/algorithms', methods=['GET'])
def get_algorithm_info():
    """
    API endpoint to get information about available algorithms
    """
    algorithms_info = {
        'dijkstra': {
            'name': 'Dijkstra Algorithm',
            'description': 'Finds the shortest path with minimum cost/weight',
            'optimal_for': 'Cost minimization',
            'endpoint': '/api/dijkstra'
        },
        'bfs': {
            'name': 'Breadth-First Search (BFS)',
            'description': 'Finds the path with minimum number of hops/stops',
            'optimal_for': 'Minimizing number of cities to pass through',
            'endpoint': '/api/bfs'
        },
        'dfs': {
            'name': 'Depth-First Search (DFS)',
            'description': 'Finds the first available path (depth-first exploration)',
            'optimal_for': 'Path exploration (not necessarily optimal)',
            'endpoint': '/api/dfs'
        }
    }
    
    return jsonify({
        'algorithms': algorithms_info,
        'comparison_endpoint': '/api/compare',
        'status': 'success'
    }), 200

# ================ ERROR HANDLERS ================
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Method not allowed'}), 405

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Keep flask automatically updating when code changes occur    
if __name__ == '__main__': 
    app.run(debug=True)