from lib.album import Album

def test_album_constructs():
    album = Album(1, "Test Title", 1999, 2)
    album.id == 1
    album.title == "Test Title"
    album.release_year == 1999
    album.artist_id == 2