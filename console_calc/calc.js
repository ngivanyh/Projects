// some functions only work in a web browser's console

var mode  = prompt("Enter a mode (add/subtract/multiply/divide) : ");

var fnum = prompt("Enter first number: ");
var snum = prompt("Enter second number: ");

if (mode === "add") {
	alert(Number(fnum) + Number(snum));
} else if (mode === "subtract") {
	alert(Number(fnum) - Number(snum));
} else if (mode === "multiply") {
	alert(Number(fnum) * Number(snum));
} else if (mode === "divide") {
	alert(Number(fnum) / Number(snum));
} else {
	alert("Invalid mode");
}