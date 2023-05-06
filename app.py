from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for menu items
menu_items = [
    {'name': 'Item 1', 'price': 10, 'cooktime': 20, 'availability': 80},
    {'name': 'Item 2', 'price': 15, 'cooktime': 25, 'availability': 70},
    {'name': 'Item 3', 'price': 20, 'cooktime': 30, 'availability': 60}
]

# Define a route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the menu page
@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)

# Define a route for the cook page
@app.route('/cook', methods=['GET', 'POST'])
def cook():
    if request.method == 'POST':
        # Add new item to menu
        new_item = {
            'name': request.form['name'],
            'price': float(request.form['price']),
            'cooktime': int(request.form['cooktime']),
            'availability': int(request.form['availability'])
        }
        menu_items.append(new_item)

    return render_template('cook.html')

if __name__ == '__main__':
    app.run(debug=True)
