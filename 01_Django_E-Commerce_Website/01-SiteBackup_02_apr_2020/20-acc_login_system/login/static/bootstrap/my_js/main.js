/* category menu scripts-------------------*/
$(document).ready(function(){
	
  $(".cat1_span,.cat1_box").hover(function(){
	$(".cat1_span > .material-icons").text("keyboard_arrow_up");
	$(".cat1_span").css("color","#00a183");
    $(".cat1_box").css("z-index",1);
    }, function(){
	$(".cat1_span > .material-icons").text("keyboard_arrow_down");
	$(".cat1_span").css("color","black");
    $(".cat1_box").css("z-index",-1);
  });

  $(".cat2_span,.cat2_box").hover(function(){
	$(".cat2_span > .material-icons").text("keyboard_arrow_up");
    $(".cat2_box").css("z-index",1);
    }, function(){
	$(".cat2_span > .material-icons").text("keyboard_arrow_down");
    $(".cat2_box").css("z-index",-1);
  });
  
  $(".cat3_span,.cat3_box").hover(function(){
	$(".cat3_span > .material-icons").text("keyboard_arrow_up");
    $(".cat3_box").css("z-index",1);
    }, function(){
	$(".cat3_span > .material-icons").text("keyboard_arrow_down");
    $(".cat3_box").css("z-index",-1);
  });
  
  $(".cat4_span,.cat4_box").hover(function(){
	$(".cat4_span > .material-icons").text("keyboard_arrow_up");
    $(".cat4_box").css("z-index",1);
    }, function(){
	$(".cat4_span > .material-icons").text("keyboard_arrow_down");
    $(".cat4_box").css("z-index",-1);
  });
  
  
  
  
  
  
  
  
  
});