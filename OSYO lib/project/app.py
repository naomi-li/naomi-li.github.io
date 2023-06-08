import os
import csv 
import sqlite3

from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for

# Configure application
app = Flask(__name__)
'''
def create_connection(db_file):
    """ create a database connection to the SQLite database
    :param db_file: database file
    :return: Connection object or None
    """
'''

def get_db():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

'''
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
'''


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


ROWS_PER_PAGE = 50

@app.route("/all/")
def all():
    """
    Query all rows in the data table
    :param db_conn: the Connection object
    :return:
    """
    # find the appropriate information
    conn = get_db()
    all = conn.execute('SELECT * FROM data').fetchall()
    conn.close()
    return render_template("all.html", all=all)

@app.route("/index")
def admin():
    return redirect(url_for("index"))


@app.route("/all/<id>")
def music(id):
    conn = get_db()
    cursor = conn.execute('SELECT * FROM data WHERE id=?', (id,))
    music = cursor.fetchone()
    conn.close()
    
    if music == None:
        return render_template("apology.html", error=404)
    return render_template("music.html", music=music)

@app.route('/all/<string:id>', methods=['GET'])
def get_id(id):
    return id

@app.route("/all/ensemble/<ensemble>")
def ensemble(ensemble):
    ensemble = ensemble.upper()
    conn = get_db()
    all = conn.execute("SELECT * FROM data WHERE Ensemble LIKE '%'||?||'%'", (ensemble,)).fetchall()
    conn.close()
    return render_template("ensemble.html", all=all, ensemble=ensemble)







if __name__ == "__main__":
    app.run(debug=True)
