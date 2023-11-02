// Fetches from an URL and displays the value of hello from that fetch in the HTML tag DIV#hello.
const $ = window.$;
const ApiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.get(ApiUrl, function (data) {
    $('#hello').text(data.hello);
  });
});
