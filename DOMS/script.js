let q1 = document.querySelector('.two')
console.log(q1)

let q2 = document.querySelector('.cc')
console.log(q2)

let q3 = document.querySelector('h1')
console.log(q3)

let byttribute = document.querySelector(id = '[one]')

let button = document.querySelector('button')
let intext = document.querySelector('input')
let ulist = document.querySelector('ul')


// button.addEventListener('click', function() {

//     let textcolor = inp

// })


// button.addEventListener('click', function() {

//     let txt = text.value
//     let newel = document.createElement('li')
//     newel.textContent = txt
//     ulist.appendChild(newel)
//     text.value = ""

// })


button.addEventListener('click', function() {

    let text = intext.value
    let newli = document.createElement('li')
    newli.textContent = text
    ulist.appendChild(newli)
    intext.value = ""

})