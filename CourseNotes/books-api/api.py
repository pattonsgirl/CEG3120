import sqlite3
from flask import Flask, render_template, request, url_for, redirect, flash, abort, jsonify

app = Flask(__name__)
# TODO: set flash secret key (needed for sessions)
# https://flask.palletsprojects.com/en/2.0.x/patterns/flashing/
# app.config['SECRET_KEY'] = 'your secret key'
# store in .env file and keep secret (no tracking?)

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_book(book_id):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?',
                        (book_id,)).fetchone()
    conn.close()
    if book is None:
        abort(404)
        # TODO: custom messages
        # https://www.digitalocean.com/community/tutorials/how-to-handle-errors-in-a-flask-application#step-2-creating-custom-error-pages
    return book

@app.route('/')
def index():
    # TODO: index.html with API documentation
    return render_template('index.html')

@app.route('/api/v1/resources/books/all')
def all_books():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    #return jsonify(books)
    return render_template('list.html', books=books)

@app.route('/api/v1/resources/books/newbook', methods=['GET', 'POST'])
def new_book():
    # when GET, return form.  when POST, process data
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        published = request.form['published']
        first_sentence = request.form['first_sentence']
        id = request.form['id']

        if not title:
            flash('Title is required!')
        elif not author:
            flash('Author is required!')
        elif not published:
            flash('Year published is required!')
        elif not first_sentence:
            first_sentence = ""
        elif not id:
            id = "null"
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO books (title, author,published,first_sentence,id) VALUES (?, ?, ?, ?, ?)', \
                         (title, author, published, first_sentence, id))
            conn.commit()
            conn.close()
            flash("New book added!")
            return redirect(url_for('all_books'))
            #return jsonify("Entry added")
    return render_template('new_book.html')

@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    book = get_book(id)
    return jsonify(book)

@app.route('/api/v1/resources/books/<id>/edit/', methods=['GET', 'POST'])
def edit_book(id):
    return 'Post %s' % id
    # TODO: use id to do things
    book = get_book(id)
    # TODO - fill form with book info?

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        published = request.form['published']
        first_sentence = request.form['first_sentence']
        id = request.form['id']

        if not title:
            flash('Title is required!')
        elif not author:
            flash('Author is required!')
        elif not published:
            flash('Year published is required!')
        elif not first_sentence:
            first_sentence = ""
        else:
            conn = get_db_connection()
            conn.execute('UPDATE books SET title = ?, author = ?, published = ?, first_sentence = ?' 
                         ' WHERE id = ?', 
                         (title, author, published, first_sentence, id))
            conn.commit()
            conn.close()
            return redirect(url_for('all_books'))

    return render_template('edit_book.html', book=book)

@app.route('/api/v1/resources/books/<int:id>/delete/', methods=['POST'])
def delete(id):
    book = get_book(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(book['title']))
    return redirect(url_for('all_books'))

#app.run()
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
