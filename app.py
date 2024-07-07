from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/img/products'

# PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yllxstcj:1p3sJpJ3a-ywj6qIw_orkDueuNgKXJ9n@motty.db.elephantsql.com/yllxstcj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Settings
app.secret_key = 'mysecretkey'

# Model definition
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    photo = db.Column(db.Text)
    amount = db.Column(db.Integer, nullable=False)

@app.route("/")
def index():
    products = Products.query.all()
    return render_template("index.html", products=products)

@app.route('/register_product', methods=['GET', 'POST'])
def addProduct():
    return render_template("register.html")

@app.route('/add_product', methods=['POST'])
def formProduct():
    if request.method == 'POST':
        category = request.form['category']
        name = request.form['name']
        price = request.form['price']
        amount = request.form['amount']
        if 'photo' in request.files:
            photo_file = request.files['photo']
            if photo_file.filename != '':
                filename = secure_filename(photo_file.filename)
                photo_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                new_product = Product(category=category, name=name, price=price, amount=amount, photo=filename)
                db.session.add(new_product)
                db.session.commit()
                flash("Product added successfully")
        return redirect(url_for('index'))

@app.route("/edit/<int:id>")
def getProduct(id):
    product = Product.query.get_or_404(id)
    return render_template('edit.html', product=product)

@app.route("/update/<int:id>", methods=['POST'])
def updateProduct(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.category = request.form['category']
        product.name = request.form['name']
        product.price = request.form['price']
        product.amount = request.form['amount']
        if 'photo' in request.files:
            photo_file = request.files['photo']
            if photo_file.filename != '':
                filename = secure_filename(photo_file.filename)
                photo_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                product.photo = filename
        db.session.commit()
        flash("Product updated successfully")
        return redirect(url_for('index'))

@app.route("/delete/<int:id>")
def deleteProduct(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash("Product deleted successfully")
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))
