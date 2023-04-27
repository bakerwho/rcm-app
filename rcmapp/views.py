from django.shortcuts import render
from .models import Movie, Rating

def recommend_movies(request):
    # Retrieve all movies
    movies = Movie.objects.all()

    # Calculate average rating for each movie
    movie_ratings = []
    for movie in movies:
        ratings = Rating.objects.filter(movie=movie)
        if ratings:
            avg_rating = sum(rating.rating for rating in ratings) / len(ratings)
            movie_ratings.append((movie, avg_rating))

    # Sort movies by average rating in descending order
    movie_ratings.sort(key=lambda x: x[1], reverse=True)

    # Get top 10 movies
    top_movies = movie_ratings[:10]

    # Pass top movies to template
    context = {'top_movies': top_movies}
    return render(request, 'recommendation.html', context)
