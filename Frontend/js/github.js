let search_form = document.getElementById("search-form");

search_form.addEventListener("submit", function (event) {
  event.preventDefault();
  let search_query = document.getElementById("search");

  // let { search_query } = this.elements;

  let giturl = "http://127.0.0.1:5000/github?query=" + search_query.value;


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
    .then(() => {
      const stop = new Date().getTime() / 1000;
      console.log("Serial Time: ", stop - start);
    })
    .catch((err) => {
      console.log(err);
    });

  
    
});