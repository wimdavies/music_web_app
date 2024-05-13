import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['POST'])
def post_albums():
    db_connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(db_connection)
    album = Album(
        None,
        request.form["title"],
        request.form["release_year"],
        request.form["artist_id"]
    )

    # if "title" not in request.form or "release_year" not in request.form or "artist_id" not in request.form:
    #     return "Invalid parameters", 400
    # else:
    album_repository.create(album)
    return "Album added successfully"

@app.route('/albums', methods=['GET'])
def get_albums():
    db_connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(db_connection)
    albums = album_repository.all()
    return "\n".join([
        str(album) for album in albums
    ])

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

