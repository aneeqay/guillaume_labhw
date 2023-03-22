from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()

# create aritsts
artist1 = Artist("Madonna")
artist_repository.create(artist1)
artist2 = Artist("Prince")
artist_repository.create(artist2)

# create albums
album1 = Album("The Immaculate Collection", "Pop", artist1)
album_repository.create(album1)
album2 = Album("Purple Rain", "Pop", artist2)
album_repository.create(album2)
album3 = Album("Vogue", "Pop", artist1)
album_repository.create(album3)
print(album3.title)

# update album
album3.title = "The White Album"
album_repository.update(album3)
print(album3.title)

# update album
artist2.name = "The artist formerly known as Prince"
artist_repository.update(artist2)
print(artist2.name)

# # print function results
print(artist_repository.select(1))
print(album_repository.select(1))

print(artist_repository.select_all())
print(album_repository.select_all())

print(album_repository.albums_by_artist(artist1))

album_repository.delete(album2.id)
print(album_repository.select_all())
# print(album2.__dict__)

artist_repository.delete(artist1.id)
print(artist_repository.select_all())
print(album_repository.select_all())

