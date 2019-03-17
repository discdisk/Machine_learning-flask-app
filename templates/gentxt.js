let button;
let postData;
let url='/gentext';
function setup() {
  var inp = createInput('');
  inp.position(100,250);
  inp.input(myInputEvent);

  button = createButton('click me');
  button.position(150, 250);
  button.mousePressed(passTheword);
}



function myInputEvent() {
  console.log('you are typing: ', this.value());
  postData = {word:  this.value()}
}
function passTheword(){
	httpPost(url,'json',postData,function(result){console.log(result)});
}
