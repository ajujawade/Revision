let calcAverage = (a, b, c) => (a + b + c) / 3
console.log(calcAverage(3, 4, 5))

//Test 1

let scoreIndia = calcAverage(40, 23, 71)
let scoreAus = calcAverage(65, 54, 49)
console.log(scoreIndia, scoreAus)

let winner = function(avgIndia, avgAus) {
    if (avgIndia >= 2 * avgAus) {
        console.log(`India Wins (${avgIndia} vs ${avgAus})`)
    } else if (avgAus >= 2 * avgIndia) {
        console.log(`Aus Wins (${avgAus} vs ${avgIndia} )`)
    } else {
        console.log('No team wins...')
    }
}

winner(scoreIndia, scoreAus)
winner(200, 1000)
scoreIndia = calcAverage(240, 123, 71)
scoreAus = calcAverage(65, 54, 49)
winner(scoreIndia, scoreAus)