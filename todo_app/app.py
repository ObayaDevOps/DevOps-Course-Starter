from flask import Flask, render_template
# import .data.session_items
from .data.session_items import get_items, add_item


from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Now need to retreive the items fron the session file and pass them to the index.html
@app.route('/')
def index():
    return render_template('index.html', todo_items=get_items())


if __name__ == '__main__':
    app.run()
