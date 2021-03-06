function pagination(num_rows,element){
  var req_num_row=num_rows;
  var $tr=jQuery(element);
  var total_num_row=$tr.length;
  var num_pages=0;
  if(total_num_row % req_num_row ==0){
    num_pages=total_num_row / req_num_row;
  }
  if(total_num_row % req_num_row >=1){
    num_pages=total_num_row / req_num_row;
    num_pages++;
    num_pages=Math.floor(num_pages++);
  }
  for(var i=1; i<=num_pages; i++){
    jQuery('#pagination').append("<a>"+i+"</a>&nbsp;");
  }
  $tr.each(function(i){
    jQuery(this).hide();
    if(i+1 <= req_num_row){
      $tr.eq(i).show();
    }

  });
  jQuery('#pagination a').click(function(e){
    e.preventDefault();
    $tr.hide();
    var page=jQuery(this).text();
    var temp=page-1;
    var start=temp*req_num_row;
    //alert(start);

    for(var i=0; i< req_num_row; i++){

      $tr.eq(start+i).show();

    }
  });
}

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

  $('i.add_favourite').hover(
    function() {
      $(this).removeClass("fa-heart-o")
      $(this).addClass("fa-heart")
    }, function() {
      $(this).removeClass("fa-heart")
      $(this).addClass("fa-heart-o")
    }
  );

  $('i.del_favourite').hover(
    function() {
      $(this).removeClass("fa-heart")
      $(this).addClass("fa-heart-o")
    }, function() {
      $(this).removeClass("fa-heart-o")
      $(this).addClass("fa-heart")
    }
  );

  pagination(5, "#tabla_favs tbody tr");
  pagination(7, "#tabla_todos tbody tr");




})
