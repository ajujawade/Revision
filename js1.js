// let list = ["Bunty", "Om", "Raj", "Tony", "Piyush"]

// console.log(typeof(list))

// //console.log(list)

// for (let i = 0; i < list.length; i++) {
//     console.log(list[i])
// }

// list.push("Ajay")
// console.log(list)

// list.forEach(function(el, index, arr) {
//     console.log(el)
// })


let list = ["Bunty", "Om", "Raj", "Tony", "Piyush"]
    // q1 = list.map(function(el, index, arr) {
    //     return "Welcome " + el
    // })

// console.log(q1)

// let num = [334, 224, 556, 677, 44, 566, 7, 8, 8]

// q2 = num.filter(function(el, index, arr) {
//     return el > 10
// })

// console.log(q2)

// q3 = num.reduce(function(acc, el, index, arr) {
//     return acc + el
// })

// console.log(q3)

//let fruits = ["Grapes", "Banana", "Gauva", "Chikoo"]

// console.log(fruits)

// fruits2 = ["Banana", "Chikoo"]
// fruits3 = fruits2.concat(fruits)
// console.log(fruits3)

// q5 = fruits.indexOf("Banana")
// console.log(q5)

// q1 = fruits.slice(0, 2)
// console.log(fruits)
// console.log(q1)

// q2 = fruits.splice(0, 2)
// console.log(fruits)
// console.log(q2)

let flatexample = [
    ["Grapes", "Banana", "Gauva", "Chikoo"],
    ["Nagpur", "Jaipur", "Chandrapur"],
    ["India", "USA", "Russian"]
]

console.log(flatexample)

console.log(flatexample.flat())

a1 = flatexample.flat()
console.log(a1)