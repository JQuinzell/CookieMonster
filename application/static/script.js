var $main

var cookieData = {
  "cookies": [
    {
      name: "Your mother made it",
      price: "5.99"
    },
    {
      name: "Chocolate",
      price: "2.99"
    }
  ]
}

var warehouseData = {
  "warehouses": [
    {
      name: "Warehouse1",
      address: "A street"
    },
    {
      name: "Warehouse9000",
      address: "Mars"
    }
  ]
}

$(function(){
  $main = $("#main-content")

  loadMainPage()

  $("li.cookies").click(loadCookiePage)
  $("li.warehouses").click(loadWarehousePage)
  $("li.distributors").click(loadDistributorPage)
  $("li.buyers").click(loadBuyerPage)
})

function setContent(html) {
  $main.html(html)
}

function loadMainPage() {
  $.ajax("/static/templates/main.html")
    .done(function(data){
      setContent(data)
    })
}

function loadCookiePage() {
  $.ajax("/static/templates/cookies.html")
    .done(function(data){
      data = Mustache.render(data, cookieData)
      setContent(data)
    })
}

function loadWarehousePage() {
  $.ajax("/static/templates/warehouses.html")
    .done(function(data){
      data = Mustache.render(data, warehouseData)
      setContent(data)
    })
}

function loadDistributorPage() {
  $.ajax("/static/templates/distributors.html")
    .done(function(data){
      setContent(data)
    })
}

function loadBuyerPage() {
  $.ajax("/static/templates/buyers.html")
    .done(function(data){
      setContent(data)
    })
}