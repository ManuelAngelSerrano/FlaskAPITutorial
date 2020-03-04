import flask
from flask import request, jsonify
from dbBroker import dbBroker

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>
<p>/tasks para ver todas las tareas</p>''' 

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# A route to return all of the available entries in our catalog.
@app.route('/tasks/', methods=['GET'])
def api_all():
    dbB = dbBroker()
    all_books = dbB.query('SELECT * FROM tasks;')
    return jsonify(all_books)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def api_book(task_id):
    query = f"SELECT * FROM tasks WHERE id={task_id};"
    dbB = dbBroker()
    task = dbB.query(query)
    return jsonify(task)

app.run()
