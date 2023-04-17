import sqlite3
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

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
    conn = get_db_connection()
    #books = conn.execute('SELECT * FROM books').fetchall()
    
    conn.close()
    #return jsonify(books)
    return render_template('new_book.html')

app.run()
