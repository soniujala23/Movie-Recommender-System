import pickle
import streamlit as st
import requests
import pandas as pd
import os

st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.stButton>button {
    background-color: #E50914;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
.stSelectbox {
    color: black;
}
</style>
""", unsafe_allow_html=True)

# ---------------- FETCH POSTER ----------------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8"
        response = requests.get(url, timeout=5)

        print(response.status_code)   # 👈 ADD THIS
        data = response.json()
        print(data)                  # 👈 ADD THIS

        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    except Exception as e:
        print(e)
        return "https://via.placeholder.com/500x750?text=Error"


# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters


# ---------------- LOAD FILES SAFELY ----------------
base_dir = os.path.dirname(__file__)

movies_dict = pickle.load(open(os.path.join(base_dir, 'model/movie_list.pkl'), 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open(os.path.join(base_dir, 'model/similarity.pkl'), 'rb'))

# ---------------- UI ----------------
# ---------------- UI ----------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Title
st.markdown(
    "<h1 style='text-align: center; color: #E50914;'>🎬 Movie Recommender</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Find movies similar to your favorites 🍿</p>",
    unsafe_allow_html=True
)

# Dropdown
selected_movie = st.selectbox(
    "🔍 Search or select a movie",
    movies['title'].values
)

# Button
if st.button('🚀 Show Recommendations'):
    with st.spinner('Finding best movies for you... 🎥'):
        names, posters = recommend(selected_movie)

    st.markdown("## 🎯 Recommended Movies")

    cols = st.columns(5)

    for i in range(len(names)):
        with cols[i]:
            st.image(posters[i])
            st.markdown(
                f"<p style='text-align: center; font-weight: bold;'>{names[i]}</p>",
                unsafe_allow_html=True
            )
# ---------------- BUTTON ----------------
if st.button('Show Recommendation'):
    with st.spinner('Fetching recommendations... 🎥'):
        names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(len(names)):
        with cols[i]:
            st.image(posters[i])
            st.markdown(f"**{names[i]}**")
            