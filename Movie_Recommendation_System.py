#Movie_Recommendation_System:

#import modules
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#1.Load movie dataset
file_id = "YOUR_FILE_ID_HERE"
url = f"https://drive.google.com/uc?id={file_id}"
movies = pd.read_csv(url)

#2.Clean missing values
movies['genres']=movies['genres'].fillna("")
movies['overview']=movies['overview'].fillna("")

#3.combine the imp movie information
movies["features"]=(movies["genres"]+" "+movies["overview"])

#4.convert text into numerical vectors
vectorizer=TfidfVectorizer(stop_words="english")
feature_vectors=vectorizer.fit_transform(movies["features"])

#5.calculate similarity between movies
similarity_matrix=cosine_similarity(feature_vectors)

#6.create movie index
movie_indices=pd.Series(movies.index,index=movies["title"].str.lower()).drop_duplicates()

#7.recommendation feature
def recommend_movies(movie_title,number_of_movies=5):
    movie_title=movie_title.lower()
    if movie_title not in movie_indices:
        print("movie is not found in dataset")
        return
    
    movie_index=movie_indices[movie_title]
    similarity_scores=list(enumerate(similarity_matrix[movie_index]))
    similarity_scores=sorted(similarity_scores,key=lambda x:x[1],reverse=True)
    print(f"\nmovies similer to '{movies.iloc[movie_index]['title']}':\n")
    count=0

    for index, score in similarity_scores[1:]:
        print(
            f"{count + 1}. "
            f"{movies.iloc[index]['title']} "
            f"(Similarity: {score:.2f})"
            )
        count += 1
        if count == number_of_movies:
            break

#8.User interface
print("="*45)
print("-----MOVIE RECOMMENDATION SYSTEM-----")
print("="*45)

st.title("🎬 Movie Recommendation System")

movie = st.text_input("Enter a movie name")

if st.button("Recommend"):
    if movie.strip() == "":
        st.warning("Please enter a movie name.")
    elif movie.lower() == "exit":
        st.info("Thank you!")
    else:
        recommend_movies(movie)
