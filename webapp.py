import pickle
import streamlit as st
import requests
import pandas as pd


st.header(' MOVIE RECOMMENDER ')

def get_poster(id_of_movie):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=fb4a1d7e4b966e203091fe688e269981".format(id_of_movie)
    to_get_data = requests.get(url)
    to_get_data = to_get_data.json()
    poster_path = to_get_data['poster_path']
    path_of_poster = "https://image.tmdb.org/t/p/w500/" + poster_path
    return path_of_poster

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    movies_recommended = []
    poster_recommended = []
    for i in distances[1:10]:

        # to get the movie poster

        id_of_movie = movies.iloc[i[0]].movie_id

        poster_recommended.append(get_poster(id_of_movie))

        movies_recommended.append(movies.iloc[i[0]].title)

    return movies_recommended, poster_recommended



movies = pickle.load(open('movie_list.pkl','rb'))

similarity = pickle.load(open('movies_similarity.pkl','rb'))

movie_list = movies['title'].values
movie_selected = st.selectbox(
    "TYPE NAME OF THE MOVIE",
    movie_list
)

if st.button('Click here for the movie results'):

    movies_recommended,poster_recommended = recommend(movie_selected)

    column1, column2, column3, column4, column5, column6, column7 = st.columns(7)

    with column1:
        st.text(movies_recommended[0])
        st.image(poster_recommended[0])

    with column2:
        st.text(movies_recommended[1])
        st.image(poster_recommended[1])

    with column3:
        st.text(movies_recommended[2])
        st.image(poster_recommended[2])

    with column4:
        st.text(movies_recommended[3])
        st.image(poster_recommended[3])

    with column5:
        st.text(movies_recommended[4])
        st.image(poster_recommended[4])

    with column6:
        st.text(movies_recommended[5])
        st.image(poster_recommended[5])

    with column7:
         st.text(movies_recommended[6])
         st.image(poster_recommended[6])




