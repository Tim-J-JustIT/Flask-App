import sqlite3

#conn=sqlite3.connect(r'project-app\dbCon.py')
#connect method

conn=sqlite3.connect('project-app/cms.db')
cursor= conn.cursor()