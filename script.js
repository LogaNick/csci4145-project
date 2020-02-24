var newsContainer = document.getElementById('news_container');
var btn = document.getElementById("news_btn");

btn.addEventListener("click", getNews());

function getNews() {
  var ourRequest = new XMLHttpRequest();
  ourRequest.open('GET', 'http://127.0.0.1:5000/news', true);
//  ourRequest.onload = function() {
//    if (ourRequest.status >= 200 && ourRequest.status < 400) {
//      var ourData = JSON.parse(ourRequest.responseText);
////      renderHTML(ourData);
//    } else {
//      console.log("We connected to the server, but it returned an error.");
//    }
//
//  };

//  ourRequest.onerror = function() {
//    console.log("Connection error");
//  };
//
  console.log(ourRequest.send());
}

//function renderHTML(data) {
//  var htmlString = "<p>" + data.body + date.user;
//  htmlString += '.</p>';
//
//  newsContainer.insertAdjacentHTML('beforeend', htmlString);
//}
