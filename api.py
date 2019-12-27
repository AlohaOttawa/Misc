import flask
# from flask import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# create test data
books = [
    {'id': 0,
     'title': 'Ontario Property Tax',
     'rate type': 'rural',
     'rate': '.024',
     'valid from': '1993',
     'valid to': '2020'},
    {'id': 1,
     'title': 'Ontario Property Tax',
     'rate type': 'industrial',
     'rate': '.033',
     'valid from': '1993',
     'valid to': '2020"'},
    {'id': 2,
     'title': 'Ontario Property Tax',
     'rate type': 'commercial',
     'rate': '.042',
     'valid from': '1993',
     'valid to': '2020'}
]


@app.route('/', methods=['GET'])
def home():
    return '<h1>Distant Reading Archive - Hal</h1>'


def hello_world():
    return 'Hello World!'


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # check if an id was provided as part of the URL
    # if ID is provided, assign it to a variable
    # if no ID, then display an error
    if 'hal' in request.args:
        hal = int(request.args['hal'])
    else:
        return "ERROR: no ID was provided.  Please specify an ID"

    # create an empty list to hold the record
    results = []

    # loop through the data and mach the results with the provided ID
    # ids are unique but other fields may return many results
    for book in books:
        if book['id'] == hal:
            results.append(book)

    # use jsonify from flask to convert list to json stream
    return jsonify(results)


if __name__ == '__main__':
    app.run()
