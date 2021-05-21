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
      let tweet = data["Tweets"];
      console.log(tweet);
      console.log(tweet.length);
      {
        let div = document.getElementById("tweets_h");
        div.innerHTML = `<blockquote class='header'>Tweets</blockquote>`
      }
      for (let links = 0; links < data["Tweets"].length; ++links) {
        div.innerHTML += `<blockquote class="twitter-tweet">
          <p>
          ${data["Tweets"][links].text}
          </p>
          <p>Sentiment: ${data["Tweets"][links].sentiment}</p>
          <p> Tweet url: <a href="${tweet[links]['link']}">
          ${tweet[links]['link']}
        </p>
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