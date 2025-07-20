#!/usr/bin/env python3
""" Making a dynamic template with loops and parsing with JSON """
import json
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        json_file_path = os.path.join(os.path.dirname(__file__), 'items.json')
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        items_list = data.get('items', [])
        
        return render_template('items.html', items=items_list)
    
    except FileNotFoundError:
        return render_template('items.html', items=[])
    
    except json.JSONDecodeError:
        return render_template('items.html', items=[])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
