movies = [
    {
        "Title": "Waterworld",
        "Year": 1997,
        "imdbID": "tt0455840"
    },
    {
        "Title": "Waterworld2",
        "Year": 1997,
        "imdbID": "tt0455840"
    },
    {
        "Title": "Waterboy",
        "Year": 1997,
        "imdbID": "tt0455840"
    },
    {
        "Title": "Waterboy2",
        "Year": 2000,
        "imdbID": "tt0455840"
    },
    {
        "Title": "abc",
        "Year": 2000,
        "imdbID": "tt0455840"
    },
    {
        "Title": "abcd",
        "Year": 1997,
        "imdbID": "tt0455840"
    },
]

def fetch_all_movies():
    return movies

def getMovies(year, query):
    all_movies = fetch_all_movies()

    match_movies = []
    for movie in all_movies:
        if movie.get('Year') != year:
            continue

        lower_title = movie.get('Title').lower()
        query_match = False

        if query.startswith('*') and query.endswith('*'):
            found = lower_title.find(query[1:-1])
            if found >= 0:
                query_match = True
        elif query.startswith('*') and lower_title.endswith(query[1:]):
            query_match = True
        elif query.endswith('*') and lower_title.startswith(query[:-1]):
            query_match = True
        elif query == lower_title:
            query_match = True

        if query_match:
            match_movies.append([movie['imdbID'], movie['Title']])

    return match_movies

movies = getMovies(2000, '*aterb*')
print(movies)
