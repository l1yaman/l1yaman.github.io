from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from PIL import Image
import sqlite3, os

app = Flask(__name__)
app.secret_key = 'super_secret_key'

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def init_db():
    with sqlite3.connect('shop.db') as conn:
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            price REAL,
            image TEXT
        )
        ''')
        conn.commit()

init_db()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_admin():
    return session.get("user") == "admin"

@app.route('/login')
def login():
    session['user'] = 'admin'
    flash('Logged in as admin')
    return redirect(url_for('admin_panel'))

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out")
    return redirect('/')

@app.route('/')
def index():
    with sqlite3.connect("shop.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM products")
        products = c.fetchall()
    return render_template("index.html", products=products)

@app.route('/admin')
def admin_panel():
    if not is_admin():
        return redirect('/login')

    with sqlite3.connect("shop.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM products")
        products = c.fetchall()
    return render_template("admin.html", products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if not is_admin():
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        file = request.files['image']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)

            try:
                img = Image.open(path)
                img.verify()
            except:
                os.remove(path)
                flash("Invalid image")
                return redirect(url_for('add_product'))

            with sqlite3.connect("shop.db") as conn:
                c = conn.cursor()
                c.execute("INSERT INTO products (name, description, price, image) VALUES (?, ?, ?, ?)",
                          (name, description, price, filename))
                conn.commit()
            flash("Product added")
            return redirect('/admin')

    return render_template("add.html")

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    if not is_admin():
        return redirect('/login')

    with sqlite3.connect("shop.db") as conn:
        c = conn.cursor()
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            price = float(request.form['price'])
            c.execute("UPDATE products SET name=?, description=?, price=? WHERE id=?",
                      (name, description, price, id))
            conn.commit()
            flash("Product updated")
            return redirect('/admin')

        c.execute("SELECT * FROM products WHERE id=?", (id,))
        product = c.fetchone()
    return render_template("edit.html", product=product)

@app.route('/delete/<int:id>')
def delete_product(id):
    if not is_admin():
        return redirect('/login')

    with sqlite3.connect("shop.db") as conn:
        c = conn.cursor()
        c.execute("SELECT image FROM products WHERE id=?", (id,))
        img = c.fetchone()
        if img:
            try:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], img[0]))
            except:
                pass
        c.execute("DELETE FROM products WHERE id=?", (id,))
        conn.commit()
    flash("Product deleted")
    return redirect('/admin')

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
