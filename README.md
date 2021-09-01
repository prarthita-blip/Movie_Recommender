# Movie_Recommender

Movie Recommending Website:
 
 

Install

The project requires python and following python libraries installed:
1.	numpy
2.	pandas
3.	matplotlib
4.	flask
5.	PyWebIO

The project has been executed using a jupyter notebook.

Data

The dataset used in this project is the ‘MovieLens(20 M) dataset’ available at Kaggle.
There are several csv files in the dataset. The one that are used in this project are:
1.	movie.csv
2.	rating.csv

Code

The movie recommending model uses KNN algorithm in order to perform Item to Item Collaborative filtering. It takes a movie name as input and then finds ten movies which are closest to that input movie and finally recommends those movies to the user.
The project uses flask and PyWebIO to build the website and the website is deployed on Heroku.

Result

I tested the project with several movies and the recommendation received from it was quite satisfactory.
