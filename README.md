# Movie_Recommender

Install

The project requires python and following python libraries installed:
1.	numpy
2.	pandas
3.	matplotlib
The project has been executed using a jupyter notebook.

Data

The dataset used in this project is the ‘MovieLens(20 M) dataset’ available at Kaggle.
There are several csv files in the dataset. The one that are used in this project are:
1.	movie.csv
2.	rating.csv

Code

The project uses a simple item based collaborative filtering method to recommend 5 movies to the user based on a movie he/she saw recently. It takes the movie-title and rating of each user for each movie and forms a user-item matrix. 
The code also analyses some basic features like the average rating given by users, the movies with highest average rating and the movies with highest and lowest view count to get an idea about the dataset.
Finally, the code calculates Pearson correlation between item(movie) rows and the movies with top 5 correlation values are returned as recommendation.

Result

I tested the project with several movies and the recommendation received from it was quite satisfactory.
