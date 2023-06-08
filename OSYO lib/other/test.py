import os
import csv 
import sqlite3

from flask import Flask, flash, jsonify, redirect, render_template, request, session

#configure application
app = Flask(__name__)



@app.route("/")
def index():
    return "HI"

@app.route("/all")
def all():
    return "ALL"

if __name__ == "__main__":
    app.run()