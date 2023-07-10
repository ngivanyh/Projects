// get all html tags i need to use
const usr_floor = document.getElementById("usr_floor");
const btn = document.getElementById("submit");
const elevator1_cur_floor = document.getElementById("elevator1_cur_floor");
const elevator2_cur_floor = document.getElementById("elevator2_cur_floor");
const elevator3_cur_floor = document.getElementById("elevator3_cur_floor");
const request_floor = document.getElementById("select_floor");
const request_floor_val = request_floor.value;
console.log(request_floor.value);


const max_floor = 10;
const min_floor = 1;

const getRandomFloor  = (min, max) => {
    min = Math.floor(min);
    max = Math.ceil(max);
    return Math.floor(Math.random() * (max - min + 1) + min);
}


const goToFloor = (requested_floor, current_floor) => {
    console.log(typeof requested_floor, requested_floor);
    console.log(typeof current_floor, current_floor);
    if (requested_floor === current_floor || isNaN(requested_floor) || request_floor > 10 || request_floor < 1) {
        console.log("here")
        return;
    } else {
        console.log("hello world");
    }
}

usr_floor.innerHTML = "Current Floor: " + getRandomFloor(min_floor, max_floor).toString();
elevator1_cur_floor.innerHTML = "Elevator 1 Current Floor: " + getRandomFloor(min_floor, max_floor).toString();
elevator2_cur_floor.innerHTML = "Elevator 2 Current Floor: " + getRandomFloor(min_floor, max_floor).toString();
elevator3_cur_floor.innerHTML = "Elevator 3 Current Floor: " + getRandomFloor(min_floor, max_floor).toString();

btn.addEventListener("click", function() {
    goToFloor(parseInt(request_floor_val), parseInt(usr_floor.innerHTML.replace(/Current Floor: /g, '')));
});