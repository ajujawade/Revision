// let q1 = document.querySelector('.two')
// console.log(q1)

// let q2 = document.querySelector('.cc')
// console.log(q2)

// let q3 = document.querySelector('h1')
// console.log(q3)

// let byttribute = document.querySelector(id = '[one]')

// let button = document.querySelector('button')
// let intext = document.querySelector('input')
// let ulist = document.querySelector('ul')


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


// button.addEventListener('click', function() {

//     let text = intext.value
//     let newli = document.createElement('li')
//     newli.textContent = text
//     ulist.appendChild(newli)
//     intext.value = ""

// })


let q1 = document.querySelector('.two')
console.log(q1)

// let q2 = document.querySelector('.cc')
// console.log(q2)

let q3 = document.querySelector('h1')
console.log(q3)

let byttribute = document.querySelector(id = '[one]')

let changecolorbutton = document.querySelector('.changecolor')
let intext = document.querySelector('input')
let ulist = document.querySelector('ul')
let addelbutton = document.querySelector('.addelement')
let headone = document.querySelector('h1')


changecolorbutton.addEventListener('click', function() {

    let val = intext.value
    headone.style.color = val
    ulist.style.color = val
    intext.value = ''

})



addelbutton.addEventListener('click', function() {

    let newel = document.createElement('li')
    let text = intext.value
    newel.textContent = text
    if (text == '') {
        pass
    } else {
        createButton('Remove', 'remove', newel)
        createButton('Up', 'up', newel)
        createButton('Down', 'down', newel)
    }
    ulist.appendChild(newel)
    intext.value = ''

})



function createButton(textCon, className, el) {

    let newbutton = document.createElement('button')
    newbutton.textContent = textCon
    newbutton.classList.add(className)
    el.appendChild(newbutton)


}

ulist.addEventListener('click', function(event) {

    // console.log(event)
    // console.log(event.target)
    // console.log(event.target.tagName)

    if (event.target.tagName === 'BUTTON') {

        if (event.target.className === 'remove') {

            let li = event.target.parentElement
            let ulist = li.parentElement
            ulist.removeChild(li)

        } else if (event.target.className === 'up') {

            let li = event.target.parentElement
            let ulist = li.parentElement
            let prev = li.previousElementSibling
            if (prev) {

                ulist.insertBefore(li, prev)

            }

        } else if (event.target.className === 'down') {

            let li = event.target.parentElement
            let ulist = li.parentElement
            let next = li.nextElementSibling
            if (next) {

                ulist.insertBefore(next, li)

            }

        }
    }


})