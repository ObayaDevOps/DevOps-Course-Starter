from flask import Flask, render_template, request, redirect
from .data.session_items import get_items, add_item


from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html', todo_items=get_items())
   

@app.route('/add_item', methods=['POST'])
def add_todo_item():
    title = request.form.get('field_name')
    add_item(title)
    return redirect('/', code=302)


if __name__ == '__main__':
    app.run()
