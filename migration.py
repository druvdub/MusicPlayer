import MySQLdb
import mysql, mysql.connector
connectio = mysql.connector.connect(host="localhost", user="beta", password="password", database="musicplayer")

cursr = connectio.cursor()

cursr.execute("""CREATE TABLE music (
    id int primary key auto_increment,
    song_name varchar(255), 
    artist varchar(255), 
    publish_year int, 
    album varchar(255), 
    address varchar(255), 
    genre varchar(255)
    )""")

cursr.execute("""CREATE TABLE playlist (
    id int primary key AUTO_INCREMENT,
    playlist_name varchar(255)
    )""")

cursr.execute("""CREATE TABLE playlist_songs (
    track_number int,
    track_id int,
    playlist_id int
    )""")

