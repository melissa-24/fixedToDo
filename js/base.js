var dateTime = new Date()
console.log('current dateTime', dateTime)

var aDate = dateTime.toLocaleDateString()
console.log('current Date', aDate)

// var theDate = document.getElementById('dayDate')
// console.log(aDate)
// theDate.innerText = aDate
document.getElementById('dayDate').innerText = aDate