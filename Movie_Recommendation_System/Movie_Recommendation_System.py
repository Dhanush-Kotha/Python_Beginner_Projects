# ============================================================
# MOVIE RECOMMENDATION SYSTEM
# ============================================================

import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# 1. STREAMLIT PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)


# ============================================================
# 2. APPLICATION TITLE
# ============================================================

st.title("🎬 Movie Recommendation System")

st.write(
    "Enter a movie name and get 5 similar movie recommendations."
)


# ============================================================
# 3. LOAD MOVIE DATASET
# ============================================================

@st.cache_data
def load_movie_data():

    movies = pd.read_csv("Movie_Recommendation_System/movies.csv.zip")

    return movies


# Load dataset
try:

    movies = load_movie_data()

except FileNotFoundError:

    st.error("❌ movies.csv.zip was not found.")

    st.info(
        "Make sure movies.csv.zip is in the same folder "
        "as this Python file."
    )

    st.stop()


# ============================================================
# 4. CLEAN MISSING VALUES
# ============================================================

movies["genres"] = movies["genres"].fillna("")
movies["overview"] = movies["overview"].fillna("")


# ============================================================
# 5. COMBINE MOVIE INFORMATION
# ============================================================

movies["features"] = (
    movies["genres"] + " " + movies["overview"]
)


# ============================================================
# 6. CONVERT TEXT INTO NUMERICAL VECTORS
# ============================================================

@st.cache_resource
def create_tfidf_vectors(features):

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    feature_vectors = vectorizer.fit_transform(
        features
    )

    return feature_vectors


feature_vectors = create_tfidf_vectors(
    movies["features"]
)


# ============================================================
# 7. CALCULATE COSINE SIMILARITY
# ============================================================

# IMPORTANT:
# Do NOT use @st.cache_data or @st.cache_resource here.
# feature_vectors is a scipy sparse matrix and Streamlit
# may not be able to hash it.

similarity_matrix = cosine_similarity(
    feature_vectors
)


# ============================================================
# 8. CREATE MOVIE INDEX
# ============================================================

movies["title_lower"] = (
    movies["title"]
    .astype(str)
    .str.strip()
    .str.lower()
)

movie_indices = pd.Series(
    movies.index,
    index=movies["title_lower"]
).drop_duplicates()


# ============================================================
# 9. MOVIE RECOMMENDATION FUNCTION
# ============================================================

def recommend_movies(
    movie_title,
    number_of_movies=5
):

    # Clean user input
    movie_title = movie_title.strip().lower()

    # Check whether movie exists
    if movie_title not in movie_indices:

        return None

    # Get movie index
    movie_index = movie_indices[movie_title]

    # Get similarity scores
    similarity_scores = list(
        enumerate(
            similarity_matrix[movie_index]
        )
    )

    # Sort from highest similarity to lowest
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Store recommendations
    recommendations = []

    # Skip the first result because it is
    # the movie entered by the user
    for index, score in similarity_scores[1:]:

        recommendations.append(
            {
                "title": movies.iloc[index]["title"],
                "score": score
            }
        )

        if len(recommendations) == number_of_movies:

            break

    return recommendations


# ============================================================
# 10. STREAMLIT INPUT
# ============================================================

st.subheader("🔎 Find Similar Movies")

movie = st.text_input(
    "Enter a movie name:",
    placeholder="Example: Avatar"
)


# ============================================================
# 11. RECOMMEND BUTTON
# ============================================================

if st.button(
    "🎬 Recommend",
    type="primary"
):

    # --------------------------------------------------------
    # EMPTY INPUT
    # --------------------------------------------------------

    if movie.strip() == "":

        st.warning(
            "⚠️ Please enter a movie name."
        )


    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    elif movie.strip().lower() == "exit":

        st.info(
            "👋 Thank you for using the Movie Recommendation System!"
        )


    # --------------------------------------------------------
    # RECOMMEND MOVIES
    # --------------------------------------------------------

    else:

        recommendations = recommend_movies(
            movie
        )


        # ----------------------------------------------------
        # MOVIE NOT FOUND
        # ----------------------------------------------------

        if recommendations is None:

            st.error(
                f"❌ '{movie}' was not found in the dataset."
            )

            st.info(
                "Please check the spelling and try another movie."
            )


        # ----------------------------------------------------
        # DISPLAY RECOMMENDATIONS
        # ----------------------------------------------------

        else:

            st.success(
                f"✅ Movies similar to '{movie.title()}'"
            )

            st.subheader(
                "🍿 Recommended Movies"
            )

            # Display recommendations
            for i, recommendation in enumerate(
                recommendations,
                start=1
            ):

                movie_name = recommendation["title"]

                score = recommendation["score"]


                # Movie name
                st.write(
                    f"### {i}. 🎬 {movie_name}"
                )


                # Similarity score
                st.caption(
                    f"Similarity Score: {score:.2f}"
                )


                # Separator
                st.divider()
