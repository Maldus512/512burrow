$( document ).ready(function() {
    $("a.question").on("click", function(event) {
           el = $(event.target).siblings().filter("p.answer")
           signal = $(event.target).children().filter("span.plusminus")
           x = $(el).css("display")
           if (x != "block") {
               $(el).css("display", "block") 
               $(signal).text("- ")
           }
           else {
               $(el).css("display", "none") 
               $(signal).text("+ ")
           }
           return false
       })
    console.log($("a.question"))
})
