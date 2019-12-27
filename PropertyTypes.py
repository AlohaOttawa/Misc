import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Ontario Property Types</h1>
<p>A prototype API for retrieving property type codes</p>'''


@app.route('/api/v1/resources/propertyseries/all', methods=['GET'])
def api_property_series():
    conn = sqlite3.connect('budget.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_property_series = cur.execute('SELECT * FROM PropertyCodeSeries;').fetchall()

    return jsonify(all_property_series)

@app.route('/api/v1/resources/propertycodes/all', methods=['GET'])
def api_property_codes():
    conn = sqlite3.connect('budget.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_property_codes = cur.execute('SELECT * FROM PropertyCodes;').fetchall()

    return jsonify(all_property_codes)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/propertyseries', methods=['GET'])
def api_property_series_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM PropertyCodeSeries WHERE"
    to_filter = []

    if id:
        query += ' pcsid=? AND'
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

    conn = sqlite3.connect('budget.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

@app.route('/api/v1/resources/propertycodes', methods=['GET'])
def api_property_codes_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM PropertyCodes WHERE"
    to_filter = []

    if id:
        query += ' pcid=? AND'
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

    conn = sqlite3.connect('budget.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()