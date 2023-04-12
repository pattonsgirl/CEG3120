import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/api', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID or AUTHOR was provided as part of the URL.
    # If ID or AUTHOR is provided, assign it to a variable.
    # If no search field is provided, display an error in the browser.
    results = []
    if 'id' in request.args:
        id = int(request.args['id'])
        for book in books:
            if book['id'] == id:
                results.append(book)
    elif 'author' in request.args:
        author = request.args['author']
        for book in books:
            if book['author'] == author:
                results.append(book)
    else:
        return "Error: No search field provided. Please specify a search field.\n id\t author"

    # if list is empty
    if len(results) == 0:
        return "Error: No results found"
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
