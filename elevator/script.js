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
const curtext = "Current Floor: ";

const max_floor = 10;
const min_floor = 1;

const getRandomFloor  = (min, max) => {
    min = Math.floor(min);
    max = Math.ceil(max);
    return Math.floor(Math.random() * (max - min + 1) + min).toString();
}

const compare = (elevator1, elevator2, elevator3, requested_floor, cur_floor) => {
    // usr_floor.innerHTML.replace(/curtext /g, '')
    let cloest_to_usr = [];

    const e1textnum = elevator1.replace(e1text, '');
    const e2textnum = elevator2.replace(e2text, '');
    const e3textnum = elevator3.replace(e3text, '');

    const e1floor = parseInt(e1textnum) - cur_floor;
    const e2floor = parseInt(e2textnum) - cur_floor;
    const e3floor = parseInt(e3textnum) - cur_floor;
    console.log(e1floor);

    var elevators_to_usr = [e1floor, e2floor, e3floor];

    console.log(elevators_to_usr[0]);

    for (let i = 0; i < 3; i++) {
        if (elevators_to_usr[i] < 0) {
            elevators_to_usr[i] *= -1;
        }
    }

    let cloest_val = Math.min(...elevators_to_usr);

    for (let j = 0; j < 3; j++) {
        if (elevators_to_usr[j] == cloest_val) {
            cloest_to_usr.push(elevators_to_usr[j]);
        }
    }

    return [cloest_to_usr, elevators_to_usr];

};

const goToFloor = (requested_floor, current_floor) => {
    if (requested_floor === current_floor || isNaN(requested_floor) || requested_floor > 10 || requested_floor < 1) {
        return;
    } else {
        let return_val = compare(elevator1_cur_floor.innerHTML, elevator2_cur_floor.innerHTML, elevator3_cur_floor.innerHTML, requested_floor, current_floor);

        for (let i = 0; i < 3; i++) {
            if (return_val[1][i] === return_val[0][i]) {
                var elevator_code = i;
                break;
            }
        }

        console.log(return_val);

        if (elevator_code === 0) {
            usr_floor.innerHTML = curtext + requested_floor.toString();
            elevator1_cur_floor.innerHTML = e1text + + requested_floor.toString();
        } else if (elevator_code === 1) {
            usr_floor.innerHTML = curtext + requested_floor.toString();
            elevator2_cur_floor.innerHTML = e2text + + requested_floor.toString();
        } else if (elevator_code === 2) {
            usr_floor.innerHTML = curtext + requested_floor.toString();
            elevator3_cur_floor.innerHTML = e3text + + requested_floor.toString();
        }
    }
}

let e1randfloor = getRandomFloor(min_floor, max_floor);
let e2randfloor = getRandomFloor(min_floor, max_floor);
let e3randfloor = getRandomFloor(min_floor, max_floor);

usr_floor.innerHTML = curtext + getRandomFloor(min_floor, max_floor);
elevator1_cur_floor.innerHTML = e1text + e1randfloor;
elevator2_cur_floor.innerHTML = e2text + e2randfloor;
elevator3_cur_floor.innerHTML = e3text + e3randfloor;

btn.addEventListener("click", function() {
    goToFloor(parseInt(request_floor.value), parseInt(usr_floor.innerHTML.replace(curtext, '')));
});