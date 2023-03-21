from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()

artist1 = Artist("Madonna")
artist_repository.create(artist1)
artist2 = Artist("Prince")
artist_repository.create(artist2)

album1 = Album("The Immaculate Collection", "Pop", artist1)
album_repository.create(album1)
album2 = Album("Purple Rain", "Pop", artist2)
album_repository.create(album2)

print(artist_repository.select(1))
print(album_repository.select(1))

print(artist_repository.select_all())
print(album_repository.select_all())

