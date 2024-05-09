from dbCon import *

cursor.execute("""
CREATE TABLE "users" (
    "UserID"    INTEGER NOT NULL UNIQUE,
    "Firstname"    TEXT,
    "Lastname"    TEXT,
    "Email"    TEXT,
    "ProfileImg" BLOB,
    PRIMARY KEY("UserID" AUTOINCREMENT)
)""")