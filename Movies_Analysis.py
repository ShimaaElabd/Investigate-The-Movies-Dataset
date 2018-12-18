
# coding: utf-8

# 
# # Project: Movies Data Analysis
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# How can we measure a success of a movie ? -It could be by different parameters like:
# - The vote rate for the movie if it's highly rated like (8 or 9) in scale of 10 or very low rate like (4 or 5).
# - The budget of the movie, mostly the movie with high budget has a bigger probability to succeed.
# - The revenue of the movie ofcourse is a good indicator for the suceess of the movie.
# - The popularity of the movie and how much propaganda it has.
# - The genres or the type of the movie, maybe Action movies have the biggest revenues.
# - The cast, the crew or the production companies could give us an impact about success this movie.
# 
# So I'm going to digging into those questions, with data on the vote rate, cast, crew, budget, and revenues of several films, and analyze it .....................
# 
# other questions:-
# 
# - Which genres are most popular from year to year?
# - What kinds of properties are associated with the movie that has the highest revenue?

# In[114]:


# import needed packages
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# ### General Properties

# In[115]:


# Read the data
Movies_Analysis = pd.read_csv("tmdb-movies.csv")
Movies_Analysis.head(2)


# In[116]:


Movies_Analysis.shape


# In[117]:


# summary statistics
Movies_Analysis.describe()


# In[118]:


# more information about the data
Movies_Analysis.info()


# In[119]:


Movies_Analysis.nunique()


# In[120]:


# number of duplicated values
Movies_Analysis.duplicated().sum()


# In[121]:


# data types..
Movies_Analysis.dtypes


# 
# ### Data Cleaning 

# In[122]:


# At first i will copy the original data and work on the copied one.
movies = Movies_Analysis.copy()
movies.head(2)


# In[123]:


# determine number of null values.
movies.isnull().sum()


# ### Drop Extraneous Columns

# In[124]:


# drop columns from movies dataset
movies.drop(['id', 'imdb_id', 'homepage', 'tagline', 'keywords', 'overview' ], axis=1, inplace=True)

# confirm changes
movies.head(1)


# In[125]:


# view dimensions of dataset
movies.shape


# ## Drop Rows with Missing Values

# In[126]:


# view missing value count for the movies dataset
movies.isnull().sum()


# In[127]:


# drop rows with any null values in the dataset.
movies.dropna(inplace=True)


# In[128]:


# checks if any of columns in the dataset have null values.
movies.isnull().sum().any()


# In[129]:


# view dimensions of dataset
movies.shape


# In[130]:


# print number of duplicates in the movies dataset
print(movies.duplicated().sum())


# In[131]:


# drop duplicates in the dataset
movies.drop_duplicates(inplace=True)


# In[132]:


# print number of duplicates in the movies dataset
print(movies.duplicated().sum())


# In[133]:


movies.info()


# ### Draw Histogram for the movies dataset

# In[138]:


movies.hist(figsize=(20, 15));


# In[141]:


movies['production_companies'].value_counts()


# In[142]:


movies['genres'].value_counts()


# ### First, I chose The dependent variable to be the vote average and we could have many independent variables like:
# 
# - Budget
# - Popularity
# - Revenue
# - Genres
# 

# In[143]:


masterpiece_movie = movies.query('vote_average >= ' + str(8.5) )
remarkable_movie  = movies.query('vote_average >= ' + str(7.0) )
ordinary_movie    = movies.query('vote_average <= ' + str(7.0) )


# In[144]:


masterpiece_movie["vote_average"].mean()


# In[145]:


masterpiece_movie["vote_average"].hist( alpha = 0.6, bins=10, label = "masterpiece" )
remarkable_movie["vote_average"].hist( alpha = 0.6, bins=10, label = "remarkable" )
ordinary_movie["vote_average"].hist( alpha = 0.6, bins=10, label = "ordinary" )
plt.legend();


# ## From this graph we note that most of the movies in range of 5 to 7 (ordinary movie) class.

# In[171]:


masterpiece_movie.groupby('vote_average').mean()


# In[172]:


remarkable_movie.groupby('vote_average').mean()#.plot(kind='bar')


# In[148]:


ordinary_movie.groupby('vote_average').mean()


# ## The first independent variable ( The Budget ):-

# In[150]:


masterpiece_movie["budget"].hist( alpha = 0.5, label = "masterpiece" )
remarkable_movie["budget"].hist( alpha = 0.5,  label = "remarkable" )
ordinary_movie["budget"].hist( alpha = 0.5, label = "ordinary" )
plt.legend();


# - ### From this graph we noted that the (Masterpiece) class which refer to the highly rated movies, are very rare and have the highest budget.
# - ### The ( Ordinary and Remarkable) classes which refer to the movies with average rates, have the lowest budget.
# - ### The ( Ordinary) class is the most common class in this dataset.

# ## The second independent variable ( The Popularity ):-

# In[151]:


masterpiece_movie["popularity"].hist( alpha = 0.5, label = "masterpiece" )
remarkable_movie["popularity"].hist( alpha = 0.5, label = "remarkable" )
ordinary_movie["popularity"].hist( alpha = 0.5, label = "ordinary" )
plt.legend();


# - ### From this graph we noted that the (Masterpiece) class which refer to the highly rated movies, are very rare and have the highest Popularity.
# - ### The ( Ordinary and Remarkable) classes which refer to the movies with average rates, have the lowest popularity, almost from (0 to 5 ).
# - ### The ( Ordinary) class is the most common class in this dataset.

# ## The third independent variable ( The Revenu ):-

# In[176]:


masterpiece_movie["revenue"].hist( alpha = 0.5, label = "masterpiece" )
remarkable_movie["revenue"].hist( alpha = 0.5, label = "remarkable" )
ordinary_movie["revenue"].hist( alpha = 0.5, label = "ordinary" )
plt.legend();


# - ### From this graph we noted that the (Masterpiece) class, are also very rare and have the highest revenue.
# - ### The ( Ordinary and Remarkable) classes, have the lowest revenue.
# - ### The ( Ordinary) class is the most common class in this dataset.

# In[166]:


movies["release_year"].value_counts()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# **Questions:-** 

# # Which genres are most popular from year to year?

# In[167]:


classic_movies = movies.query('release_year >= ' + str(1960) +' & release_year<=' + str(1990))
classic_movies["genres"].mode()


# In[168]:


movies_2000s = movies.query('release_year >= ' + str(1990) +' & release_year<=' + str(2010))
movies_2000s["genres"].mode()


# In[169]:


movies_2018s = movies.query('release_year >= ' + str(2010) +' & release_year<=' + str(2018))
movies_2018s["genres"].mode()


# - ### from 1960 to 1990 the Comedy movies is the most popular
# - ### from 1990 to 2010 the Comedy movies is the most popular
# - ### from 2010 to 2018 the Drama movies is the most popular

# # What kinds of properties are associated with the movie that has the highest revenue?

# In[177]:


revenue = movies["revenue"].max()


# In[179]:


high_revenue = movies.query('revenue == ' + str(revenue) )


# In[180]:


high_revenue.head()


# ###  The properties  associated with the movie that has the highest revenue is :-
# - The budgetis higher than 	237000000
# - The revenue is higher than 2781505000
# - The director is James Cameron.
# - The genre is Action|Adventure|Fantasy|Science Fiction
# - The production companies is Ingenious Film Partners|Twentieth Century Fox
# - The vote average is 7.1

# <a id='conclusions'></a>
# ## Conclusions

# I aimed to find the parameters that help in the success of a movie like,
# 
# - The budget of the movie, and we found that the movie with high budget has a higher rate more than 7.
# - The revenue of the movie, and we found that the movie with high revenu has a high rate.
# - The popularity of the movie.
# 
# I also tried to investigate more and answer questions like:-
# - Which genres are most popular from year to year? 
# 
# Comedy in classic movies and drama recently.
# - What kinds of properties are associated with the movie that has the highest revenue?
# 
# The director is James Cameron and The budget is higher than 237000000 and The revenue is higher than 2781505000
# The genre is Action|Adventure|Fantasy|Science Fiction
# The production companies is Ingenious Film Partners|Twentieth Century Fox.
