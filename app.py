from flask import Flask, render_template, request, url_for, redirect, Response, abort
import sqlite3 as sql

app=Flask(__name__, static_url_path="/static")


#create function to handle db connection
def cmsconn():
    conn=sql.connect('project-app/cms.db')
    conn.row_factory=sql.Row
    return conn

@app.route("/") 
@app.route("/index")
def index():
    return render_template('index.html', title="Home")

@app.route("/products")
def product():
    return render_template("products.html", title="Products")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/users")
def users():
    userTbl=cmsconn()
    cursor=userTbl.cursor()
    cursor.execute('select * from users')
    allUsers=cursor.fetchall()
    return render_template("users.html", title="Users", aUser=allUsers)

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method=="POST":
        #userid=request.form[""] manual id uses this line
        fname=request.form["Firstname"] 
        lname=request.form["Lastname"] 
        email=request.form["Email"] 
        image=request.form["ProfileImg"]
        userTbl=cmsconn()
        cursor=userTbl.cursor()
        userid=cursor.lastrowid
        cursor.execute('insert into users VALUES(?,?,?,?,?)', userid,fname,lname,email,image)
        userTbl.commit()
        userTbl.close()
        return redirect(url_for('users'))
    return render_template("add_user.html", title="add_user")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3500)
# ALWAYS the last line 