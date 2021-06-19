# this program gets the latest 10000 pro matches every time it runs
import sqlite3
import urllib.parse
import urllib.request
import urllib.error
import json
conn = sqlite3.connect('promatchesdb.sqlite')
cur = conn.cursor()
cur.execute('''create table if not exists ProMatch(
           match_id text primary key,
 duration integer,
start_time integer,
radiant_team_id text,
radiant_name text,
dire_team_id  text,
dire_name text,
leagueid text,
league_name text,
series_id text,
series_type text,
radiant_score integer,
dire_score integer,
radiant_win integer)''''')
url='https://www.opendota.com/api/proMatches'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=url, headers=headers)

result=urllib.request.urlopen(req).read()

data=json.loads(result)

for d in data:
    cur.execute('''insert or ignore into ProMatch values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', ([l for l in d.values()]))
conn.commit()
last_match_id=data[99]['match_id']
for i in range(99):
    last_match_id=data[99]['match_id']
    url = 'https://www.opendota.com/api/proMatches?less_than_match_id='+str(last_match_id)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    result = urllib.request.urlopen(req).read()
    data = json.loads(result)
    for d in data:
        cur.execute('''insert or ignore into ProMatch values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', ([l for l in d.values()]))

    conn.commit()
    last_match_id = data[99]['match_id']
