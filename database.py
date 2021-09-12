import MySQLdb
import mysql, mysql.connector

connectio = mysql.connector.connect(host="localhost", user="beta", password="password", database="musicplayer")

cursor = connectio.cursor()

# insert a song to music table with metadata

def insert_song(song_name, artist, publish_year, album, address, genre):
    cursor.execute("INSERT INTO music(song_name, artist, publish_year, album, address, genre) VALUES (%(song)s,%(artiste)s,%(pubyr)s,%(album)s,%(address)s,%(genre)s)",{"song":song_name, "artiste":artist, "pubyr":publish_year, "album":album, "address":address, "genre":genre})
    connectio.commit()

# delete a song by id

def delete_song_by_id(id):
    cursor.execute("DELETE from music where id = %(id)s",{"id":id})
    cursor.execute("DELETE from playlist_song where track_id = %(track_id)s",{"track_id":id})
    connectio.commit()

def get_song_by_address(address):
    cursor.execute("SELECT * from music where address = %(address)s",{"address":address})
    result = cursor.fetchall()
    return result

def get_songs():
    cursor.execute("select * from music")
    result = cursor.fetchall()
    return result

def get_album(album):    
    cursor.execute("SELECT * FROM music WHERE album = %(album)s",{"album":album})
    new_list = cursor.fetchall()
    return new_list

def get_artist(artist):
    cursor.execute("SELECT * FROM music WHERE artist = %(artist)s",{"artist":artist}) 
    new_list = cursor.fetchall() 
    return new_list

def get_genre(genre):
    cursor.execute("SELECT * from music WHERE genre = %(genre)s",{"genre":genre} ) 
    new_list = cursor.fetchall()
    return new_list

def get_albums():
    cursor.execute("SELECT DISTINCT album FROM music ")
    new_list = cursor.fetchall() 
    return new_list

def get_artists():
    cursor.execute("SELECT DISTINCT artist FROM music ") 
    new_list = cursor.fetchall() 
    return new_list 

def get_genres():
    cursor.execute("SELECT DISTINCT genre FROM music " ) 
    new_list = cursor.fetchall() 
    return new_list

def get_playlist(id):
    cursor.execute("""SELECT track_id, address from playlist_song inner join music on playlist_song.track_id = music.id where playlist_id = %(plid)s order by playlist_song.track_number""",{"plid":id})
    new_list = cursor.fetchall()
    return new_list

def get_playlists():
    cursor.execute("SELECT DISTINCT playlist_songs.playlist_id, playlist.playlist_name FROM playlist_songs inner join playlist on playlist.id=playlist_songs.playlist_id")
    new_list = cursor.fetchall()
    return new_list

#add a new playlist with all songs user wants 

def add_playlist(playlist_name, song_list):
    cursor.execute("INSERT INTO playlist(playlist_name) VALUES (%(val)s) ",{"val":playlist_name})     
    element = cursor.lastrowid
    new_list = []
    for i in range(len(song_list) ) :
        new_list.append((i + 1, song_list[i], element,))
    print(new_list)
    cursor.executemany("INSERT INTO Playlist_song(track_number, track_id, playlist_id) VALUES (%s, %s, %s)", new_list) 
    connectio.commit()


#delete a playlist by its name which user gives us

def delete_playlist(playlist_name):
    cursor.execute("DELETE FROM playlist WHERE id = %(id)s",{"id":playlist_name})
    cursor.execute("DELETE FROM playlist_song WHERE playlist_id = %(plid)s ",{"plid":playlist_name})
    connectio.commit()





