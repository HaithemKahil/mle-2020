import FeaturesUtils
import pandas as pd
from dataset_manager.DataSearchUtils import *


class NaiveRecommender:

    def __init__(self, movies, users, ratings) -> None:
        self.movies = movies
        self.users = users
        self.ratings = ratings
        self.similarity = FeaturesUtils.calculate_similarity_matrix(movies)

    def get_recommendations(self,user_id):
        top_movies = self.ratings[self.ratings['user_id'] == user_id].sort_values(by='rating', ascending=False).head(3)[
            'movie_id']
        index = ['movie_id', 'title', 'similarity']

        most_similars = []
        for top_movie in top_movies:
            most_similars += FeaturesUtils.get_most_similar(self.similarity, get_movie_name(self.movies, top_movie),
                                              get_movie_year(self.movies, top_movie))

        return pd.DataFrame(most_similars, columns=index).drop_duplicates().sort_values(by='similarity',
                                                                                        ascending=False).head(5)
