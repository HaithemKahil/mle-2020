from dataset_manager.DataSearchUtils import *
from dataset_manager.StaticEntries import genre_cols


def calculate_similarity_matrix(movies):
    similarity = movies[genre_cols].values.dot(movies[genre_cols].values.T)
    return similarity


def get_most_similar(similarity, movies, movie_name, year=None, top=10):
    index_movie = get_movie_id(movies, movie_name, year)
    best = similarity[index_movie].argsort()[::-1]
    return [(ind, get_movie_name(movies, ind), similarity[index_movie, ind]) for ind in best[:top] if ind != index_movie]
