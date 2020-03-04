import flask
from flask import request, jsonify
import sqlite3

db = './tasks.db'

app = flask.Flask(__name__)
app.config["DEBUG"] = True

class dbBroker:
    def __init__(self, database):
        self.db = database
        self.conn = sqlite3.connect(self.db)
        self.conn.row_factory = self.dict_factory
        self.cursor = self.conn.cursor()

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
    
    def query(self, consulta):
        return self.cursor.execute(consulta).fetchall()

    def execute(self, consulta):
        self.cursor.execute(consulta)
        self.cursor.commit()

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
    dbB = dbBroker(db)
    all_books = dbB.query('SELECT * FROM tasks;')
    return jsonify(all_books)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def api_book(task_id):
    query = f"SELECT * FROM tasks WHERE id={task_id};"
    dbB = dbBroker(db)
    task = dbB.query(query)
    return jsonify(task)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()
