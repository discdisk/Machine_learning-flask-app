let c
let b_clear
let answer
function setup() {
    answer = createElement('h2', 'answer will be here!');
    answer.id('textt')
    c=createCanvas(200,200);
    c.id('canvasss');
    background(200);
    let button = createButton('send');
    button.position(130, 270);
    button.mousePressed(send_pic);


    b_clear = createButton('clear');
    b_clear.position(40, 270);
    b_clear.mousePressed(clear_canvas);

}
function draw() {
    if (mouseIsPressed) {
        fill(0); // Set fill to white
        ellipse(mouseX, mouseY, 30, 30); // Draw white ellipse using RADIUS mode
    
    }
}

function clear_canvas(){
    background(200);
}
function send_pic() {
	var canvas = document.getElementById("canvasss");
    var tt = document.getElementById("textt");
	var dataURL = canvas.toDataURL("image/jpeg", 1.0);
	console.log(dataURL);
	let postData = {imgURI:  dataURL}
	let url = '/demotext';
	httpPost(url,'json',postData,function(result){tt.innerHTML=('answer is:'+result);});
}