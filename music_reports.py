from file_handling import import_data

ARTIST_NAME = 0
ALBUM_NAME = 1
RELEASE_YEAR = 2
GENRE = 3
LENGTH = 4


def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    specific_genre_albums = [album for album in albums if album[GENRE] == genre]
    return specific_genre_albums


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
