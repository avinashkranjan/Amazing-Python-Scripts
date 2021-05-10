document.addEventListener('DOMContentLoaded', function (event) {
  const requestURL = 'datastore.json'
  const request = new XMLHttpRequest()
  request.open('GET', requestURL)
  request.responseType = 'json'
  request.send()
  request.onload = processData

  function processData() {
    const data = request.response
    const authors = []
    let jsonData = JSON.parse(JSON.stringify(data))
    let categories = Object.keys(jsonData)
    let scriptNumber = 1
    for (category in categories) {
      var category_scripts = jsonData[categories[category]]
      for (script in category_scripts) {
        author = category_scripts[script][4]
        authors.push(author)
        scriptNumber++
      }
    }
    authorsArray = sortByFrequency(authors)
    const contributors = Array.from(new Set(authorsArray))
    contributorCards(contributors)
  }

  function contributorCards(contributors) {
    const contributorHolder = document.getElementById('contributors-holder')
    for (let index = 0; index <= contributors.length; index++) {
      const divHTML = `<div class="col-md-2 col-sm-6 my-2">
                <div class="contributor-card card shadow-sm border-2 rounded">
                    <div class="card-body p-0"><img src="https://github.com/${contributors[index]}.png?size=125" alt="" class="card-img-top">
                        <div class="contributor-name">                      
                            <a href="https://github.com/${contributors[index]}" class="mt-2"> <h6 class="mb-0">${contributors[index]} <i class="fab fa-github"></i></h6></a>
                        </div>
                    </div>
                </div>
            </div>`
      contributorHolder.innerHTML += divHTML
    }
  }

  // Bind event listener
  let search = document.getElementById('search-contributor')
  search.addEventListener('keydown', searchContributor)

  function searchContributor() {
    let contributorsCount = document.getElementById('contributors-holder')
      .children.length
    let contributors = document.getElementById('contributors-holder').children
    let searchKey = document
      .getElementById('search-contributor')
      .value.toLowerCase()
    for (let count = 0; count < contributorsCount; count++) {
      contributorName = contributors[count]
        .getElementsByTagName('h6')[0]
        .innerHTML.toLowerCase()
      if (contributorName.includes(searchKey)) {
        contributors[count].style.display = 'block'
      } else {
        contributors[count].style.display = 'none'
      }
    }
  }

  function sortByFrequency(array) {
    var frequency = {}

    array.forEach(function (value) {
      frequency[value] = 0
    })

    var uniques = array.filter(function (value) {
      return ++frequency[value] == 1
    })

    return uniques.sort(function (a, b) {
      return frequency[b] - frequency[a]
    })
  }
})
