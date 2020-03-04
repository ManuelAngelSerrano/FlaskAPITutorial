import flask
from flask import request, jsonify
from tasksDAO import tasksDAO

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
def api_getAll():
    return jsonify(tasksDAO().getAll())

@app.route('/tasks/<int:task_id>', methods=['GET'])
def api_get(task_id):
    return jsonify(tasksDAO().get(task_id))

@app.route('/tasks/', methods=['POST'])
def api_new():
    priority = request.args.get('priority')    
    task = request.args.get('task')    
    tasksDAO().set(priority, task)
    return "<h1>200</h1>", 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def api_delete(task_id):
    tasksDAO().delete(task_id)
    return "<h1>200</h1>", 200

@app.route('/tasks/', methods=['DELETE'])
def api_deleteAll():
    tasksDAO().deleteAll()
    return "<h1>200</h1>", 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def api_update(task_id):
    priority = request.args.get('priority')    
    task = request.args.get('task')    
    tasksDAO().update(task_id, priority, task)
    return "<h1>200</h1>", 200


app.run()
