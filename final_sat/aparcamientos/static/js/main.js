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

function sortTable() {
  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.getElementById("tabla_likes");
  switching = true;
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.getElementsByTagName("TR");
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[5];
      y = rows[i + 1].getElementsByTagName("TD")[5];
      //check if the two rows should switch place:
      if (parseInt(x.innerHTML) < parseInt(y.innerHTML)) {
        //if so, mark as a switch and break the loop:
        shouldSwitch= true;
        break;
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }
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
  sortTable();
  pagination(5, "#tabla_likes tbody tr");




})
