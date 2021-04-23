let search_form = document.getElementById("search-form");

search_form.addEventListener("submit", function (event) {
  event.preventDefault();
  let search_query = document.getElementById("search");

  let twitterurl = "http://127.0.0.1:5000/twitter?query=" + search_query.value;

  var start = new Date().getTime() / 1000;

  let twitterResponse = fetch(twitterurl)
    .then((res) => res.json())
    .then((data) => {
      let div = document.getElementById("main");
      console.log(data["Tweets"]);
      console.log(data["Tweets"].length);
      for (let links = 0; links < data["Tweets"].length; ++links) {
        div.innerHTML += `<div class="col">
            <div class="card">
           <div class="card-body">
           <h5 class="card-title">${data["Tweets"][links].text}</h5>
           <p class="card-text">Sentiment: ${data["Tweets"][links].sentiment}</p>
          </div>
          </div>
          </div>`;
      }
    })
    .then(() => {
      const stop = new Date().getTime() / 1000;
      console.log("Serial Time: ", stop - start);
    })
    .catch((err) => {
      console.log(err);
    });

});