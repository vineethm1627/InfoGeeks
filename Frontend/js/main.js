let search_form = document.getElementById("search-form");

search_form.addEventListener("submit", function (event) {
  event.preventDefault();
  let search_query = document.getElementById("search");

  // let { search_query } = this.elements;

  let parallelurl =
    "http://127.0.0.1:5000/parallel?query=" + search_query.value;


  let parallelResponse = fetch(parallelurl)
    .then((res) => res.json())
    .then((data) => {
      var div = document.getElementById("timer");
      div.innerHTML = `<blockquote class="alert simple-alert">
      <h3>Time Taken= ${data["Total Parallel"]} sec</h3>
      </blockquote>`
      console.log("Parallel Time ", data["Total Parallel"]);

      {var div = document.getElementById("tweets_h");
      div.innerHTML =  `<blockquote class='header'><br>Tweets</blockquote>`}

      {var div = document.getElementById("twitter");  
     
      var tweet = data["Tweets"];
      console.log(tweet);
      console.log(tweet.length);
      for (let links = 0; links < tweet.length; ++links) {
        div.innerHTML += `<blockquote class="twitter-tweet">
        <p>

        ${tweet[links]['text']}
        </p>
        <p>Sentiment: ${tweet[links]['sentiment']}</p>

        <p>Tweet url: <a href="${tweet[links]['link']}">
        ${tweet[links]['link']} </a>
        </p>
      </blockquote>`;
      }}

      {var div = document.getElementById("news_h");
      div.innerHTML =  `<blockquote class='header'><br>News Articles </blockquote>`
      }


      {var div = document.getElementById("news");  
      var news = data["News"];
      console.log(news);
      console.log(news.length);
      for (let links = 0; links < news[0].length; ++links) {
        div.innerHTML += `<blockquote class="twitter-tweet">
      <p><a href="${news[0][links]}">

      ${news[0][links]}
      </a>
      </p>
    </blockquote>`;
      }
    }

    {var div = document.getElementById("yt_h");
      div.innerHTML=  `<blockquote class='header'><br>Youtube Videos</blockquote>`
    }


      {var div = document.getElementById("yt");  
      var vid = data["Youtube"]
      console.log(vid);
      console.log(vid.length);
      for (let links = 0; links < vid.length; ++links) {
        div.innerHTML += `<blockquote class="twitter-tweet">
        <p><a href="${vid[links]}">

        ${vid[links]}
        </a>
        </p>
      </blockquote>`;
      }
    }

    {var div = document.getElementById("git_h");
    div.innerHTML=  `<blockquote class='header'><br>Github Repositories</blockquote>`
  }
      
    {
      var div = document.getElementById("git");  
      var gitrepo = data['Github']
      console.log(gitrepo);
      console.log(gitrepo.length);
      for (let links = 0; links < gitrepo.length; ++links) {
        div.innerHTML += `<blockquote class="twitter-tweet">
        <p><a href="${gitrepo[links][0]}">

        ${gitrepo[links][0]}
        </a>
        </p>
        <p>Stars: ${gitrepo[links][1]}</p>
      </blockquote>`;
      }}
    })
    .catch((err) => {
      console.log(err);
})
});