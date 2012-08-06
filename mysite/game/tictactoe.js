var c = document.createElement("canvas");
$(c).attr("width") = 400;
$(c).attr("height") = 400;


var ctx = c.getContext("2d");
ctx.strokeStyle = "black";
ctx.strokeStyle = "blue";
ctx.lineWidth = 10;
ctx.beginPath();


ctx.beginPath();
ctx.arc(100, 100, 90, 0, 2*Math.PI);
ctx.fill();