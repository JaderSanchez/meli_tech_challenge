import asyncio
import aiohttp
 
BASE_URL = "https://jsonmock.hackerrank.com/api/tvseries?page="

async def fetch_page(session, page: int):
  async with session.get(BASE_URL + str(page)) as response:
    return await response.json()

async def get_all_tvshows():

  async with aiohttp.ClientSession() as session:

    # Get first page to extract total_pages
    first_page_data = await fetch_page(session, 1)
    total_pages = first_page_data["total_pages"]

    # Create tasks for all other pages
    tasks = [fetch_page(session, page) for page in range(2, total_pages + 1)]

    # Execute all task in parallel
    results = await asyncio.gather(*tasks)

    # Combine all data
    all_data = first_page_data["data"]

    for r in results:
      all_data.extend(r["data"])

    return all_data


async def bestInGenre(genre: str) -> str:

  # Get all TV shows
  tvshows = await get_all_tvshows()

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

async def main():

  bestTvshow = await bestInGenre('Action')
  # bestTvshow = await bestInGenre('Thrillers') # Incorrect genre

  print(bestTvshow)

if __name__ == "__main__":
  asyncio.run(main())
