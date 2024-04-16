let getUser = document.querySelector('button')

getUser.addEventListener('click',function(){

    fetch('https://reqres.in/api/users?page=2')
    .then(function(response){
        return response.json()
    })
    .then(function(response){
        console.log(response)
        console.log(response.data)
    

    response.data.forEach(function(el){
        document.write(`<h1>${el.id}</h1>`)
        document.write(`<h1>${el.email}</h1>`)
        document.write(`<h1>${el.first_name}</h1>`)
        document.write(`<h1>${el.last_name}</h1>`)
        document.write(`<img src= ${el.avatar}>`)
    })
})

})