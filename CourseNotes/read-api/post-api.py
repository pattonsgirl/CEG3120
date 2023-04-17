import flask
from flask import request, jsonify, render_template, flash
import sqlite3

# Column names:
# id | published | author | title | first_sentence

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/api/v1', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p><p>TODO: replace with documetation</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()

    return jsonify(all_books)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


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

@app.route('/addbook')
def new_book():
   return render_template('newbook.html')

@app.route('/api/v1/resources/books/addbook',methods = ['POST', 'GET'])
def addbook():
    if request.method == 'POST':
        msg = "This is the default message"
        try:
            # id | published | author | title | first_sentence
            id = request.form['id']
            published = request.form['published']
            author = request.form['author']
            title = request.form['title']
            first_sentence = request.form['first_sentence']

            conn = sqlite3.connect('books.db')
            cur = conn.cursor()            

            cur.execute("INSERT INTO books (id,published,author,title,first_sentence) VALUES (?,?,?,?)",(id,published,author,title,first_sentence) )

            conn.commit()
            msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            #return render_template("results.html",msg = msg)
            return jsonify(msg)
            con.close()


#def run_app():
#    return app
app.run()

#works
#if __name__ == "__main__":
#    from waitress import serve
#    serve(app, port=5000)
