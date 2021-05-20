let search_form = document.getElementById("search-form");

search_form.addEventListener("submit", function (event) {
  event.preventDefault();
  let search_query = document.getElementById("search");

  let newsurl = "http://127.0.0.1:5000/webscrape?query=" + search_query.value;


  var start = new Date().getTime() / 1000;
  let newsResponse = fetch(newsurl)
    .then((res) => res.json())
    .then((data) => {
      let div = document.getElementById("main");
      console.log(data["Links"]);
      console.log(data["Links"].length);
      {
        let div = document.getElementById("news_h");
        div.innerHTML = `<blockquote class='header'><br>News Articles </blockquote>`
      }
      for (let links = 0; links < data["Links"][0].length; ++links) {
        div.innerHTML += `<blockquote class="twitter-tweet">
        <p><a href="${data["Links"][0][links]}">

        ${data["Links"][0][links]}
        </a>
        </p>
      </blockquote>`;
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
