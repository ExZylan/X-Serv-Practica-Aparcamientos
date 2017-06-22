$(document).ready(function() {

  $('i.like').hover(
    function() {
      $(this).removeClass("fa-thumbs-o-up")
      $(this).addClass("fa-thumbs-up")
    }, function() {
      $(this).removeClass("fa-thumbs-up")
      $(this).addClass("fa-thumbs-o-up")
    }
  );

  $('i.favourite').hover(
    function() {
      $(this).removeClass("fa-heart-o")
      $(this).addClass("fa-heart")
    }, function() {
      $(this).removeClass("fa-heart")
      $(this).addClass("fa-heart-o")
    }
  );

  $('i.favourite').click(
    function() {
      $(this).removeClass("fa-heart-o")
      $(this).addClass("fa-heart")
    }
  );

})
