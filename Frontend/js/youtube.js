let search_form = document.getElementById("search-form");

search_form.addEventListener("submit", function (event) {
  event.preventDefault();
  let search_query = document.getElementById("search");

  let yturl = "http://127.0.0.1:5000/youtube?query=" + search_query.value;

  var start = new Date().getTime() / 1000;

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
    .then(() => {
      const stop = new Date().getTime() / 1000;
      console.log("Serial Time: ", stop - start);
    })
    .catch((err) => {
      console.log(err);
    });
});
