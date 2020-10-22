from flask import Flask, render_template, request, redirect
from .data.session_items import get_items, add_item, remove_item, mark_item_complete, clear_all_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    todo_items = get_items()
    if(todo_items != None):
        return render_template('index.html', todo_items=get_items())
    else:
        return render_template('index.html')

@app.route('/add_item', methods=['POST'])
def add_todo_item():
    title = request.form.get('field_name')
    add_item(title)
    return redirect('/', code=302)

@app.route('/remove_item', methods=['POST'])
def remove_todo_item():
    item_id = request.form.get('item_id')
    
    if item_id.isnumeric():
        removal_outcome = remove_item(item_id)
        return redirect('/', code=302)
    else:
        return 'Please enter a numeric value !'

@app.route('/clear_items', methods=['POST'])
def clear_all_todo_items():
    clear_all_items()
    return redirect('/', code=302)


if __name__ == '__main__':
    app.run()
