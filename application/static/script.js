var cookieNames = ["Chocolatey Goodness", "Square Oreo", "Vanilla Wafer of Wisdom", "A Really Good Cookie", "Something Sweet"];
var cookieTypes = ["Chocolate Chip", "Candy", "Sugar Free", "Really Good", "Gourmet"];
var buyerNames = ["John", "Jerry", "The Man", "Obama", "Poncho"]
var distNames = ["Tom and  Jerries", "Old Guys", "A Pretty Lady"]
var cookieDistributors = ["Cookie Supplier Inc.", "We Got Cookies", "Made by Your Grandmother"]
var warehouseNames = ["Monopoly House", "Where the Anarchists Are", "Secret Palace", "Cookie Mansion", "Warehouse in the Sky"]
var addresses = ["Hell", "Sesame Street", "Your Backyard", "I forgot", "www.cookies.com"]
shuffle(cookieNames);
shuffle(cookieTypes);
shuffle(buyerNames);
shuffle(warehouseNames);

var cookieTemplate = $('#cookieTemplate').html();
var distTemplate = $('#distTemplate').html();
var buyerTemplate = $('#buyerTemplate').html();

var view = { dists: []}

distNames.forEach(function(name){
  var dist = {
    name: name,
    address: addresses[Math.floor(Math.random() * 5)],
    cookies: Math.floor(Math.random() * 500)
  }

  view.dists.push(dist)
});

var output = Mustache.render(distTemplate, view);
$('#dists').append(output)

view = {cookies: []};
for(var i = 0; i < 5; i++) {
  var cookie = {
    name: cookieNames[i],
    type: cookieTypes[i],
    distributor: cookieDistributors[Math.floor(Math.random() * 3)],
    count: randomCount(),
    warehouse: warehouseNames[i],
    price: randomPrice()
  };

  view.cookies.push(cookie);
};

output = Mustache.render(cookieTemplate, view);
$('#cookies').append(output)

var warehouseTemplate = $('#warehouseTemplate').html()
view = {warehouses: []}

shuffle(warehouseNames)
shuffle(addresses)

warehouseNames.forEach(function(name, i){
  var w = {
    name: name,
    address: addresses[i],
    cookies: Math.floor(Math.random() * 5000),
    cookie1: cookieNames[Math.floor(Math.random() * 5)],
    cookie2: cookieNames[Math.floor(Math.random() * 5)],
    cookie3: cookieNames[Math.floor(Math.random() * 5)],
  }

  view.warehouses.push(w)
});

output = Mustache.render(warehouseTemplate, view);
$('#warehouses').append(output)

view = {buyers: []}
buyerNames.forEach(function(name){
  var buyer = {
    name: name
  }
  view.buyers.push(buyer)
})

output = Mustache.render(buyerTemplate, view)
$("#buyers").append(output)

function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex ;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

function randomCount(){
  return Math.floor(Math.random() * 500)
}

function randomPrice(){
  return String(Math.floor(Math.random() * 10)) + ".99"
}