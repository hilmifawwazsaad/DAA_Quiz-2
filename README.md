# 🚗 TRANSPORTIMA - Central Java Transportation Route Finder Application

## 📋 Project Information

**Project Name:** TRANSPORTIMA (Transportation Route Finder for Central Java)

**Course:** Algorithm Design and Analysis (PAA) - Quiz 2

**Description:** A Flask-based web application that implements shortest path finding algorithms (Dijkstra, BFS, DFS) for transportation in Central Java with three transportation modes: car, motorcycle, and train.

---

## 👥 Team Members

| No | Full Name | Student ID |
|----|-----------|------------|
| 1  | Amanda Illona Farrel | 5025221056 |
| 2  | Hilmi Fawwaz Sa'ad | 5025221103 |
| 3  | Muhammad Detri Abdul Fikar | 5025221236 |

---

## 🎯 Main Features

- **Dijkstra Algorithm**: Find routes with minimum cost/distance
- **BFS Algorithm**: Find routes with minimum number of hops/cities
- **DFS Algorithm**: Find routes using depth-first search method
- **Algorithm Comparison**: Compare results from all three algorithms simultaneously
- **Multi-Modal Transport**: Support route finding for car, motorcycle, and train
- **Web Interface**: User-friendly web interface with Bootstrap

---

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Graph Processing**: NetworkX
- **Visualization**: Matplotlib
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Data Structure**: Graph with weighted edges

---

## 📁 Project Structure

```
Quiz_2/
├── main.py                    # Flask application main file
├── mapping.py                 # Algorithm implementations
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── app/
│   ├── data/                  # Data files
│   │   ├── cities.py          # List of cities in Central Java
│   │   ├── coordinates.py     # City coordinates
│   │   ├── car_routes.py      # Car transportation routes
│   │   ├── motorcycle_routes.py # Motorcycle routes
│   │   └── train_routes.py    # Train routes
│   └── templates/             # HTML templates
│       ├── index.html         # Landing page
│       ├── home.html          # Home page
│       ├── menu.html          # Menu page
│       └── about.html         # About page
├── static/                    # Static files (CSS, JS, images)
│   ├── script.js              # JavaScript functionality
│   └── assets/                # Images and icons
└── bootstrap/                 # Bootstrap CSS and JS files
```

---

## 🚀 How to Run the Application

### 1. System Requirements
- Python 3.8 or newer
- pip (Python package installer)

### 2. Install Dependencies
```powershell
# Clone or download this project
git clone https://github.com/hilmifawwazsaad/DAA_Quiz-2.git

# Navigate to project directory
cd DAA_Quiz-2

# Install required dependencies
pip install -r requirements.txt
```

### 3. Run the Application
```powershell
# Run Flask application
python main.py
```

### 4. Access the Application
- Open browser and visit: `http://localhost:5000`
- Or `http://127.0.0.1:5000`

---

## 📖 Usage Guide

### 1. Accessing Web Interface
1. Run the application using commands above
2. Open browser and access `http://localhost:5000`
3. Navigate through available menus

### 2. Using API Endpoints

#### Dijkstra Algorithm
```bash
POST /api/dijkstra
Content-Type: application/json

{
  "start": "magelang",
  "finish": "blora"
}
```

#### BFS Algorithm
```bash
POST /api/bfs
Content-Type: application/json

{
  "start": "magelang",
  "finish": "blora"
}
```

#### DFS Algorithm
```bash
POST /api/dfs
Content-Type: application/json

{
  "start": "magelang",
  "finish": "blora"
}
```

#### Compare All Algorithms
```bash
POST /api/compare
Content-Type: application/json

{
  "start": "magelang",
  "finish": "blora"
}
```

---

## 🧪 Testing

To test the application:

1. **Manual Testing via Web Interface:**
   - Access the web page and test each feature
   - Try various combinations of origin and destination cities

2. **API Testing:**
   - Use tools like Postman or curl
   - Test all endpoints with valid data

---

## 📚 Implemented Algorithms

### 1. Dijkstra Algorithm
- **Purpose**: Find routes with minimum total cost/distance
- **Complexity**: O((V + E) log V)
- **Advantage**: Optimal for weighted graph

### 2. BFS (Breadth-First Search) Algorithm
- **Purpose**: Find routes with minimum number of hops/cities
- **Complexity**: O(V + E)
- **Advantage**: Optimal for unweighted graph, minimum hops

### 3. DFS (Depth-First Search) Algorithm
- **Purpose**: Find existing paths (not necessarily optimal)
- **Complexity**: O(V + E)
- **Characteristics**: Exploratory, not optimal

---

## 🐛 Troubleshooting

### Error: ModuleNotFoundError
```powershell
# Install missing dependencies
pip install flask networkx matplotlib numpy
```

### Error: Port already in use
- Change port in main.py or stop application using port 5000

### Error: Template not found
- Make sure folder structure matches the description above

---

## 📞 Team Contact

- **Team Email**: transportima.team@gmail.com
- **Repository**: [GitHub Repository Link]
- **Documentation**: See docs/ folder for complete documentation

---

## 📄 License

This project is created for academic purposes for Quiz 2 of Algorithm Design and Analysis course.

---

*Made with ❤️ by TRANSPORTIMA Team - Institut Teknologi Sepuluh Nopember (ITS)*