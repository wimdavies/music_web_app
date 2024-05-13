from lib.album import Album
from lib.album_repository import AlbumRepository

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection)
    albums = repository.all()
    assert len(albums) == 12
    assert albums[0].id == 1

def test_find_a_record(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection)
    album = repository.find(1)
    assert album.id == 1

def test_create_a_record(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection)
    album = Album(None, "Evermore", 2020, 3)
    assert repository.create(album) == None

    albums = repository.all()
    assert len(albums) == 13
    assert albums[-1].title == "Evermore"

def test_delete_a_record(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection)
    assert repository.delete(1) == None

    albums = repository.all()
    assert len(albums) == 11
    assert albums[0].id == 2