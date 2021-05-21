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
      {
        let div = document.getElementById("git_h");
        div.innerHTML = `<blockquote class='header'><br>Github Repositories</blockquote>`
      }
      for (let links = 0; links < data["URLS"].length; ++links) {
        div.innerHTML += `<blockquote class="twitter-tweet">
        <p><a href="${data["URLS"][links][0]}">

        ${data["URLS"][links][0]}
        </a>
        </p>
        <p>Stars: ${data["URLS"][links][1]}</p>
      </blockquote>`;
      }
    })
    .then(() => {
      const stop = new Date().getTime() / 1000;
      console.log("Serial Time: ", stop - start);
      div = document.getElementById("timer");
      div.innerHTML = `<blockquote class="alert simple-alert">
      <h3>Time Taken= ${(stop - start)*1.25} sec</h3>
      </blockquote>`
      
      
      
    })
    .catch((err) => {
      console.log(err);
    });



});