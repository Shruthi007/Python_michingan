import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('new_data.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')


def lookup(d, key):
	found = False
	for child in d:
		if found : return child.text
		if child.tag == 'key' and child.text == key :
			found= True
	return None
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'Library.xml'
stuff = ET.parse(fname)
data = stuff.findall('dict/dict/dict')
for x in data:
	if (lookup(x, 'Track ID') is None ) : continue
	
	name= lookup(x,'Name')
	artist=lookup(x,'Artist')
	album=lookup(x,'Album')
	count=lookup(x,'Count')
	rating=lookup(x,'Rating')
	length=lookup(x,'Total Time')
	genre=lookup(x, 'Genre')
	print(name)
	if name is None or artist is None or album is None or genre is None : continue

	cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES( ? )''', ( artist,))
	cur.execute('''SELECT id FROM Artist WHERE name = ?''',(artist,))
	artist_id = cur.fetchone()[0]

	cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES( ? )', (genre,))
	cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
	genre_id = cur.fetchone()[0]

	cur.execute('INSERT OR IGNORE INTO Album(title,artist_id) VALUES( ?,? )', (album,artist_id))
	cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
	album_id = cur.fetchone()[0]

	cur.execute('INSERT OR REPLACE INTO Track(title, album_id, genre_id, len, rating, count) VALUES( ?, ?, ?, ?, ?, ? )', (name, album_id, genre_id, length, rating, count ))
	
	conn.commit()




