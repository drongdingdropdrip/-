var Links = {
    setColor:function(color){
    $('a').css('color', color);
  }
}
var Body = {
  setColor:function (color){
    $('body').css('color', color);
  },
  setBackgroundColor:function (color){
    $('body').css('backgroundColor', color);
  }
}
function nightDayHandler(drop){
  var target = document.querySelector('body');
  if(self.value === 'night'){
    Body.setBackgroundColor('black');
    Body.setColor('white');
    drop.value = 'day';
    Links.setColor('powderblue');
  } else {
    Body.setBackgroundColor('white');
    Body.setColor('black');
    drop.value = 'night';
    Links.setColor('blue');
  }
}
