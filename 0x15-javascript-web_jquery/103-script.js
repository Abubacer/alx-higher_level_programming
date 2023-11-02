// Fetches from an URL and prints how to say “Hello” depending on the language.
const $ = window.$;
const ApiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=';
$(document).ready(function () {
  $('#btn_translate, #language_code').on('click keypress', function (event) {
    if (event.type === 'click' || event.which === 13) {
      const languageCode = $('#language_code').val();
      $.get(ApiUrl + languageCode, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
