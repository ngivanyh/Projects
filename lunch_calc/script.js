var input = document.getElementById("input-box");
var btn  = document.getElementById("calculate");
var p = document.querySelector("p");
var input_txt = input.value;

// create dom event that gets that value of textarea and if it is a number then it will change the p tag to that value
btn.addEventListener("click", function() {
    if (isNaN(input.value)){
        p.textContent = "Please enter a number";
    } else {
        console.log(input.value.split(""));
        p.textContent = input.value;
    }
});