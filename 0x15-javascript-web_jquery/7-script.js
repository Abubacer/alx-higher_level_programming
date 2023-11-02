// Fetches the character name from an URL and displays it in the HTML tag DIV#character.
const $ = window.$;
const ApiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(ApiUrl, function (characterData) {
  $('#character').text(characterData.name);
});
