from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from config import db_config
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('form.html', action='Add')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('form.html', user=user, action='Edit')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
