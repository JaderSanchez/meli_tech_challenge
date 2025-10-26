# Problem

Use the HTTP GET method to retrieve information about recent television shows.
Query the API: 

https://jsonmock.hackerrank.com/api/tvseries

The query result is paginated. To access additional pages, append `?page={num}` to the URL where num is the page number.

**Response JSON Schema**

```
{
  "page": 1,
  "per_page": 10,
  "total": 200,
  "total_pages": 20,
  "data": [
    {
      "name": "Game of Thrones",
      "runtime_of_series": "(2011-2019)",
      "certificate": "A",
      "runtime_of_episodes": "57 min",
      "genre": "Action, Adventure, Drama",
      "imdb_rating": 9.3,
      "overview": "Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.",
      "no_of_votes": 1773458,
      "id": 1
    },
    ...
  ]
}
```


## Task Challenge

Given a genre, find the series with the highest imdb rating. If there is a tie, return the alphabetically lower name.

## Function Description

`def bestInGenre(genre: str) -> str:`

**Parameter:**
  genre (str): the genre to search

**Return:**
  str : the highest-rated show in the genre, with the lowest name alphabetically if there is a tie

### Sample

> Input: Action

> Output: Game of Thrones

## Sample Explanation

The 4 highest-rated shows in the Action genre are:

- Game of Thrones — 9.3
- Avatar: The Last Airbender — 9.2
- Hagane no renkinjutsushi — 9.1
- Shingeki no kyojin — 8.9

## How I'll solve it:

1. I need to get all tvshows, then I'll fetch all pages.

2. I'll filter by genre.

3. I'll sort by imdb rating descending.

4. Verify if there is a tie, and if it exists then order by name alphabetically.

5. I'll return the name of the first tvshow in the sorted list.