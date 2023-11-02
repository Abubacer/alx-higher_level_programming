// Fetches from an URL and prints how to say “Hello” depending on the language.
const $ = window.$;
const ApiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=';
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.get(ApiUrl + languageCode, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
