document.addEventListener('DOMContentLoaded', (event) => {
  const requestURL = 'datastore.json';
  const request = new XMLHttpRequest();
  request.open('GET', requestURL);
  request.responseType = 'json';
  request.send();
  request.onload = processData;

  function processData() {
    const data = request.response;
    const authors = [];
    const jsonData = JSON.parse(JSON.stringify(data));
    const categories = Object.keys(jsonData);
    let scriptNumber = 1;
    
    for (const category of categories) {
      const categoryScripts = jsonData[category];
      for (const script of categoryScripts) {
        const author = script[4];
        authors.push(author);
        scriptNumber++;
      }
    }
    
    const authorsArray = sortByFrequency(authors);
    const contributors = Array.from(new Set(authorsArray));
    contributorCards(contributors);
  }

  function contributorCards(contributors) {
    const contributorHolder = document.getElementById('contributors-holder');
    
    for (const contributor of contributors) {
      const div = document.createElement('div');
      div.className = 'col-md-2 col-sm-6 my-2';
      div.innerHTML = `
        <div class="contributor-card card shadow-sm border-2 rounded">
          <div class="card-body p-0">
            <img src="https://github.com/${contributor}.png?size=125" alt="" class="card-img-top">
            <div class="contributor-name">
              <a href="https://github.com/${contributor}" class="mt-2">
                <h6 class="mb-0">${contributor} <i class="fab fa-github"></i></h6>
              </a>
            </div>
          </div>
        </div>
      `;
      contributorHolder.appendChild(div);
    }
  }

  const search = document.getElementById('search-contributor');
  search.addEventListener('input', searchContributor);

  function searchContributor() {
    const contributors = document.querySelectorAll('.contributor-card');
    const searchKey = search.value.toLowerCase();
    
    contributors.forEach((contributor) => {
      const contributorName = contributor.querySelector('h6').textContent.toLowerCase();
      
      if (contributorName.includes(searchKey)) {
        contributor.style.display = 'block';
      } else {
        contributor.style.display = 'none';
      }
    });
  }

  function sortByFrequency(array) {
    const frequency = {};
    
    array.forEach((value) => {
      frequency[value] = 0;
    });

    const uniques = array.filter((value) => {
      return ++frequency[value] === 1;
    });

    return uniques.sort((a, b) => {
      return frequency[b] - frequency[a];
    });
  }
});
