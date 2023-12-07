import numpy as np
import pandas as pd
import requests

# Define the URL for movie data
myurl = "https://liangfgithub.github.io/MovieData/movies.dat?raw=true"

# Fetch the data from the URL
response = requests.get(myurl)

# Split the data into lines and then split each line using "::"
movie_lines = response.text.split('\n')
movie_data = [line.split("::") for line in movie_lines if line]

# Create a DataFrame from the movie data
movies = pd.DataFrame(movie_data, columns=['movie_id', 'title', 'genres'])
movies['movie_id'] = movies['movie_id'].astype(int)

genres = list(
    sorted(set([genre for genres in movies.genres.unique() for genre in genres.split("|")]))
)


def get_displayed_movies():
    return movies.head(100)


def get_recommended_movies(new_user_ratings):
    return movies.head(10)


def get_popular_movies(genre: str):
    # Results generated by the algorithm laid out in System I.  Hardcoding the results
    # for all possible genres in the dataset in order to improve app performance.
    genre_to_popular_movies = {
        "Action": np.array([253, 1108, 802, 1106, 1848, 2374, 1107, 106, 1120, 1131]),
        "Adventure": np.array([253, 1108, 1106, 2955, 1107, 1120, 858, 1114, 2698, 1167]),
        "Animation": np.array([1066, 0, 708, 2898, 689, 1133, 3197, 2162, 3508, 2788]),
        "Children's": np.array([0, 858, 2898, 1025, 33, 2162, 3508, 1003, 2556, 581]),
        "Comedy": np.array([2651, 3010, 1652, 3367, 1107, 2203, 1059, 2785, 1066, 0]),
        "Crime": np.array([802, 49, 3413, 593, 287, 1485, 1131, 1123, 1143, 3203]),
        "Documentary": np.array([744, 3635, 3111, 1065, 2722, 239, 123, 1100, 1883, 2652]),
        "Drama": np.array([2651, 309, 513, 802, 1106, 1848, 579, 3367, 3152, 926]),
        "Fantasy": np.array([253, 1025, 2592, 1003, 2426, 2665, 240, 1993, 749, 2757]),
        "Film-Noir": np.array([1485, 527, 852, 1160, 861, 3203, 1175, 1192, 2005, 869]),
        "Horror": np.array([3054, 1124, 1186, 1129, 1288, 2511, 1166, 1817, 1236, 2462]),
        "Musical": np.array([858, 1196, 838, 853, 2108, 1130, 1767, 884, 997, 581]),
        "Mystery": np.array([1485, 843, 852, 1160, 1122, 863, 842, 564, 1192, 3488]),
        "Romance": np.array([1107, 851, 1120, 2203, 346, 1173, 1155, 908, 2488, 1139]),
        "Sci-Fi": np.array([253, 1106, 2374, 1120, 713, 575, 527, 1148, 1124, 1178]),
        "Thriller": np.array([2557, 579, 2374, 49, 593, 1485, 575, 843, 847, 1148]),
        "War": np.array([513, 1106, 1848, 106, 851, 1120, 713, 346, 1158, 1110]),
        "Western": np.array([3367, 1212, 2816, 1174, 3429, 1111, 576, 1191, 2823, 585]),
    }

    return movies.iloc[genre_to_popular_movies.get(genre, np.array([]))]
