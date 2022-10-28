#CRESSWELL Alex Streamlit Assignment App

import streamlit as st
import requests

st.title("IMDB Movie Search")
title = st.text_input("Enter a movie title and press enter:")

if title:
    try:
        url = f'http://www.omdbapi.com/?t={title}&apikey=f3472bb6'
        print=(url)
        re = requests.get(url)
        re = re.json()
        mainColumn, secondaryColumn = st.columns([1,2])

        with mainColumn:
            st.image(re['Poster'])

        with secondaryColumn:
            st.subheader(re['Title'])
            st.caption(f"Genre: {re['Genre']}")
            st.caption(f"Year: {re['Year']}")
            st.caption(f"Director: {re['Director']} Main Cast: {re['Actors']}")
            st.write(re['Plot'])
            st.text(f"Rating: {re['imdbRating']}") 
            st.progress(float(re['imdbRating'])/10)

    except:
        st.error("There is no movie with that title, please try again.")
