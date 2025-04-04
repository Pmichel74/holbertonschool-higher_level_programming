const movieList = document.querySelector('#list_movies');

fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    for (let index = 0; index < data.results.length; index++) {
      const newMovie = document.createElement('li');
      newMovie.textContent = data.results[index].title;
      movieList.appendChild(newMovie);
    }
  });
