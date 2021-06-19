import sqlite3
import urllib.parse
import urllib.request
import urllib.error
import json
conn = sqlite3.connect('promatchesdb.sqlite')
cur = conn.cursor()

cur.execute('select radiant_score from ProMatch')
result=cur.fetchall()
print(result)
conn.commit()
