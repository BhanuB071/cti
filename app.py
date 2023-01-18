from flask import Flask, render_template, g, request, redirect
import sqlite3 as sql


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/view", methods=["GET"])
def view():
    if request.method == "GET":
        print('hello')
        con = sql.connect('cti.db')
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select * from student_grades")

        results = cur.fetchall()
        con.close()
        grades = []

        for result in results:
            grade = dict(id=result[0], name=result[1], course=result[2], grade=result[3])
            grades.append(grade)

        print(grades)

        return render_template("view.html", grades=grades)

@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "GET":
        return render_template('add.html')

    if request.method == "POST":

        name = request.form.get("name")
        course = request.form.get("course")
        grade = request.form.get("grade")
        con = sql.connect('cti.db')
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("INSERT INTO student_grades (name, course, grade) VALUES (?, ?, ?)", (name, course, grade))
        con.commit()
        con.close()
        return render_template("add.html")