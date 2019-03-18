function setup() {
    let data="";
    let button = createButton('send');
    let inp = createInput('asda');
    inp.input(myInputEvent);
    button.mousePressed(send_text);
}
function draw() {

}

function myInputEvent() {
  console.log('you are typing: ', this.value());
  data=this.value();
}

function send_text(){
    let tt = document.getElementById("div1");
    tt.innerHTML=('updating...');
    let postData = {input:  data};
    let url = '/demot';
    httpPost(url,'json',postData,function(result){tt.innerHTML=('answer is:'+result['txt']);});
}