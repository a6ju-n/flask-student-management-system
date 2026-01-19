import sqlite3
from flask import Flask, render_template, request, redirect,session,url_for
app = Flask(__name__, template_folder='HTML')
app.secret_key = "this_is_a_secret_key_123"
def dbs():
    return sqlite3.connect("dbase.db")
@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST': 
        conn=dbs()
        cursor=conn.cursor()
        a=request.form.get('usr')
        b=str(request.form.get('pwd'))
        cursor.execute("SELECT ID FROM faculty WHERE ID=? AND pwd=? ",(a,b))
        user = cursor.fetchone()
        conn.close()
        if user:
            return render_template("trmain.html")
        else:
            return render_template('err.html')
    return render_template("login.html")

@app.route('/denter', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        roll = request.form['Id']
        name = request.form['nme']
        dept = request.form['dept']
        marks = request.form['mark']
        pwd= request.form['pwd']
        conn = dbs()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO student (ID,Name,Department,Mark,pwd)  VALUES (?,?,?,?,?)",
            (roll,name, dept, marks,pwd)
        )
        conn.commit()
        conn.close()
        return redirect("/view")
    return render_template("dataenter.html")

@app.route('/view')
def index():
    conn = dbs()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    conn.close()
    

    return render_template('view.html', students=students)

@app.route('/delete/<int:id>')
def delete(id):
    conn = dbs()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE ID = ? ", (id,))
    print(id)
    conn.commit()
    conn.close()

    return redirect('/view')

a=0
@app.route('/stud',methods=['GET','POST'])
def login2():
    if request.method=='POST': 
        conn=dbs()
        cursor=conn.cursor()
        a=request.form.get('id')
        b=str(request.form.get('pwd'))
        cursor.execute("SELECT ID FROM student WHERE ID=? AND pwd=? ",(a,b))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['stud_id'] = a 
            return redirect(url_for('index2'))
        else:
            return render_template('err.html')
    return render_template("studlog.html")

@app.route('/view2')
def index2():
    a = session.get('stud_id')
    print(a)
    conn = dbs()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student where ID=?",(a,))
    students = cursor.fetchall()
    conn.close()
    

    return render_template('studmain.html', students=students)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = dbs()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student where ID=?",(id,))
    students = cursor.fetchone()
    print("students =", students)
    print("type(students) =", type(students))
    if request.method == 'POST':
        roll = request.form['Id']
        name = request.form['nme']
        dept = request.form['dept']
        marks = request.form['mark']
        pwd= request.form['pwd']
       
        cursor.execute("UPDATE student SET  ID = ?,Name = ?,Department = ?,Mark = ?,pwd = ? WHERE ID =? ", 
                       (roll,name,dept,marks,pwd,id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template("update.html",students=students,id=id)

if __name__ == '__main__':
    app.run(debug=True)

