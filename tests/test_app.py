# Tests for your routes go here

def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        "Album(1, Doolittle, 1989, 1)",
        "Album(2, Surfer Rosa, 1988, 1)",
        "Album(3, Waterloo, 1974, 2)",
        "Album(4, Super Trouper, 1980, 2)",
        "Album(5, Bossanova, 1990, 1)",
        "Album(6, Lover, 2019, 3)",
        "Album(7, Folklore, 2020, 3)",
        "Album(8, I Put a Spell on You, 1965, 4)",
        "Album(9, Baltimore, 1978, 4)",
        "Album(10, Here Comes the Sun, 1971, 4)",
        "Album(11, Fodder on My Wings, 1982, 4)",
        "Album(12, Ring Ring, 1973, 2)"
    ])

def test_post_albums_success(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post("/albums", data={
        "title": "Midnights",
        "release_year": "2022",
        "artist_id": "3"
    })
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == "Album added successfully"

    get_response = web_client.get("/albums")
    last_album = get_response.data.decode("utf-8").split("\n")[-1]
    assert last_album == "Album(13, Midnights, 2022, 3)"

def test_post_albums_with_invalid_params(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400

    get_response = web_client.get("/albums")
    last_album = get_response.data.decode("utf-8").split("\n")[-1]
    assert last_album == "Album(12, Ring Ring, 1973, 2)"

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
