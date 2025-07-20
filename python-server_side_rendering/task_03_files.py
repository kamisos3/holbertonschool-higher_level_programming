#!/usr/bin/env python3
""" Displays data from JSON or CSV files in Flask """
import json
import csv
import os
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json_products(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv_products(filepath):
    products = []
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
    except Exception:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products = []
    if source == 'json':
        products = read_json_products(os.path.join(os.path.dirname(__file__), 'products.json'))
    elif source == 'csv':
        products = read_csv_products(os.path.join(os.path.dirname(__file__), 'products.csv'))
    else:
        error = 'Wrong source'
    if not error and product_id is not None:
        filtered = [p for p in products if p['id'] == product_id]
        if filtered:
            products = filtered
        else:
            error = 'Product not found'
            products = []
    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
