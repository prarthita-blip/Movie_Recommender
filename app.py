#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
from scipy.sparse import csr_matrix
import argparse
import pandas as pd
from pywebio import start_server

import joblib
import numpy as np

knn = joblib.load('recommendation_model.pkl')
df =pd.read_csv("movie-user-rating.csv")
data_movie=pd.read_csv("movie.csv")

user_movie_table = df.pivot_table(index = ["movieId"],columns = ["userId"],values = "rating").fillna(0)

csr_data = csr_matrix(user_movie_table.values)
user_movie_table.reset_index(inplace=True)


app = Flask(__name__)


def movie_app():
    movie_name=input("Write full name of the Movie")
    
    if movie_name[:4]=="The ":
        x = movie_name.split(" ",1)
        movie_name=x[1]+", "+x[0]
        
    n_movies_to_reccomend = 10
    movie_list = data_movie[data_movie['title'].str.contains(movie_name)]  
    if len(movie_list):        
        movie_idx= movie_list.iloc[0]['movieId']
        movie_idx = user_movie_table[user_movie_table['movieId'] == movie_idx].index[0]
        distances , indices = knn.kneighbors(csr_data[movie_idx],n_neighbors=n_movies_to_reccomend+1)    
        rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
        recommend_frame = []
        for val in rec_movie_indices:
            movie_idx = user_movie_table.iloc[val[0]]['movieId']
            idx = data_movie[data_movie['movieId'] == movie_idx].index
            put_text(data_movie.iloc[idx]['title'].values[0])
    else:
        put_text("No movies found. Please check your input")

    
    
    
        
    
    
    
        
app.add_url_rule('/tool', 'webio_view', webio_view(movie_app),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(movie_app, port=args.port)


# In[ ]:




