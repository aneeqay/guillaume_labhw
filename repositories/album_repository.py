from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def create(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values =[id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        album = Album(result['title'], result['genre'], result['artist_id'], result['id'])
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        album = Album(row['title'], row['genre'], row['artist_id'], row['id'])
        albums.append(album)
    return albums

def albums_by_artist(artist):
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    albums = []
    for row in results:
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)