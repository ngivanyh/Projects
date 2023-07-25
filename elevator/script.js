const usr_floor = document.getElementById("usr_floor");
const btn = document.getElementById("submit");
const elevator1_cur_floor = document.getElementById("elevator1_cur_floor");
const elevator2_cur_floor = document.getElementById("elevator2_cur_floor");
const elevator3_cur_floor = document.getElementById("elevator3_cur_floor");
const request_floor = document.getElementById("select_floor");

const html_text = ["Elevator 1 Current Floor: ", "Elevator 2 Current Floor: ", "Elevator 3 Current Floor: ", "Current Floor: "];

const getRandomFloor  = () => {
    min = Math.floor(1);
    max = Math.ceil(10);
    return Math.floor(Math.random() * (max - min + 1) + min).toString();
}

const compare = (elevator1, elevator2, elevator3, cur_floor) => {
    let cloest_to_usr = [];

    const e1floor = parseInt(elevator1.replace(html_text[0], '')) - cur_floor;
    const e2floor = parseInt(elevator2.replace(html_text[1], '')) - cur_floor;
    const e3floor = parseInt(elevator3.replace(html_text[2], '')) - cur_floor;

    var elevators_to_usr = [e1floor, e2floor, e3floor];

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
        const request_floor_str = requested_floor.toString();
        let return_val = compare(elevator1_cur_floor.innerHTML, elevator2_cur_floor.innerHTML, elevator3_cur_floor.innerHTML, current_floor);

        let i = 0;

        console.log(return_val[0][0]);

        while (return_val[1][i] != return_val[0][0]) {
            console.log(return_val[1][i]);
            i++
        }

        let elevator_code = i; 

        console.log(return_val, elevator_code);

        usr_floor.innerHTML = html_text[3] + request_floor_str;

        if (elevator_code === 0) {
            elevator1_cur_floor.innerHTML = html_text[0] + request_floor_str;
        } else if (elevator_code === 1) {
            elevator2_cur_floor.innerHTML = html_text[1] + request_floor_str;
        } else if (elevator_code === 2) {
            elevator3_cur_floor.innerHTML = html_text[2] + request_floor_str;
        }
    }
}

usr_floor.innerHTML = html_text[3] + getRandomFloor();
elevator1_cur_floor.innerHTML = html_text[0] + getRandomFloor();
elevator2_cur_floor.innerHTML = html_text[1] + getRandomFloor();
elevator3_cur_floor.innerHTML = html_text[2] + getRandomFloor();

btn.addEventListener("click", function() {
    goToFloor(parseInt(request_floor.value), parseInt(usr_floor.innerHTML.replace(html_text[3], '')));
});