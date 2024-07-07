from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/img/products'

#MySQL connection
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='gaming_products'
mysql=MySQL(app)

#settings
app.secret_key='mysecretkey'

@app.route("/")
def index():
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM products')
    data=cur.fetchall()
    return render_template("index.html",products=data)

@app.route('/register_product', methods=['GET','POST'])
def addProduct():
    return render_template("register.html")

@app.route('/add_product',methods=['POST'])
def formProduct():
    if request.method== 'POST':
        category=request.form['category']
        name=request.form['name']
        price=request.form['price']
        amount=request.form['amount']
        photo=request.files['photo']
        if 'photo' in request.files:
            photo_file=request.files['photo']
            if photo_file.filename != '':
                filename = secure_filename(photo_file.filename)
        photo_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO products (category,name,price,amount,photo) VALUES (%s,%s,%s,%s,%s)',(category,name,price,amount,filename))
        mysql.connection.commit()
        flash("Contact added successfully")
        return redirect(url_for('index'))


@app.route("/edit/<id>")
def getProduct(id):
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM products WHERE id=%s',(id,))
    data=cur.fetchall()
    return render_template('edit.html',product=data[0])

@app.route("/update/<id>",methods=['POST'])
def updateProduct(id):
    if request.method== 'POST':
        category=request.form['category']
        name=request.form['name']
        price=request.form['price']
        amount=request.form['amount']
        photo=request.files['photo']
        if 'photo' in request.files:
            photo_file=request.files['photo']
            if photo_file.filename != '':
                filename = secure_filename(photo_file.filename)
        photo_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cur=mysql.connection.cursor()
        cur.execute("""
                UPDATE products
                SET category=%s,
                    name=%s,
                    price=%s,
                    amount=%s,
                    photo=%s
                WHERE id=%s
                """,(category,name,price,amount,filename,id))
        mysql.connection.commit()
        flash("Contact added successfully")
        return redirect(url_for('index'))
    
    
@app.route("/delete/<string:id>")
def deleteProduct(id):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM products WHERE id={0}'.format(id))
    mysql.connection.commit()
    flash("Contact deleted successfully")
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))

""" Prueba de cambios """