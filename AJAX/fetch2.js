
function getUserPage(pagenum) {
    return fetch(`https://reqres.in/api/users?page=${pagenum}`)
    .then(function(response){
        return response.json()
    })
    .then(function(response){
        return response.data[prompt("Enter Index")].id
    })
}

function getUserID(id){
    return fetch(`https://reqres.in/api/users/${id}`)
    .then(function(response){
        return response.json()
    })
    .then(function(response){
        return response.data
    })
}

function renderHTML(el){
    document.write(`<h1>${el.id}</h1>`)
    document.write(`<h1>${el.email}</h1>`)
    document.write(`<h1>${el.first_name}</h1>`)
    document.write(`<h1>${el.last_name}</h1>`)
    document.write(`<img src= ${el.avatar}>`)
}

let id = getUserPage(prompt("Enter Page Number "))

.then(function(id){
    return getUserID(id)
})

.then(function(obj){
    renderHTML(obj)
})

