// Fetches and lists the title for all movie from an URL.
const $ = window.$;
const ApiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(ApiUrl, function (movieData) {
  movieData.results.forEach(function (movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
