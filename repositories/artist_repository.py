from db.run_sql import run_sql

from models.artist import Artist

def create(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist # can be optional if we don't need the artist returned

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values =[id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = Artist(result['name'], result['id'])
    return artist

def select_all():
    # set up an empty list to be returned
    artists = []
    # create a string of SQL
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['name'], row['id']) # translating the dictionary into Artist objects
        artists.append(artist)
    # return the list
    return artists
        
def update(artist):
    sql = "UPDATE artists SET name = %s WHERE id = %s" # FLAG and ask about tomo why not "UPDATE artists SET (name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)