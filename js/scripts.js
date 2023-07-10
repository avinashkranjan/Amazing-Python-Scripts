document.addEventListener('DOMContentLoaded', function (event) {
  const requestURL = 'datastore.json';
  const request = new XMLHttpRequest();
  request.open('GET', requestURL);
  request.responseType = 'json';
  request.send();
  request.onload = processData;

  let currentPage = 1;

  function processData() {
    const data = request.response;
    let jsonData = JSON.parse(JSON.stringify(data));
    let categories = Object.keys(jsonData);
    let scriptNumber = 1;

    for (category in categories) {
      var category_scripts = jsonData[categories[category]];
      for (script in category_scripts) {
        var scriptDetails = {
          name: script,
          summary: category_scripts[script][5],
          author: category_scripts[script][4],
          folder: category_scripts[script][0],
          file: category_scripts[script][1],
        };
        populateCards(scriptNumber, scriptDetails);
        scriptNumber++;
      }
    }
    displayAllCards();
    updatePageNumber();
    updateButtonStates();
  }

  function displayAllCards() {
    const cardsPerPage = 16;
    const startIndex = (currentPage - 1) * cardsPerPage;
    const endIndex = startIndex + cardsPerPage;

    let cards = document.getElementById('card-holder').children;
    for (let count = 0; count < cards.length; count++) {
      if (count >= startIndex && count < endIndex) {
        cards[count].style.display = 'block';
      } else {
        cards[count].style.display = 'none';
      }
    }
  }

  function updatePageNumber() {
    let pageNumberElement = document.getElementById('page-number');
    pageNumberElement.textContent = currentPage;
  }

  function updateButtonStates() {
    let prevPageButton = document.getElementById('prevPage');
    let nextPageButton = document.getElementById('nextPage');
    const totalPages = getTotalPages();

    if (currentPage === 1) {
      prevPageButton.classList.add('disabled');
    } else {
      prevPageButton.classList.remove('disabled');
    }

    if (currentPage === totalPages) {
      nextPageButton.classList.add('disabled');
    } else {
      nextPageButton.classList.remove('disabled');
    }
  }

  function getTotalPages() {
    const cardsPerPage = 16;
    const totalCards = document.getElementById('card-holder').children.length;
    return Math.ceil(totalCards / cardsPerPage);
  }

  document.getElementById('prevPage').addEventListener('click', function () {
    if (currentPage > 1) {
      currentPage--;
      displayAllCards();
      updatePageNumber();
      updateButtonStates();
      scrollToTop();
    }
  });

  document.getElementById('nextPage').addEventListener('click', function () {
    const totalPages = getTotalPages();

    if (currentPage < totalPages) {
      currentPage++;
      displayAllCards();
      updatePageNumber();
      updateButtonStates();
      scrollToTop();
    }
  });

  function populateCards(scriptNumber, scriptDetails) {
    let cardHolder = document.getElementById('card-holder');
    let isHidden = scriptNumber <= 20 ? '' : 'hidden';

    let divHTML = `<div class="col-sm-6 col-md-3 ${isHidden} ">
                      <div class="card shadow">
                          <div class="card-body">
                              <h5 class="card-title">${scriptDetails['name']}</h5>
                              <p class="card-text">${scriptDetails['summary']}</p>
                              <p><a href="https://github.com/${scriptDetails['author']}">${scriptDetails['author']}</a></p><br>
                              <a href="https://github.com/avinashkranjan/Amazing-Python-Scripts/blob/master/${scriptDetails['folder']}/${scriptDetails['file']}" class="btn btn-primary">Take Me</a>
                          </div>
                      </div>
                  </div>`;
    cardHolder.innerHTML += divHTML;
  }

  function Search() {
    let cardsCount = document.getElementById('card-holder').children.length;
    let cards = document.getElementById('card-holder').children;
    let searchKey = document.getElementById('search').value.toLowerCase();
    for (let count = 0; count < cardsCount; count++) {
      scriptTitle = cards[count]
        .getElementsByTagName('h5')[0]
        .innerHTML.toLowerCase();
      if (scriptTitle.includes(searchKey)) {
        cards[count].style.display = 'block';
      } else {
        cards[count].style.display = 'none';
      }
    }
  }

  let search = document.getElementById('search');
  search.addEventListener('keydown', Search);
// Handle Scroll to Top Function
  document.getElementById('scroll-top').addEventListener('click', function () {
    scrollToTop();
  });

  function scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }
});
