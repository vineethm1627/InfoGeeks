let search_form = document.getElementById("search-form");

search_form.addEventListener("submit", function (event) {
  event.preventDefault();
  let search_query = document.getElementById("search");

  // let { search_query } = this.elements;

  let giturl = "http://127.0.0.1:5000/github?query=" + search_query.value;
  let yturl = "http://127.0.0.1:5000/youtube?query=" + search_query.value;
  let twitterurl = "http://127.0.0.1:5000/twitter?query=" + search_query.value;
  let newsurl = "http://127.0.0.1:5000/webscrape?query=" + search_query.value;

  let parallelurl =
    "http://127.0.0.1:5000/parallel?query=" + search_query.value;

  var start = new Date().getTime() / 1000;

  let gitResponse = fetch(giturl)
    .then((res) => res.json())
    .then((data) => {
      let div = document.getElementById("main");
      console.log(data["URLS"]);
      console.log(data["URLS"].length);
      for (let links = 0; links < data["URLS"].length; ++links) {
        div.innerHTML += `<div class="col">
            <div class="card">
           <div class="card-body">
           <h5 class="card-title">${data["URLS"][links][0]}</h5>
           <p class="card-text">Stars: ${data["URLS"][links][1]}</p>
          </div>
          </div>
          </div>`;
      }
    })
    .catch((err) => {
      console.log(err);
    });

  let ytResponse = fetch(yturl)
    .then((res) => res.json())
    .then((data) => {
      let div = document.getElementById("main");
      console.log(data["Videos"]);
      console.log(data["Videos"].length);
      for (let links = 0; links < data["Videos"].length; ++links) {
        div.innerHTML += `<div class="col">
            <div class="card">
           <div class="card-body">
           <h5 class="card-title">${data["Videos"][links]}</h5>
          </div>
          </div>
          </div>`;
      }
    })
    .catch((err) => {
      console.log(err);
    });

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
    .catch((err) => {
      console.log(err);
    });

  let newsResponse = fetch(newsurl)
    .then((res) => res.json())
    .then((data) => {
      let div = document.getElementById("main");
      console.log(data["Links"]);
      console.log(data["Links"].length);
      for (let links = 0; links < data["Links"][0].length; ++links) {
        div.innerHTML += `<div class="col">
            <div class="card">
           <div class="card-body">
           <h5 class="card-title">${data["Links"][0][links]}</h5>
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

  let parallelResponse = fetch(parallelurl)
    .then((res) => res.json())
    .then((data) => {
      console.log("Parallel Time ", data["Total Parallel"]);
    })
    .catch((err) => {
      console.log(err);
    });
});
