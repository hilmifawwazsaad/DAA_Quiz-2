from flask import Flask, render_template, url_for, request, redirect, jsonify
import os
# from mapping2 import 

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

# routing untuk halaman abaout
@app.route('/about')
def about():
    return render_template('about.html')

# proses pharsing data dari frontend ke backend 
from mapping2 import process
@app.route('/api/process',methods=['POST'])
def routes():
    # Assuming the JSON body contains 'start' and 'finish'
    
    # Extract 'start' and 'finish' from the JSON data
    start = request.json.get('start')
    finish = request.json.get('finish')

    # Call the 'process' function with 'start' and 'finish'
    shortest_path_length, shortest_path_length_car, shortest_path_length_train, route_path = process(start, finish)
    # print('xxx', x, y, z)

    # Convert the values to JSON format
    result_json = jsonify(
        {'shortest_path_length': shortest_path_length, 
         'shortest_path_length_car': shortest_path_length_car, 
         'shortest_path_length_train': shortest_path_length_train,
         'route_path': route_path})

    return result_json

# agar flask tetap update secara otomatis apabila ada perubahan code    
if __name__ == '__main__': app.run(debug=True)
