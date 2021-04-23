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
      console.log("Parallel Time ", data["Total Parallel"]);
    })
    .catch((err) => {
      console.log(err);
    });
});
