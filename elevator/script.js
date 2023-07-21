// get all html tags i need to use
const usr_floor = document.getElementById("usr_floor");
const btn = document.getElementById("submit");
const elevator1_cur_floor = document.getElementById("elevator1_cur_floor");
const elevator2_cur_floor = document.getElementById("elevator2_cur_floor");
const elevator3_cur_floor = document.getElementById("elevator3_cur_floor");
const request_floor = document.getElementById("select_floor");

const e1text = "Elevator 1 Current Floor: ";
const e2text = "Elevator 2 Current Floor: ";
const e3text = "Elevator 3 Current Floor: ";

const max_floor = 10;
const min_floor = 1;

const getRandomFloor  = (min, max) => {
    min = Math.floor(min);
    max = Math.ceil(max);
    return Math.floor(Math.random() * (max - min + 1) + min).toString();
}

const compare = (elevator1, elevator2, elevator3, requested_floor, cur_floor) => {
    var elevators_to_usr = [elevator1 - cur_floor, elevator2 - cur_floor, elevator3 - cur_floor];

    let usr_to_destination = requested_floor - cur_floor;

    for (let i = 0; i < 3; i++) {
        if (elevators_to_usr[i] < 0) {
            elevators_to_usr[i] *= -1;
            elevators_to_usr += usr_to_destination;
        }
    }

    let cloest_to_usr = Math.min(...elevators_to_usr);

    return cloest_to_usr;

};

const goToFloor = (requested_floor, current_floor) => {
    if (requested_floor === current_floor || isNaN(requested_floor) || requested_floor > 10 || requested_floor < 1) {
        return;
    } else {
        let cloest = compare(elevator1_cur_floor, elevator2_cur_floor, elevator3_cur_floor, requested_floor, current_floor);

        for (let i = 0; i < 3; i++) {
            if (elevators_to_usr[i] == closet) {
                let elevator_code = i;
            }
        }

        if (elevator_code === 0) {
            usr_floor.innerHTML = "Current Floor: " + requested_floor.toString();
            elevator1_cur_floor.innerHTML = e1text + + requested_floor.toString();
        } else if (elevator_code === 1) {
            usr_floor.innerHTML = "Current Floor: " + requested_floor.toString();
            elevator2_cur_floor.innerHTML = e2text + + requested_floor.toString();
        } else if (elevator_code === 2) {
            usr_floor.innerHTML = "Current Floor: " + requested_floor.toString();
            elevator3_cur_floor.innerHTML = e3text + + requested_floor.toString();
        }
    }
}

usr_floor.innerHTML = "Current Floor: " + getRandomFloor(min_floor, max_floor);
elevator1_cur_floor.innerHTML = e1text + getRandomFloor(min_floor, max_floor);
elevator2_cur_floor.innerHTML = e2text + getRandomFloor(min_floor, max_floor);
elevator3_cur_floor.innerHTML = e3text + getRandomFloor(min_floor, max_floor);

btn.addEventListener("click", function() {
    goToFloor(parseInt(request_floor.value), parseInt(usr_floor.innerHTML.replace(/Current Floor: /g, '')));
});