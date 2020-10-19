from flask import Flask, render_template

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Need to make the page display the template
@app.route('/')
def index():
    # todo_items=['item1']
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
