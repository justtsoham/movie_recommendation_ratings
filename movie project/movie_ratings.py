# movie_ratings.py
import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('movies.csv')

# Average rating per genre
avg_rating = movies.groupby('Genre')['Rating'].mean()
print(avg_rating)

# Plot
avg_rating.sort_values().plot(kind='barh', figsize=(8,5))
plt.title('Average Movie Rating by Genre')
plt.xlabel('Average Rating')
plt.tight_layout()
plt.show()