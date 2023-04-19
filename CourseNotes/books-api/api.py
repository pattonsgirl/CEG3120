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
    # when GET, return form.  when POST, process data
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    conn = get_db_connection()
    #books = conn.execute('SELECT * FROM books').fetchall()
    
    conn.close()
    #return jsonify(books)
    return render_template('new_book.html')

#app.run()
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
