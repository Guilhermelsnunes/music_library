import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# album_repository.delete_all()
# artist_repository.delete_all()


artist1 = Artist("Luciano Pavarotti")
artist_repository.save(artist1)
artist2 = Artist("Frank Sinatra")
artist_repository.save(artist2)

artist_repository.select_all()

album1 = Album("The 50 Gratest Tracks", "opera", artist1)
album_repository.save(album1)

album2 = Album("The Very Best Of Frank Sinatra", "pop", artist2)
album_repository.save(album2)

artists = artist_repository.select_all()
albums = album_repository.select_all()

for artist in artists:
    print(artist.__dict__)

for album in albums:
    print(album.__dict__)

pdb.set_trace()