// const specific_date = new Date('2023-04-01');

const cal = [];

const getDays = (year, month) => {
    let days = 0;
    if (month === 2) {
        if (year % 4 === 0) {
            if (year % 100 === 0) {
                if (year % 400 === 0) {
                    days = 29;
                    return days; // Leap year
                } else {
                    days = 28;
                    return days; // Not a leap year
                }
            } else {
                days = 29;
                return days; // Leap year
            }
        } else {
            days = 28;
            return days; // Not a leap year
        }
    } else if (month === 1, month === 3, month === 5, month === 7, month === 8, month === 10, month === 12) {
        days = 31;
        return days;
    } else {
        days = 30;
        return days;
    }
        
}

const push_zero = (total) => {
    let push_times = 0;
    while (push_times != total) {
        cal.push(0);
        push_times += 1;
    }
} 

const pushUntilFull = (count, totalDays) => {
    while (count != totalDays) {
        count += 1;
        cal.push(count);
    }
}

const append = (day_cnt, spe_date) => {
    let cnt = 0;
    if (spe_date.getDay() === 0) {
        pushUntilFull(cnt, day_cnt);
    } else if (spe_date.getDay() === 1) {
        push_zero(1);
        pushUntilFull(cnt, day_cnt);
    } else if (spe_date.getDay() === 2) {
        push_zero(2);
        pushUntilFull(cnt, day_cnt);
    } else if (spe_date.getDay() === 3) {
        push_zero(3);
        pushUntilFull(cnt, day_cnt);
    } else if (spe_date.getDay() === 4) {
        push_zero(4);
        pushUntilFull(cnt, day_cnt);
    } else if (spe_date.getDay() === 5) {
        push_zero(5);
        pushUntilFull(cnt, day_cnt);
    } else if (spe_date.getDay() === 6) {
        push_zero(6);
        pushUntilFull(cnt, day_cnt);
    }
}

// var noOfDays = getDays(2023, 4);

// append(noOfDays);

// console.log(month);

const done = document.getElementById("btn");
const usr_year = document.getElementById("year");
const user_month = document.getElementById("month");
const cal_head = document.getElementById("cal_header");
const cal_1 = document.getElementById("cal_1");
const cal_2 = document.getElementById("cal_2");
const cal_3 = document.getElementById("cal_3");
const cal_4 = document.getElementById("cal_4");
const cal_5 = document.getElementById("cal_5");

done.addEventListener('click', function() {
    let year = usr_year.value;
    let month = user_month.value;
    let output = year.toString() + "/" + month.toString();

    cal_head.innerText = output;

    let specific_date_str = "";

    if (month > 9) {
        specific_date_str = year.toString() + "-" + month.toString() + "-01";
    } else {
        specific_date_str = year.toString() + "-0" + month.toString() + "-01";
    }

    // console.log(typeof specific_date_str);

    // console.log(specific_date_str);

    const specific_date = new Date(specific_date_str);

    let noOfDays = getDays(year, month);

    append(noOfDays, specific_date);

    const print_cal = cal.map((element) => {
        // // var g_element = element;
        // let weeks = 0;
        // while (weeks - cal.length != 0) {
        //     for (let i = 0; i % 7 != 0; i++) {
        //         var week = "";
        //         if (element === 0) {
        //             week += "  ";
        //         } else {
        //             week += " " + element.toString;
        //         }
        //     }
        //     week += "<br>";
        //     weeks += 1;
        // }

        // cal_p.innerText = week;
    })

});