$(function(){
  $.ajax("/static/templates/main.html")
    .done(function(data){
      $("#main-content").html(data)
    });
})