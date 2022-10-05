const searchInput = document.getElementById("td-input");

// store name elements in array-like object
const names = document.getElementsByClassName("_tde-info");
const tags = document.getElementsByClassName("_tde-tags");

// listen for user events
searchInput.addEventListener("keyup", (event) => {
    const { value } = event.target;

    // get user search input converted to lowercase
    const searchQuery = value.toLowerCase();

    for (const nameElement of names) {
        // store name text and convert to lowercase
        let name = nameElement.textContent.toLowerCase();

        // compare current name to search input
        if (name.includes(searchQuery)) {
            // found name matching search, display it

            nameElement.parentNode.style.display = "block";
        } else {
            // no match, don't display name
            nameElement.parentNode.style.display = "none";
        }
    }
});

$(document).on('click','._td-te', function(){
  var clickedValue = $(this).text();

  $('._td-te').removeClass('tag-active');
  $(this).addClass('tag-active');

  for (const tag of tags) {
    let tagString = tag.textContent.toLowerCase();

    if(clickedValue != '#all'){
      if (tagString.includes(clickedValue)){
        tag.parentNode.style.display = "block";
        } else {
        tag.parentNode.style.display = "none";
      }
    } else {
       tag.parentNode.style.display = "block";
    }
  }


});
