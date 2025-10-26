import requests

# IMPORTANT: This function could be improved using something equivalent to promise.all in JavaScript 
# to send all requests at the same time and reduce significatively the time it takes to fetch data.
# To keep a simpler solution I'll not use async await
 


def bestInGenre(genre: str) -> str:

  # Get all TV shows
  tvshows = getAllTvShows()

  # Filter by genre
  filtered_tvshows = [tvshow for tvshow in tvshows if genre.lower().strip() in tvshow['genre'].lower().split(', ')]

  if len(filtered_tvshows) == 0:
    raise LookupError(f'There are not tvshows with genre: {genre}')

  # Order by imdb rating
  sorted_tvshows = sorted(filtered_tvshows, key=lambda tvshow: tvshow['imdb_rating'], reverse=True)

  # Get a tie list with the top imdb rating tvshows
  max_imdb = sorted_tvshows[0]['imdb_rating']

  top_tvshows = []

  for tvshow in sorted_tvshows:
    if tvshow['imdb_rating'] == max_imdb:
      top_tvshows.append(tvshow)
    else:
      break # Exit from loop to avoid iterate all items

  # Order by name ascending
  sorted_top_tvshows = sorted(top_tvshows, key=lambda tvshow: tvshow['name'])

  # Return the name of the first tvshow in the tvshows list ordered by name ascending
  return sorted_top_tvshows[0]['name']

def main():

  bestTvshow = bestInGenre('Action')
  # bestTvshow = bestInGenre('Thrillers') # Incorrect genre

  print(bestTvshow)

if __name__ == "__main__":
  main()
