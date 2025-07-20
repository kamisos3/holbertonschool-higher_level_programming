# Python Server-Side Rendering

▶ **Introduction**
This project demonstrates Python Server-Side Rendering (SSR) using Flask and Jinja2 templates. SSR is used to generate dynamic HTML content on the server before sending it to the client, enabling better SEO, faster initial page loads, and easier integration with backend data sources. The project showcases how Python can be used for SSR to build web applications that render HTML pages dynamically from templates and data sources such as JSON, CSV, and SQLite databases.

▶ **Table of Contents**

- Overview[#overview]
- Concepts[#concepts]
- Example[#example]
- Installation[#installation]
- Author[#author]

▶ **Overview**

► Building Flask web applications with Jinja2 templates
► Rendering HTML pages with dynamic data from files and databases
► Implementing reusable template components (header, footer)
► Displaying and filtering data from JSON, CSV, and SQLite sources
► Error handling for missing data and invalid requests

▶ **Concepts**

- Server-Side Rendering (SSR): Generating HTML on the server using Python and sending it to the browser.
- Flask Framework: Lightweight Python web framework for building web applications.
- Jinja2 Templating: Python templating engine for dynamic HTML generation.
- Template Inheritance & Includes: Reusing header and footer templates across multiple pages.
- Data Integration: Reading and displaying data from JSON, CSV, and SQLite database files.
- Routing & Query Parameters: Handling multiple routes and filtering data using URL parameters.
- Error Handling: Managing invalid sources, missing data, and database errors gracefully.

▶ **Example**

Flask route rendering a template with dynamic data:

```python
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products = []
    if source == 'json':
        products = read_json_products('products.json')
    elif source == 'csv':
        products = read_csv_products('products.csv')
    elif source == 'sql':
        products = read_sql_products('products.db')
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
```

Jinja2 template snippet:

```html
<table>
    <tr><th>Name</th><th>Category</th><th>Price</th></tr>
    {% for product in products %}
    <tr>
        <td>{{ product.name }}</td>
        <td>{{ product.category }}</td>
        <td>{{ product.price }}</td>
    </tr>
    {% endfor %}
</table>
```

▶ Installation

Clone this repository in your terminal:

```bash
git clone https://github.com/kamisos3/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering
```

▶ Author

Kami Sostre [https://github.com/kamisos3]